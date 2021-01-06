from tkinter import *
from tkinter import messagebox
main = Tk()
main.title('Sql Connection')
main.geometry('400x300')

#You need 4 things to establish a database connection
#hostname,user,password,databasename
#but we only need hostname user and password from user as we can create the database later when the user registers
f = open('databaseinfo.txt','w')

#Functions
def enter():
    h1 = host.get()
    u1 = user.get()
    p1 = password.get()

    if len(h1)==0 or len(u1)==0 or len(p1) == 0:
        messagebox.showerror('Incomplete','Incomplete Form')
        return
    f.write(h1+'\n')
    f.write(u1+'\n')
    f.write(p1+'\n')
    f.close()
    main.quit()

#Entries

host = Entry(main,width = 40)
user = Entry(main,width = 40)
password = Entry(main,width = 40)

#host.insert(0,'localhost')
#user.insert(0,'root')
#password.insert(0,'password')

host.place(x = 130,y = 70)
user.place(x = 130,y = 110)
password.place(x = 130,y = 150)


#Labels
h = Label(main,text = 'host:',font = ('Arial Black',13))
u = Label(main,text = 'user:',font = ('Arial Black',13))
p = Label(main,text = 'password:',font = ('Arial Black',13))

h.place(x = 60,y = 63)
u.place(x = 60,y = 103)
p.place(x = 25,y = 143)

db = Label(main,text = 'Database Information',font = ('Courier New',24))
db.place(x = 10,y = 20)

#Buttons
con = Button(main,text = 'Confirm',font = ('Courier New',30),command = enter)
con.place(x = 100,y = 200)

main.mainloop()

#Test
'''
f = open('databaseinfo.txt')
x = ''
for i in range(3):
    x+=f.readline()
x = x.split()
print(x)
'''
