from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import mysql.connector as ms
import time as tt

f = open('databaseinfo.txt')
x = ''
for i in range(3):
    x+=f.readline()
#x now has host,user,password used for logging into the database
x = x.split()

g = open('usernameinfo.txt')

#database connection
mycon = ms.connect(host = x[0],user = x[1],password = x[2],database = g.readline())
mycur = mycon.cursor()

main = Tk()
main.geometry('400x300')
main.title('New Task')
main.resizable(0,0)

year = int(tt.strftime('%Y'))
month = int(tt.strftime('%m'))
day = int(tt.strftime('%d'))

#combobox
stayear = StringVar()
Syear = ttk.Combobox(main, width = 4, textvariable = stayear, font = ('Courier New',8)) 
Syear['values'] = (tuple(str(x) for x in range(year,2080)))
Syear.current('00')
Syear.place(x = 258,y = 83)

t = tt.strftime('%T')
stamonth = StringVar()
Smonth = ttk.Combobox(main, width = 2, textvariable = stamonth, font = ('Courier New',8)) 
Smonth['values'] = ('01','02','03','04','05','06','07','08','09','10','11','12')
Smonth.current(month-1)
Smonth.place(x = 180,y = 83)



staday = StringVar()
Sday = ttk.Combobox(main, width = 2, textvariable = staday, font = ('Courier New',8)) 
Sday['values'] = (('01','02','03','04','05','06','07','08','09')+tuple(str(x) for x in range(10,32)))
Sday.current(day-1)
Sday.place(x = 110,y = 83)


cval = tt.strftime('%T')
hours = int(cval[:2])
mins = int(cval[3:5])
seconds = int(cval[6:8]) 

stahr = StringVar()
Shr = ttk.Combobox(main, width = 2, textvariable = stahr, font = ('Courier New',8)) 
Shr['values'] = (('00','01','02','03','04','05','06','07','08','09')+tuple(str(x) for x in range(10,24)))
Shr.current(hours-1)
Shr.place(x = 110,y = 50)

stamin = StringVar()
Smin = ttk.Combobox(main, width = 2, textvariable = stamin, font = ('Courier New',8)) 
Smin['values'] = (('00','01','02','03','04','05','06','07','08','09')+tuple(str(x) for x in range(10,60)))
Smin.current(mins-1)
Smin.place(x = 170,y = 50)


stasec = StringVar()
Ssec = ttk.Combobox(main, width = 2, textvariable = stasec, font = ('Courier New',8)) 
Ssec['values'] = (('00','01','02','03','04','05','06','07','08','09')+tuple(str(x) for x in range(10,60)))
Ssec.current(seconds-1)
Ssec.place(x = 230,y = 50)


#Entries
task = Entry(main,width = 40)
task.place(x = 110,y = 20)
time = Entry(main,width = 40) 
time.place(x = 110,y = 110)

#Labels
colon1 = Label(main,text = ':',font = ('Helvetica',20)).place(x = 150,y = 38)
colon2 = Label(main,text = ':',font = ('Helvetica',20)).place(x = 210,y = 38)
dash1 = Label(main,text = '-',font = ('Helvetica',20)).place(x = 154,y = 71)
dash2 = Label(main,text = '-',font = ('Helvetica',20)).place(x = 230,y = 71)

task1 = Label(main,text = 'Task name: ')
time1 = Label(main,text = 'Time limit: ')
st1 = Label(main,text = 'Start time: ')
quote = Label(main,text = 'Work towards your dream & Never quit!',font = ('Helvetica',15))

task1.place(x = 10,y = 20)
time1.place(x = 10,y = 110)
st1.place(x = 10, y = 50)
quote.place(x = 10,y = 240)


#Functions
def convtime_to_sec(t):
    return int(t[:2])*3600+int(t[3:5])*60+int(t[6:]) 
def confirm():
    f = open('settings.txt')
    l = f.readlines()
    start = l[2][:-1]
    start = convtime_to_sec(start)
    end = l[3][:-1]
    end = convtime_to_sec(end)
    if (end<start):
        end+=24*3600
    tsk = int(l[4][:-1])
    dval = tt.strftime('%Y')+'-'+tt.strftime('%m')+'-'+tt.strftime('%d')
    mycur.execute(f"Select count(*) from schedule where starttime > '{dval+' '+tt.strftime('%T')}' order by starttime")
    (tskth,) = mycur.fetchone()
    f.close()
    starttime = str(Syear.get())+'-'+str(Smonth.get())+'-'+str(Sday.get())+' '+str(Shr.get())+':'+str(Smin.get())+':'+str(Ssec.get())
    stcheck = str(Shr.get())+':'+str(Smin.get())+':'+str(Ssec.get())
    stcheck = convtime_to_sec(stcheck)
    if  (stcheck>=start and stcheck<=end and tsk>tskth):
        mycur.execute(f"INSERT into schedule(task,time,starttime) values('{task.get()}','{time.get()}','{starttime}')")
        mycon.commit()
        task.insert(0,'')
        time.insert(0,'')
    else:
        messagebox.showwarning(title = 'Error',message = 'Fail to meet User Requirements')
    
def exit():
    main.quit()
#Button
con = Button(main,text = 'CONFIRM',command = confirm)
con.place(x = 150,y = 140)

exit = Button(main,text = 'Exit',command = exit)
exit.place(x = 150,y = 170)
main.mainloop()
