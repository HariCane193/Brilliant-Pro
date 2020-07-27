from tkinter import *
from PIL import ImageTk,Image
main = Tk()
main.title('Brilliant Pro')
main.geometry('1200x800')

backgroundImage = ImageTk.PhotoImage(Image.open('Images/login.jpg'))
#Remember to check how to get file location of image each time as end user we cant input the file location in the previous line

backgroundlabel = Label(main,image = backgroundImage).place(x = 0,y = 0,relwidth = 1,relheight = 1)

#b_title = ImageTk.PhotoImage(Image.open('Images/title.jpg'))
#b_titlelabel = Label(main,image = b_title).place(x = 450,y = 100)


Username = Entry(main,width = 50)
Username.insert(0,'Username')
Password = Entry(main,width = 50)
Password.insert(0,'Password')
Username.place(x = 450,y = 355)
Password.place(x = 450,y = 470)

main.mainloop()


