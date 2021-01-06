from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
import os
import time
import mysql.connector as ms


main = Tk()
main.title('Brilliant Pro')
main.geometry('1200x800')

#database server connection
f = open('databaseinfo.txt')
x = ''
for i in range(3):
    x+=f.readline()
f.close()
#x now has host,user,password used for logging into the database
x = x.split()
#print(x)
mycon = ms.connect(host = x[0],user = x[1],password = x[2])
mycur = mycon.cursor()
g = open('usernameinfo.txt','w')



backgroundImage = ImageTk.PhotoImage(Image.open('Images/login.jpg'))
#Remember to check how to get file location of image each time as end user we cant input the file location in the previous line

backgroundlabel = Label(main,image = backgroundImage).place(x = 0,y = 0,relwidth = 1,relheight = 1)

#Adding the username and password entries
Username = Entry(main,width = 50)
Username.insert(0,'Username')
Password = Entry(main,show = '*',width = 50)
Password.insert(0,'Password')
Username.place(x = 450,y = 355)
Password.place(x = 450,y = 470)

#clock
def clock():
    l.config(text = time.strftime('%T'))
    l.after(1000,clock)


#logging in function
def login():
    #connecting into the server
    try:
        u = Username.get()
        mycur.execute('Use '+u)
        mycur.execute('SELECT * from password')
        (pass1,) = mycur.fetchone()
        if pass1==Password.get():
            g.write(u)
            g.close()
            we = open('back.txt','w')
            we.write('timertest.py')
            we.close()
            main.destroy()
            os.system('python timertest.py')
            #checked this works
        else:
            messagebox.showerror('Error','Invalid Password')

    except:
        messagebox.showerror('Database error','Invalid Username/Password!')
    
#registration function
def register():
    os.system("python RegisterPage.py")
    return 
#button for login
login1 = Button(main,text = 'LOGIN',command = login).place(x = 550,y = 520)

#register
reg = Button(main,text = 'REGISTER',command = register).place(x = 550,y = 600)

#checking if mysql is active
if os.path.getsize('databaseinfo.txt')==0:
    col = 'red'
    mes = 'INACTIVE'
    xval = 1030
else:
    col = 'green'
    mes = 'ACTIVE'
    xval = 1050

#Labels
dtbst = Label(main,text = mes,fg = col,bg = 'black',font = ('Arial Black',20))
dtbst.place(x = xval,y = 15)

l = Label(main,text = '',bg = 'black',fg = 'white',font = ('Arial Black',20))
l.place(x = 1030,y = 250)
clock()

main.mainloop()


