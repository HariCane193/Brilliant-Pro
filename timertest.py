from tkinter import *
from PIL import ImageTk,Image
import os
import time
import mysql.connector as ms


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
#mycur.execute("Use "+u)
mycur.execute("Select * from schedule order by starttime")
tasks = mycur.fetchall();
#print(tasks)
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

#Background
b_img = ImageTk.PhotoImage(Image.open('Images/TimerBG.jpg'))
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
        mycur.execute(f"UPDATE schedule set status = 'i' where task = '{ts_dtb[tskno]}'")
        mycon.commit()
        tskno+=1
        c_task.config(text = 'Current Task: Completing Backlog')
        #if len(tim_dtb) and str(date_dtb[tskno]) == dval+' '+ cval:
            #timer(tim_dtb[tskno])
        return None
    if endT:
        s_no+=1
        Suc_no.config(text = s_no)
        tskno+=1
        c_task.config(text = 'Current Task: On break')
        #if tskno<len(tim_dtb) and str(date_dtb[tskno]) == dval+' '+cval:
        endT = False
            #timer(tim_dtb[tskno])
            
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
def upload():
    os.system("instapost.py")

def end():
    global endT
    endT = True
    success = Label(main,text = 'Nice! Continue Working!',font = ('Courier New',20))
    mycur.execute(f"UPDATE schedule set status = '1' where task = '{ts_dtb[tskno]}'")
    mycon.commit()
    success.place(x = 630,y = 430)

def update():
    os.system('SchedulePage.py')

#REFRESH Function
def ref():
    main.quit()
    os.system("timertest.py")

def moveF(taskno):
    global sta,r_button,l_button,tsk,tsk_no,tot,ts_dtb
    tsk.config(text = ts_dtb[taskno])
    '''
    print(date_dtb[tskno])
    mycur.execute(f"select status from schedule where task = '{ts_dtb[taskno]}' and starttime = '{date_dtb[tskno]}'")
    (ss,) = mycur.fetchone()
    if ss == '0':
        val = 'TO DO'
    elif ss == '1':
        val = 'DONE'
    else:
        val = 'Incomplete'
    sta.config(text = val)
    '''
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
    tsk.config(text = ts_dtb[taskno])
    '''
    mycur.execute(f"select status from schedule where task = '{ts_dtb[taskno]}' and starttime = '{date_dtb[tskno]}'")
    (ss,) = mycur.fetchone()
    if ss == '0':
        val = 'TO DO'
    elif ss == '1':
        val = 'DONE'
    else:
        val = 'Incomplete'
    sta.config(text = val)
    '''

    if taskno == 0:
        l_button = Button(main,text = '<<',font = ('Courier New',20),state = DISABLED)

    else:
        l_button = Button(main,text = '<<',font = ('Courier New',20),command =lambda: moveB(taskno-1))


    r_button = Button(main,text = '>>',font = ('Courier New',20),command = lambda: moveF(taskno+1))
    r_button.place(x = 950,y = 550)
    l_button.place(x = 570,y = 550)
    tsk_no.config(text = 'Task '+str(taskno+1)+' of '+str(tot))


#Buttons
uplink = Button(main,text = 'UPLOAD',font = ('Arial Black',20),command = upload)
uplink.place(x = 100,y = 600)
if not len(tim_dtb):
    End = Button(main,text = 'Finish',font = ('Arial Black',20),state = DISABLED)
    End.place(x = 730,y = 340)
else:

    End = Button(main,text = 'Finish',font = ('Arial Black',20),command = end)
    End.place(x = 730,y = 340)

Update = Button(main,text = 'Schedule',font = ('Arial Black',28),command = update)
Update.place(x = 1350,y = 700)

if not len(tim_dtb):
    r_button = Button(main,text = '>>',font = ('Courier New',20), state = DISABLED)
    r_button.place(x = 950,y = 550)
else:
    
    r_button = Button(main,text = '>>',font = ('Courier New',20),command =lambda: moveF(1))
    r_button.place(x = 950,y = 550)

l_button = Button(main,text = '<<',font = ('Courier New',20),state = DISABLED)
l_button.place(x = 570,y = 550)


photo = PhotoImage(file = r"Images/REFRESH.jpg")

refresh = Button(main,text = '',image = photo,command = ref)
refresh.place(x = 1450,y = 300)


tskno = 0
#Labels
s_no = 0
f_no = 0
Suc_no = Label(main,text = s_no,font = ('Arial Black',36),bg = 'black',fg = 'green')
F_no = Label(main,text = f_no,font = ('Arial Black',36),bg = 'black',fg = 'red')
Suc_no.place(x = 1350,y = 100)
F_no.place(x = 150, y = 100)

if len(tim_dtb):
    v = ts_dtb[tskno]
    a = 'On Break'
    t = str(date_dtb[tskno])
else:
    v = 'No Pending Tasks'
    a = 'No Pending Tasks'
    t = 'NA'

upc = Label(main,text = 'Upcoming Task: '+v,font = ('Arial Black',16))
upc.place(x = 1200,y = 400)

upt = Label(main,text = 'At: '+t,font = ('Arial Black',16))
upt.place(x = 1200,y = 450)

c_task = Label(main,text = 'Current Task: '+a,font = ('Arial Black',16))
c_task.place(x = 600,y = 140)

Tasks = Label(main,text = 'Tasks',font = ('Arial Black', 30))
Tasks.place(x = 725,y = 480)

Fails_T = Label(main,text = 'Fails Today',font = ('Arial Black',30))
Fails_T.place(x = 50,y = 25)

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
'''
if not tot:
    sta = Label(task_frame,text = 'Current Task: None')
    sta.pack()
else:
    if st[0] == '0':
        val = 'TO DO'
    elif st[0] == '1':
        val = 'DONE'
    else:
        val = 'Incomplete'
    sta = Label(task_frame,text = val)
    sta.pack()
'''
#Final task time data
#print(str(date_dtb[-1]))
'''
if (len(tasks)):
    value = str(date_dtb[-1]).split()[1]
    #print(value)

    value = value.split(':')
    value[0] = str(int(value[0])+1)
    v1 = ':'
    v1 = v1.join(value)
else:
    v1 = None
'''
#print(v1)

#Clock
def clock():
    global cval,dval,tskno
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
    if tskno==len(tasks) and len(tasks):
        os.system('instapost.py')
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
date()
clock()

#Function calls
#print(date_dtb[0])
#print('2020-08-02 14:54:00' == str(date_dtb[0]))
main.mainloop()
