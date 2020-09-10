from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
import mysql.connector as ms
import os
import time

main = Tk()
main.title('Your Schedule')
main.geometry('1600x1000')


#Background
bg_img = ImageTk.PhotoImage(Image.open('Images/ScheduleBG.jpg'))
bg_l = Label(main,image = bg_img)
bg_l.place(x = 0,y = 0)

#Frame

t0 = LabelFrame(main,text = '',width = 100)
t0.place(x = 10,y = 200)

t1 = LabelFrame(main,text = '',width = 100)
t1.place(x = 100,y = 200)

t2 = LabelFrame(main,text = '',width = 100)
t2.place(x = 250,y = 200)

t3 = LabelFrame(main,text = '',width = 100)
t3.place(x = 430,y = 200)

t4 = LabelFrame(main,text = '',width = 100)
t4.place(x = 550,y = 200)

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
st_dtb = []
date_dtb = []
for i in tasks:
    ts_dtb.append(i[0])
    tim_dtb.append(i[1])
    st_dtb.append(i[2])
    date_dtb.append(i[3])

Label(t0,text = 'S.NO',font = ('Arial Black',20)).pack()
Label(t1,text = 'Tasks',font = ('Arial Black',20),width = 7).pack()
Label(t2,text = 'Time Limit',font = ('Arial Black',20)).pack()
Label(t3,text = 'Status',font = ('Arial Black',20)).pack()
Label(t4,text = 'Date & Time',font = ('Arial Black',20)).pack()
if len(tasks)!=0:
    for i in range(len(tasks)):
        Label(t0,text = str(i+1),font = ('Arial Black',20)).pack()
        Label(t1,text = str(ts_dtb[i]),font = ('Arial Black',20)).pack()
        Label(t2,text = str(tim_dtb[i]),font = ('Arial Black',20)).pack()
        if st_dtb[i] == '0':
            val = 'TO DO'
        elif st_dtb[i] == 'i':
            val = 'INC'
        else:
            val = 'DONE'
        Label(t3,text = str(val),font = ('Arial Black',20)).pack()
        Label(t4,text = str(date_dtb[i]),font = ('Arial Black',20)).pack()
#Clear
def clear():
    try:
        named_tuple = time.localtime() # get struct_time
        time_string = time.strftime("%Y-%m-%d %H:%M:%S", named_tuple)
        mycur.execute(f"Select time from schedule where starttime<'{time_string}'")
        (tval,) = mycur.fetchone()
        hour = int(time.strftime("%H",named_tuple))+int(tval[:2])
        minute = int(time.strftime("%M",named_tuple))+int(tval[3:5])
        sec  = int(time.strftime("%S",named_tuple))+int(tval[-2:])
        time_string = time.strftime("%Y-%m-%d", named_tuple)
        print(tval)
        mycur.execute(f"Delete from schedule where starttime < '{time_string} {hour}:{minute}:{sec}' and STATUS = '0'")
        print(time_string)
        mycon.commit()
    except:
        pass
#Alter function
def alter():
    os.system('dtbtask.py')

#insta function
def inst():
    os.system('insta.py')
#clock
def clock():
    c.config(text = time.strftime('%T'))
    c.after(1000,clock)



#heading
S = Label(main,text = 'Upcoming Tasks',font = ('Arial Black',48),fg = 'white',bg = 'black')
S.place(x = 10, y= 10)

#Labels
c = Label(main,text = '',font = ('Arial Black',20),bg = 'white',fg = 'black')
c.place(x = 1400, y = 200)
clock()

#Buttons
al = Button(main,text = 'Alter Schedule',font = ('Arial Black',25),command = alter)
al.place(x = 1200,y = 800)

cl = Button(main,text = 'Clear Schedule',font = ('Arial Black',25),command = clear)
cl.place(x = 1200,y = 600)

inst_info = Button(main,text = 'Instagram Login Information & Image',font = ('Arial Black',20),command = inst)
inst_info.place(x = 40,y = 800)



main.mainloop()