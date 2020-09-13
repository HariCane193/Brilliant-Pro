from tkinter import *

main = Tk()
main.geometry('500x300')
main.title('instagram information')


#Entries
username = Entry(main,width = 50)
password = Entry(main,show = '*',width = 50)
userphoto = Entry(main,width = 34)

username.place(x = 103,y = 60)
password.place(x = 103,y = 90)
userphoto.place(x = 200,y = 120)

#Label
Instagram = Label(main,text = 'Instagram Information',font = ('Courier New',28))
Instagram.place(x = 10,y = 10)
user = Label(main,text = 'Username: ',font = ('Arial',10))
pass1 = Label(main,text = 'Password: ',font = ('Arial',10))

p_l = Label(main,text ='Photo Information/Location: ',font = ('Arial',10))


user.place(x = 30,y = 60)
pass1.place(x = 30,y = 90)
p_l.place(x = 30,y = 120)
#function
def confirm():
    f = open('instainfo.txt','w')
    f.write(username.get()+'\n')
    f.write(password.get())
    f.close()
    g = open('photoloc.txt','w')
    g.write(userphoto.get())
    g.close()
    main.quit()

#Button
con = Button(main,text = 'CONFIRM',font = ('Arial Black',20),command = confirm)
con.place(x = 140,y = 150)

main.mainloop()
