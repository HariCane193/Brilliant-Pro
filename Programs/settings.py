from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from PIL import ImageTk,Image
import os
import time

main = Tk()
main.title('SETTINGS')
main.geometry('800x720')
main.resizable(0,0)


#Labels
SETTINGS = Label(main,text = 'SETTINGS',font = ('Arial Black',45))
SETTINGS.place(x = 260,y = 25)
TimerBG= Label(main,text = 'Timer Background',font = ('Bodoni MT',30))
TimerBG.place(x = 50,y = 150)

ScheduleBG= Label(main,text = 'Schedule Background',font = ('Bodoni MT',30))
ScheduleBG.place(x = 50,y = 230)

ScheduleST= Label(main,text = 'Schedule START',font = ('Bodoni MT',30))
ScheduleST.place(x = 50,y = 310)

ScheduleEND= Label(main,text = 'Schedule END',font = ('Bodoni MT',30))
ScheduleEND.place(x = 50,y = 380)

MaxTasks= Label(main,text = 'Max Tasks/Day',font = ('Bodoni MT',30))
MaxTasks.place(x = 50,y = 450)

Eff= Label(main,text = 'Efficiency',font = ('Bodoni MT',30))
Eff.place(x = 50,y = 520)

colon1 = Label(main,text = ':',font = ('Arial Black',30))
colon1.place(x = 646,y = 295)

colon2 = Label(main,text = ':',font = ('Arial Black',30))
colon2.place(x = 646,y = 360)

pct = Label(main,text = '%',font = ('Arial Black',30))
pct.place(x = 660,y = 510)


#functions

#file
def save():
    f = open('settings.txt','w')
    f.write(timerBG+'\n')  
    f.write(scheduleBG+'\n')  
    f.write(str(SShr.get())+':'+str(SSmin.get())+':00'+'\n')
    f.write(str(SEhr.get())+':'+str(SEmin.get())+':00'+'\n')
    f.write(str(MEF.get())+'\n')
    f.write(str(EFF.get())+'\n')
    f.close()
    messagebox.showinfo('Confirmation','Successfully Saved!')

def browsefunc():
    filename = filedialog.askopenfilename()
    return filename

def tBG():
    global timerBG
    timerBG = browsefunc() 
def sBG():
    global scheduleBG
    scheduleBG = browsefunc()

f = open('settings.txt','r')
a = f.read().split()
try:
    timerBG = a[0]
except:
    timerBG = ''
try:
    scheduleBG = a[1]
except:
    scheduleBG = ''
f.close()

f = open('settings.txt')
BG = f.readlines()
BG = [x[:-1] for x in BG]
f.close()

#Buttons
BrowseT = Button(main,text = 'BROWSE',font = ('Courier New',20),command = tBG,bd = 4)
BrowseT.place(x = 570,y = 150)
BrowseS = Button(main,text = 'BROWSE',font = ('Courier New',20),command = sBG,bd = 4)
BrowseS.place(x = 570,y = 230)
SAVE = Button(main,text = 'SAVE',font = ('Arial Black',35),command = save,bd =4)
SAVE.place(x = 350,y = 600)

#combobox1
timeSShr = StringVar()
SShr = ttk.Combobox(main, width = 3, textvariable = timeSShr, font = ('Courier New',20)) 
SShr['values'] = ('00','01','02','03','04','05','06','07','08','09','10',
                '11','12','13','14','15','16','17','18','19','20',
                '21','22','23') 
SShr.current(BG[2][:2])
SShr.place(x = 571,y = 314)

timeSSmin = StringVar()
SSmin = ttk.Combobox(main, width = 3, textvariable = timeSSmin, font = ('Courier New',20)) 
SSmin['values'] = ('00','01','02','03','04','05','06','07','08','09','10',
                '11','12','13','14','15','16','17','18','19','20',
                '21','22','23','24','25','26','27','28','29','30',
                '31','32','33','34','35','36','37','38','39','40',
                '41','42','43','44','45','46','47','48','49','50',
                '51','52','53','54','55','56','57','58','59') 
SSmin.current(BG[2][3:5])
SSmin.place(x = 671,y = 314)

#combobox2
timeSEhr = StringVar()
SEhr = ttk.Combobox(main, width = 3, textvariable = timeSEhr, font = ('Courier New',20)) 
SEhr['values'] = ('00','01','02','03','04','05','06','07','08','09','10',
                '11','12','13','14','15','16','17','18','19','20',
                '21','22','23') 
SEhr.current(BG[3][:2])
SEhr.place(x = 571,y = 380)

timeSEmin = StringVar()
SEmin = ttk.Combobox(main, width = 3, textvariable = timeSEmin, font = ('Courier New',20)) 
SEmin['values'] = ('00','01','02','03','04','05','06','07','08','09','10',
                '11','12','13','14','15','16','17','18','19','20',
                '21','22','23','24','25','26','27','28','29','30',
                '31','32','33','34','35','36','37','38','39','40',
                '41','42','43','44','45','46','47','48','49','50',
                '51','52','53','54','55','56','57','58','59') 
SEmin.current(BG[3][3:5])
SEmin.place(x = 671,y = 380)

#combobox3
MaxStr = StringVar()
MEF= ttk.Combobox(main, width = 3, textvariable = MaxStr, font = ('Courier New',20)) 
MEF['values'] = (('00','01','02','03','04','05','06','07','08','09','10')+ tuple(str(x) for x in range(11,20)))
MEF.current(BG[4])
MEF.place(x = 571,y = 450)

#combobox4
EF = StringVar()
EFF= ttk.Combobox(main, width = 3, textvariable = EF, font = ('Courier New',20)) 
EFF['values'] = ('50','51','52','53','54','55','56','57','58','59','60',
                 '61','62','63','64','65','66','67','68','69','70',
                 '71','72','73','74','75','76','77','78','79','80',
                 '81','82','83','84','85','86','87','88','89','90',
                 '91','92','93','94','95','96','97','98','99','100') 
EFF.current(f"{str(int(BG[5])-50)}")
EFF.place(x = 571,y = 525)

main.mainloop()
