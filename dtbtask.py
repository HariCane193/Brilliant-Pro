from tkinter import *
from tkinter import messagebox
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


#Entries
task = Entry(main,width = 40)
time = Entry(main,width = 40) 
st = Entry(main,width = 40)

task.place(x = 110,y = 20)
time.place(x = 110,y = 50)
st.place(x = 110,y = 80)

#Labels
task1 = Label(main,text = 'Task name: ')
time1 = Label(main,text = 'Time limit: ')
st1 = Label(main,text = 'Start time: ')

task1.place(x = 10,y = 20)
time1.place(x = 10,y = 50)
st1.place(x = 10, y = 80)


#Functions
def confirm():
    mycur.execute(f"INSERT into schedule(task,time,starttime) values('{task.get()}','{time.get()}','{st.get()}')")
    mycon.commit()
    task.insert(0,'')
    time.insert(0,'')
    st.insert(0,'')
    
def exit():
    main.quit()
#Button
con = Button(main,text = 'CONFIRM',command = confirm)
con.place(x = 150,y = 120)

exit = Button(main,text = 'Exit',command = exit)
exit.place(x = 150,y = 150)
main.mainloop()
