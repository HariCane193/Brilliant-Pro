from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
import os
import time

main = Tk()
main.title('SETTINGS')
main.geometry('1600x800')
main.resizable(0,0)

#Labels
SETTINGS = Label(main,text = 'SETTINGS',font = ('Arial Black',45))
SETTINGS.place(x = 650,y = 25)
TimerBG= Label(main,text = 'Timer Background',font = ('Arial Black',30))
TimerBG.place(x = 50,y = 200)

ScheduleBG= Label(main,text = 'Schedule Background',font = ('Arial Black',30))
ScheduleBG.place(x = 50,y = 300)

ScheduleST= Label(main,text = 'Schedule START',font = ('Arial Black',30))
ScheduleST.place(x = 50,y = 400)

ScheduleEND= Label(main,text = 'Schedule END',font = ('Arial Black',30))
ScheduleEND.place(x = 50,y = 500)

MaxTasks= Label(main,text = 'Max Tasks/Day',font = ('Arial Black',30))
MaxTasks.place(x = 50,y = 600)

Eff= Label(main,text = 'Efficiency',font = ('Arial Black',30))
Eff.place(x = 50,y = 700)

colon1 = Label(main,text = ':',font = ('Arial Black',30))
colon1.place(x = 675,y = 380)

colon2 = Label(main,text = ':',font = ('Arial Black',30))
colon2.place(x = 675,y = 480)

pct = Label(main,text = '%',font = ('Arial Black',30))
pct.place(x = 700,y = 680)

SAVE = Button(main,text = 'SAVE',font = ('Arial Black',40),state = DISABLED)
SAVE.place(x = 1350,y = 650)

#functions

#def check():
#    print(EFF.get())

#Buttons
BrowseT = Button(main,text = 'BROWSE',font = ('Courier New',20),state = DISABLED)
BrowseT.place(x = 570,y = 210)
BrowseS = Button(main,text = 'BROWSE',font = ('Courier New',20),state = DISABLED)
BrowseS.place(x = 570,y = 300)
#C = Button(main,text = 'Check',font = ('Courier New',20),command = check)
##C.place(x = 900,y = 100)

#combobox1
timeSShr = StringVar()
SShr = ttk.Combobox(main, width = 3, textvariable = timeSShr, font = ('Courier New',20)) 
SShr['values'] = ('00','01','02','03','04','05','06','07','08','09','10',
                '11','12','13','14','15','16','17','18','19','20',
                '21','22','23') 
SShr.current('00')
SShr.place(x = 600,y = 400)

timeSSmin = StringVar()
SSmin = ttk.Combobox(main, width = 3, textvariable = timeSSmin, font = ('Courier New',20)) 
SSmin['values'] = ('00','01','02','03','04','05','06','07','08','09','10',
                '11','12','13','14','15','16','17','18','19','20',
                '21','22','23','24','25','26','27','28','29','30',
                '31','32','33','34','35','36','37','38','39','40',
                '41','42','43','44','45','46','47','48','49','50',
                '51','52','53','54','55','56','57','58','59') 
SSmin.current('00')
SSmin.place(x = 700,y = 400)

#combobox2
timeSEhr = StringVar()
SEhr = ttk.Combobox(main, width = 3, textvariable = timeSEhr, font = ('Courier New',20)) 
SEhr['values'] = ('00','01','02','03','04','05','06','07','08','09','10',
                '11','12','13','14','15','16','17','18','19','20',
                '21','22','23') 
SEhr.current('00')
SEhr.place(x = 600,y = 500)

timeSEmin = StringVar()
SEmin = ttk.Combobox(main, width = 3, textvariable = timeSEmin, font = ('Courier New',20)) 
SEmin['values'] = ('00','01','02','03','04','05','06','07','08','09','10',
                '11','12','13','14','15','16','17','18','19','20',
                '21','22','23','24','25','26','27','28','29','30',
                '31','32','33','34','35','36','37','38','39','40',
                '41','42','43','44','45','46','47','48','49','50',
                '51','52','53','54','55','56','57','58','59') 
SEmin.current('00')
SEmin.place(x = 700,y = 500)

#combobox3
MaxStr = StringVar()
MEF= ttk.Combobox(main, width = 3, textvariable = MaxStr, font = ('Courier New',20)) 
MEF['values'] = ('00','01','02','03','04','05','06','07','08','09','10') 
MEF.current('00')
MEF.place(x = 600,y = 600)

#combobox4
EF = StringVar()
EFF= ttk.Combobox(main, width = 3, textvariable = EF, font = ('Courier New',20)) 
EFF['values'] = ('50','51','52','53','54','55','56','57','58','59','60',
                 '60','61','62','63','64','65','66','67','68','69','70',
                 '70','71','72','73','74','75','76','77','78','79','80',
                 '80','81','82','83','84','85','86','87','88','89','90',
                 '90','91','92','93','94','95','96','97','98','99','100') 
EFF.current('00')
EFF.place(x = 600,y = 700)

main.mainloop()
