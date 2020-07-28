from tkinter import *
from PIL import ImageTk,Image
import time
main = Tk()
main.title('Timer')
main.geometry('1600x800')

#Background
b_img = ImageTk.PhotoImage(Image.open('TimerBG.jpg'))
b_l = Label(main,image = b_img)
b_l.place(x = 0,y = 0)

#Main Timer Function
def timer(number):
    global endT
    if number==-1:
        return None
    if endT:
        return None
    hour = number//3600
    minute = (number%3600)//60
    second = number%60
    if hour<10:
        hour = '0'+str(hour)
    else:
        hour = str(hour)
    if minute<10:
        minute = '0'+str(minute)
    else:
        minute = str(minute)
    if second<10:
        second = '0'+str(second)
    else:
        second = str(second)
    t = hour+ ':' + minute +':' + second
    my_label.config(text = t)
    my_label.after(1000,lambda: timer(number-1))

endT = False


#Functions

def end():
    global endT
    endT = True
    success = Label(main,text = 'Successfully Completed!',font = ('Courier New',20))
    success.place(x = 630,y = 430)

def update():
    return None

def moveF():
    return None

def moveB():
    return None


#Buttons

End = Button(main,text = 'Finish',font = ('Arial Black',20),command = end)
End.place(x = 730,y = 340)

Update = Button(main,text = 'Update Schedule',font = ('Arial Black',28),command = update)
Update.place(x = 1200,y = 700)

r_button = Button(main,text = '>>',font = ('Courier New',20),command = moveF)
r_button.place(x = 920,y = 550)

l_button = Button(main,text = '<<',font = ('Courier New',20),command = moveB)
l_button.place(x = 610,y = 550)

#Labels
Tasks = Label(main,text = 'Tasks',font = ('Arial Black', 30))
Tasks.place(x = 725,y = 480)

Fails_T = Label(main,text = 'Fails Today',font = ('Arial Black',30))
Fails_T.place(x = 50,y = 25)

Success_S = Label(main,text = 'Success Streak',font = ('Arial Black',30))
Success_S.place(x = 1200 ,y = 25)

my_label = Label(main,text = '1',font = ('Helvetica',72),bg='black',fg = 'red')
my_label.place(x = 600,y =210)

quote = Label(main,text = "Everyone has a plan 'till they get punched in the mouth.",font = ('Courier New',20))
quote.place(x = 15,y = 750)

#Function calls
timer(1200)

main.mainloop()

