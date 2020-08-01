from tkinter import *
from PIL import ImageTk,Image
import os
import time
import mysql.connector as ms


#username information
g = open('usernameinfo.txt')
user = g.readline()
#database server connection
f = open('databaseinfo.txt')
x = ''
for i in range(3):
    x+=f.readline()
#x now has host,user,password used for logging into the database
x = x.split()

mycon = ms.connect(host = x[0],user = x[1],password = x[2],database = user)
mycur = mycon.cursor()
mycur.execute("Select * from schedule order by starttime")
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

#Background
b_img = ImageTk.PhotoImage(Image.open('Images/TimerBG.jpg'))
b_l = Label(main,image = b_img)
b_l.place(x = 0,y = 0)

#Main Timer Function
def timer(number):
    global endT,tskno
    if number==-1:
        mycur.execute(f"UPDATE schedule set status = 'i' where task = '{ts_dtb[tskno]}'")
        mycon.commit()
        tskno+=1
        if tskno<len(tim_dtb):
            timer(tim_dtb[tskno])
        return None
    if endT:
        tskno+=1
        if tskno<len(tim_dtb):
            endT = False
            
            timer(tim_dtb[tskno])
            
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

def end():
    global endT
    endT = True
    success = Label(main,text = 'Nice! Continue Working!',font = ('Courier New',20))
    mycur.execute(f"UPDATE schedule set status = '1' where task = '{ts_dtb[tskno]}'")
    mycon.commit()
    success.place(x = 630,y = 430)

def update():
    os.system('SchedulePage.py')


def moveF(taskno):
    tsk.config(text = ts_dtb[taskno])
    mycur.execute(f"select status from schedule where task = '{ts_dtb[taskno]}'")
    (ss,) = mycur.fetchone()
    if ss == '0':
        val = 'TO DO'
    elif ss == '1':
        val = 'DONE'
    else:
        val = 'Incomplete'
    sta.config(text = val)
    if taskno == len(ts_dtb)-1:
        r_button = Button(main,text = '>>',font = ('Courier New',20),state = DISABLED)

    else:
        r_button = Button(main,text = '>>',font = ('Courier New',20),command =lambda: moveF(taskno+1))


    l_button = Button(main,text = '<<',font = ('Courier New',20),command = lambda: moveB(taskno-1))
    r_button.place(x = 950,y = 550)
    l_button.place(x = 570,y = 550)
    tsk_no.config(text = 'Task '+str(taskno+1)+' of '+str(tot))


def moveB(taskno):
    
    tsk.config(text = ts_dtb[taskno])
    mycur.execute(f"select status from schedule where task = '{ts_dtb[taskno]}'")
    (ss,) = mycur.fetchone()
    if ss == '0':
        val = 'TO DO'
    elif ss == '1':
        val = 'DONE'
    else:
        val = 'Incomplete'
    sta.config(text = val)

    if taskno == 0:
        l_button = Button(main,text = '<<',font = ('Courier New',20),state = DISABLED)

    else:
        l_button = Button(main,text = '<<',font = ('Courier New',20),command =lambda: moveB(taskno-1))


    r_button = Button(main,text = '>>',font = ('Courier New',20),command = lambda: moveF(taskno+1))
    r_button.place(x = 950,y = 550)
    l_button.place(x = 570,y = 550)
    tsk_no.config(text = 'Task '+str(taskno+1)+' of '+str(tot))


#Buttons
if not len(tim_dtb):
    End = Button(main,text = 'Finish',font = ('Arial Black',20),state = DISABLED)
    End.place(x = 730,y = 340)
else:

    End = Button(main,text = 'Finish',font = ('Arial Black',20),command = end)
    End.place(x = 730,y = 340)

Update = Button(main,text = 'Update Schedule',font = ('Arial Black',28),command = update)
Update.place(x = 1200,y = 700)

if not len(tim_dtb):
    r_button = Button(main,text = '>>',font = ('Courier New',20), state = DISABLED)
    r_button.place(x = 950,y = 550)
else:
    
    r_button = Button(main,text = '>>',font = ('Courier New',20),command =lambda: moveF(1))
    r_button.place(x = 950,y = 550)

l_button = Button(main,text = '<<',font = ('Courier New',20),state = DISABLED)
l_button.place(x = 570,y = 550)

#Labels
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

#Clock
def clock():
    c.config(text = time.strftime('%T'))
    c.after(1000,clock)

c = Label(main,text = '',font = ('Arial Black',20),bg = 'white',fg = 'black')
c.place(x = 1400, y = 200)
clock()

#Function calls
tskno = 0
if len(tim_dtb):
    timer(tim_dtb[0])

main.mainloop()
