from tkinter import *
from PIL import ImageTk,Image
main = Tk()
main.title('Brilliant Pro')
main.geometry('1200x800')

backgroundImage = ImageTk.PhotoImage(Image.open('Images/login.jpg'))
#Remember to check how to get file location of image each time as end user we cant input the file location in the previous line

backgroundlabel = Label(main,image = backgroundImage).place(x = 0,y = 0,relwidth = 1,relheight = 1)


#Adding the username and password entries
Username = Entry(main,width = 50)
Username.insert(0,'Username')
Password = Entry(main,width = 50)
Password.insert(0,'Password')
Username.place(x = 450,y = 355)
Password.place(x = 450,y = 470)

#logging in function
def login():
    #currently empty to be filled in after creating a database.
    return 

#registration function
def register():
    #currently empty to be filled in after creating a database
    return 
#button for login
login1 = Button(main,text = 'LOGIN',command = login).place(x = 550,y = 520)

#register
reg = Button(main,text = 'REGISTER',command = register).place(x = 550,y = 600)

main.mainloop()


