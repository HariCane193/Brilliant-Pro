from tkinter import *
from PIL import ImageTk,Image
import os
import time
import mysql.connector as ms
import matplotlib.pyplot as plt


#username information
g = open('usernameinfo.txt')
u = g.readline()
#print(u)
g.close()
#database server connection
f = open('databaseinfo.txt')
x = ''
for i in range(3):
    x+=f.readline()
#x now has host,user,password used for logging into the database
x = x.split()
f.close()

mycon = ms.connect(host = x[0],user = x[1],password = x[2],database = u)
mycur = mycon.cursor()
dval1 = time.strftime('%Y')+'-'+time.strftime('%m')+'-'+time.strftime('%d')
mycur.execute(f"Select * from schedule where starttime > '{dval1+' '+time.strftime('%T')}' order by starttime")
tasks = mycur.fetchall();
#task,timer,status,datetime
ts_dtb = []
tim_dtb = []
date_dtb = []
st = []
for i in tasks:
    if i[2] == '0':
        ts_dtb.append(i[0])
        tim_dtb.append(i[1])
        date_dtb.append(i[3])
        st.append(i[2])
for i in range(len(tim_dtb)):
    val = [int(x) for x in tim_dtb[i].split(':')]
    sum1 = val[0]*3600+val[1]*60+val[2]
    tim_dtb[i] = sum1

main = Tk()
main.title('Timer')
main.geometry('1600x800')
main.resizable(0,0)

#BG
f = open('settings.txt')
BG = f.readline()[:-1]
f.close()

#Background
b_img = ImageTk.PhotoImage(Image.open(BG))
b_l = Label(main,image = b_img)
b_l.place(x = 0,y = 0)

#Main Timer Function
def timer(number):
    global endT,tskno,Suc_no,F_no,s_no,f_no
    c_task.config(text = 'Current Task: '+ts_dtb[tskno])

    try:
        upc.config(text = 'Upcoming Task: '+ts_dtb[tskno+1])
        upt.config(text = 'At: '+str(date_dtb[tskno+1]))
    except:
        upc.config(text = 'Upcoming Task: '+'All done!')
        upt.config(text = 'At: '+"All done!")
    if number==-1:
        f_no+=1
        F_no.config(text = f_no)
        mycur.execute(f"UPDATE schedule set status = 'i' where task = '{ts_dtb[tskno]}' and starttime = '{str(date_dtb[tskno])}'")
        mycon.commit()
        tskno+=1
        c_task.config(text = 'Current Task: Completing Backlog')
        End = Button(main,text = 'Finish',font = ('Arial Black',20),command = end)
        End.place(x = 730,y = 340)
        return None
    if endT:
        s_no+=1
        Suc_no.config(text = s_no)
        tskno+=1
        c_task.config(text = 'Current Task: On break')
        endT = False
            
        End = Button(main,text = 'Finish',font = ('Arial Black',20),command = end)
        End.place(x = 730,y = 340)
        return None
    hour = number//3600
    minute = (number%3600)//60
    second = number%60
    if hour<10:
        hour = '0'+str(hour)
    else:
        hour = str(hour)
    if minute<10:
        minute = '0'+str(minute)
    else:
        minute = str(minute)
    if second<10:
        second = '0'+str(second)
    else:
        second = str(second)
    t = hour+ ':' + minute +':' + second
    my_label.config(text = t)
    my_label.after(1000,lambda: timer(number-1))

endT = False


#Functions
def goback():
    we = open('back.txt','r')
    a = we.read()
    we.close()
    we = open('back.txt','w')
    we.write('timertest.py')
    we.close()
    main.destroy()
    os.system(f"python {a}")
def upload():

    os.system("python instapost.py")

def end():
    global endT
    endT = True
    success = Label(main,text = 'Nice! Continue Working!',font = ('Courier New',20))
    mycur.execute(f"UPDATE schedule set status = '1' where task = '{ts_dtb[tskno]}' and starttime = '{str(date_dtb[tskno])}'")
    mycon.commit()
    success.place(x = 630,y = 430)

def update():

    we = open('back.txt','w')
    we.write('timertest.py')
    we.close()
    main.destroy()
    os.system('python SchedulePage.py')

#REFRESH Function
def ref():
    main.destroy()
    os.system("python timertest.py")

def moveF(taskno):
    global sta,r_button,l_button,tsk,tsk_no,tot,ts_dtb
    tsk.config(text = ts_dtb[taskno][:-1])
    if taskno == len(ts_dtb)-1:
        r_button = Button(main,text = '>>',font = ('Courier New',20),state = DISABLED)

    else:
        r_button = Button(main,text = '>>',font = ('Courier New',20),command =lambda: moveF(taskno+1))


    l_button = Button(main,text = '<<',font = ('Courier New',20),command = lambda: moveB(taskno-1))
    r_button.place(x = 950,y = 550)
    l_button.place(x = 570,y = 550)
    tsk_no.config(text = 'Task '+str(taskno+1)+' of '+str(tot))


def moveB(taskno):
    global sta,r_button,l_button,tsk,tsk_no,tot,ts_dtb
    tsk.config(text = ts_dtb[taskno][:-1])

    if taskno == 0:
        l_button = Button(main,text = '<<',font = ('Courier New',20),state = DISABLED)

    else:
        l_button = Button(main,text = '<<',font = ('Courier New',20),command =lambda: moveB(taskno-1))


    r_button = Button(main,text = '>>',font = ('Courier New',20),command = lambda: moveF(taskno+1))
    r_button.place(x = 950,y = 550)
    l_button.place(x = 570,y = 550)
    tsk_no.config(text = 'Task '+str(taskno+1)+' of '+str(tot))

def setrun():
    os.system('python settings.py')

def graph():
    mycur.execute("Select * from grapheff order by DATE desc LIMIT 10")
    values = mycur.fetchall()
    values = values[::-1]
    valuesx,valuesy = [],[]
    for i,j in values:
        valuesx.append(str(i))
        valuesy.append(j)
    plt.ylabel('Efficiency * Successes')
    plt.xlabel('Date')
    plt.plot(valuesx,valuesy)
    plt.show()
def ue():
    mycur.execute(f"Select count(*) from schedule where starttime>'{dval+' 00:00:00'}' and starttime<'{dval+' 23:59:59'}' and status = '1'")
    (suc123,) = mycur.fetchone()
    mycur.execute(f"Select count(*) from schedule where starttime>'{dval+' 00:00:00'}' and starttime<'{dval+' 23:59:59'}'")
    (tot123,) = mycur.fetchone()
    if not (tot123):
        tot123 = 1
    mycur.execute(f"Insert into grapheff values('{dval}',{suc123*suc123/tot123})")
    mycon.commit()
    
#Buttons
upeff = Button(main,text = 'Upload Efficiency',font = ('Arial Black',20),command = ue)
upeff.place(x = 100,y = 500)
upgraph = Button(main,text = 'Efficiency Graph',font = ('Arial Black',20),command = graph)
upgraph.place(x = 100,y = 680)
#uplink = Button(main,text = 'UPLOAD',font = ('Arial Black',20),state = DISABLED)
#uplink.place(x = 100,y = 600)
if not len(tim_dtb):
    End = Button(main,text = 'Finish',font = ('Arial Black',20),state = DISABLED)
    End.place(x = 730,y = 340)
else:

    End = Button(main,text = 'Finish',font = ('Arial Black',20),command = end)
    End.place(x = 730,y = 340)

Update = Button(main,text = 'Schedule',font = ('Arial Black',28),command = update)
Update.place(x = 1350,y = 700)

if len(tim_dtb)<=1:
    r_button = Button(main,text = '>>',font = ('Courier New',20), state = DISABLED)
    r_button.place(x = 950,y = 550)
else:
    
    r_button = Button(main,text = '>>',font = ('Courier New',20),command =lambda: moveF(1))
    r_button.place(x = 950,y = 550)

l_button = Button(main,text = '<<',font = ('Courier New',20),state = DISABLED)
l_button.place(x = 570,y = 550)


photo = PhotoImage(file = r"Images/REFRESH.jpg")

refresh = Button(main,text = '',image = photo,command = ref)
refresh.place(x = 1450,y = 320)

sett = ImageTk.PhotoImage(Image.open("Images/settingsimg.jpg"))
settings = Button(main,text = '',image = sett,command = setrun)
settings.place(x = 1260,y = 320)

backarrow = ImageTk.PhotoImage(Image.open("Images/backarrow.jpg"))
back = Button(main,text = '',image = backarrow,command = goback).place(x = 20,y = 20)

tskno = 0
#Labels
s_no = 0
f_no = 0
Suc_no = Label(main,text = s_no,font = ('Arial Black',36),bg = 'black',fg = 'green')
F_no = Label(main,text = f_no,font = ('Arial Black',36),bg = 'black',fg = 'red')
Suc_no.place(x = 1350,y = 100)
F_no.place(x = 250, y = 100)

if len(tim_dtb):
    v = ts_dtb[tskno]
    a = 'On Break'
    t = str(date_dtb[tskno])
else:
    v = 'No Pending Tasks'
    a = 'No Pending Tasks'
    t = 'NA'

upc = Label(main,text = 'Upcoming Task: '+v,font = ('Arial Black',16))
upc.place(x = 1190,y = 500)

upt = Label(main,text = 'At: '+t,font = ('Arial Black',16))
upt.place(x = 1190,y = 550)

c_task = Label(main,text = 'Current Task: '+a,font = ('Arial Black',16))
c_task.place(x = 600,y = 140)

Tasks = Label(main,text = 'Tasks',font = ('Arial Black', 30))
Tasks.place(x = 725,y = 480)

Fails_T = Label(main,text = 'Failure Streak',font = ('Arial Black',30))
Fails_T.place(x = 150,y = 25)

Success_S = Label(main,text = 'Success Streak',font = ('Arial Black',30))
Success_S.place(x = 1200 ,y = 25)

my_label = Label(main,text = '00:00:00',font = ('Helvetica',72),bg='black',fg = 'red')
my_label.place(x = 600,y =210)

quote = Label(main,text = "Everyone has a plan 'till they get punched in the mouth.",font = ('Courier New',20))
quote.place(x = 15,y = 750)


#Frames
task_frame = LabelFrame(main,text = '',width = 100)
task_frame.place(x = 650,y = 555)

#In task_frame
if not len(ts_dtb):
    txt = 'No Pending tasks'
else:
    txt = ts_dtb[0]
tsk = Label(task_frame,text = txt ,fg = 'white',bg = 'black',font = ('Arial Black',20),width = 15)
tsk.pack()
no = 1
tot = len(ts_dtb)
if tot:
    tsk_no = Label(task_frame,text = 'Task '+str(no)+' of '+str(tot))
    tsk_no.pack()
else:
    
    tsk_no = Label(task_frame,text = 'No tasks left to complete')
    tsk_no.pack()

tdupload = 0
#Clock
def clock():
    global cval,dval,tskno,tdupload
    cval = time.strftime('%T')
    c.config(text = cval)
    if cval == '00:00:00':
        date()
        mycur.execute("Delete from schedule")
        mycon.commit()

    try:
        if len(tim_dtb) and str(date_dtb[tskno]) == dval+' '+ cval:
            timer(tim_dtb[tskno])
    except:
        pass
    if tskno==len(tasks) and len(tasks) and tdupload == 0:
        os.system('pytho:tn instapost.py')
        tdupload = 1
        ue()
    c.after(1000,clock)
        
c = Label(main,text = '',font = ('Arial Black',20),bg = 'white',fg = 'black')
c.place(x = 1400, y = 200)

#Date
def date():
    global dval
    dval = time.strftime('%Y')+'-'+time.strftime('%m')+'-'+time.strftime('%d')
    d.config(text = dval)
    

d = Label(main,text = '',font = ('Arial Black',20),bg = 'white',fg = 'black')
d.place(x = 1400,y = 250)

#Function calls
date()
clock()

main.mainloop()
