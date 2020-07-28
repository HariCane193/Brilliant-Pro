from tkinter import *
import time
main = Tk()
main.title('Timer')
main.geometry('260x100')

def timer(number):
    if number==-1:
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

my_label = Label(main,text = '1',font = ('Helvetica',48),bg='black',fg = 'red')
my_label.pack(pady=20)
timer(1200)

main.mainloop()

