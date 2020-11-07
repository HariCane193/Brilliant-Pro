from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import mysql.connector as ms



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

#combobox
stayear = StringVar()
Syear = ttk.Combobox(main, width = 4, textvariable = stayear, font = ('Courier New',8)) 
Syear['values'] = (tuple(str(x) for x in range(2020,2080)))
Syear.current('00')
Syear.place(x = 258,y = 83)

stamonth = StringVar()
Smonth = ttk.Combobox(main, width = 2, textvariable = stamonth, font = ('Courier New',8)) 
Smonth['values'] = ('01','02','03','04','05','06','07','08','09','10','11','12')
Smonth.current('00')
Smonth.place(x = 180,y = 83)

staday = StringVar()
Sday = ttk.Combobox(main, width = 2, textvariable = staday, font = ('Courier New',8)) 
Sday['values'] = (('01','02','03','04','05','06','07','08','09')+tuple(str(x) for x in range(10,32)))
Sday.current('00')
Sday.place(x = 110,y = 83)

stahr = StringVar()
Shr = ttk.Combobox(main, width = 2, textvariable = stahr, font = ('Courier New',8)) 
Shr['values'] = (('00','01','02','03','04','05','06','07','08','09')+tuple(str(x) for x in range(10,24)))
Shr.current('00')
Shr.place(x = 110,y = 50)

stamin = StringVar()
Smin = ttk.Combobox(main, width = 2, textvariable = stamin, font = ('Courier New',8)) 
Smin['values'] = (('00','01','02','03','04','05','06','07','08','09')+tuple(str(x) for x in range(10,60)))
Smin.current('00')
Smin.place(x = 170,y = 50)


stasec = StringVar()
Ssec = ttk.Combobox(main, width = 2, textvariable = stasec, font = ('Courier New',8)) 
Ssec['values'] = (('00','01','02','03','04','05','06','07','08','09')+tuple(str(x) for x in range(10,60)))
Ssec.current('00')
Ssec.place(x = 230,y = 50)

starttime = str(Syear.get())+'-'+str(Smonth.get())+'-'+str(Sday.get())+' '+str(Shr)+':'+str(Smin)+':'+str(Ssec)
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
def confirm():
    mycur.execute(f"INSERT into schedule(task,time,starttime) values('{task.get()}','{time.get()}','{starttime}')")
    mycon.commit()
    task.insert(0,'')
    time.insert(0,'')
    
def exit():
    main.quit()
#Button
con = Button(main,text = 'CONFIRM',command = confirm)
con.place(x = 150,y = 140)

exit = Button(main,text = 'Exit',command = exit)
exit.place(x = 150,y = 170)
main.mainloop()
