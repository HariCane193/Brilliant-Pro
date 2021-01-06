from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import mysql.connector as ms

main = Tk()
main.title('Register')
main.geometry('600x500')

#Background
b_img = ImageTk.PhotoImage(Image.open('Images/regbg.jpg'))
b_l = Label(main,image = b_img)
b_l.place(x = 0,y = 0)

f = open('databaseinfo.txt')
x = ''
for i in range(3):
    x+=f.readline()
#x now has host,user,password used for logging into the database
x = x.split()

#connecting into the server
try:
    mycon = ms.connect(host = x[0],user = x[1],password = x[2])
    mycur = mycon.cursor()
except:
    messagebox.showerror('Database error','Server connection inactive!')

#Functions

def confirm():
    global main,user,passw
    if C_pass.get()!=Password.get():
        messagebox.showerror('Error',"Passwords don't match")
        return
    res = messagebox.askyesno('Confirmation','Are you sure?')
    if res:
        user = Username.get()
        passw = Password.get()
        mycur.execute('CREATE DATABASE '+user)
        mycur.execute('Use '+user)
        mycur.execute("CREATE table password(pass varchar(30))")
        mycur.execute(f"INSERT INTO password values('{passw}')")
        mycon.commit()
        mycur.execute("CREATE table Schedule(task varchar(40),time varchar(10),STATUS char DEFAULT '0',starttime DATETIME)")
        mycon.commit()
        mycur.execute("CREATE table graphEFF(DATE date,SxEff float)")
        mycon.commit()
        messagebox.showinfo('Confirmation','Successfully Registered')
        main.quit()
    else:
        return


#Entries

Username = Entry(main,width = 50)
Password = Entry(main,show = '*',width = 50)
Username.place(x = 170,y = 200)
Password.place(x = 170,y = 230)

C_pass = Entry(main,show = '*',width = 50)
C_pass.place(x = 170,y = 260)

Username.insert(0,'Username')
Password.insert(0,'Password')
C_pass.insert(0,'Password')

#Buttons

Register = Button(main,text = 'REGISTER',font = ('Arial Black',13),command = confirm)
Register.place(x = 250,y = 320)

#Labels
wel = Label(main,text = "Welcome to Brilliant Pro!",font = ('Freestyle Script',42))
wel.place(x = 130,y = 100)

U = Label(main,text = 'Username: ')
p = Label(main,text = 'Password: ')
c = Label(main,text = 'Confirm Password: ')

U.place(x = 100,y = 197)
p.place(x = 100,y = 227)
c.place(x = 50,y = 260)
main.mainloop()

