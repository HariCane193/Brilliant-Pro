from instabot import Bot
import mysql.connector as ms
import time
from tkinter import messagebox
import os


d = open('databaseinfo.txt')
z = ''
for i in range(3):
    z+=d.readline()
#x now has host,user,password used for logging into the database
z = z.split()
d.close()
w = open('usernameinfo.txt')
user = w.readline()
mycon = ms.connect(host = z[0],user = z[1],password = z[2],database = user)
mycur = mycon.cursor()
dval1 = time.strftime('%Y')+'-'+time.strftime('%m')+'-'+time.strftime('%d')
mycur.execute(f"Select count(status) from schedule where status = '1' and starttime>'{dval1+str(' 00:00:00')}'")
(val,) = mycur.fetchone()
mycur.execute(f"Select count(task) from schedule where starttime>'{dval1+str(' 00:00:00')}'")
(tot,) = mycur.fetchone()
w.close()

try:
    f = open('instainfo.txt')
    x = ''
    for i in range(2):
        x+=f.readline()
    #x now has host,user,password used for logging into the database
    x = x.split()
    f.close()

    g = open('photoloc.txt')
    y = g.readline()
    g.close()
    bot = Bot()
    f = open('settings.txt')
    eff = int(list(f.readlines()[-1].split())[0])/100
    f.close()

    dval1 = time.strftime('%Y')+'-'+time.strftime('%m')+'-'+time.strftime('%d')
    bot.login(username = x[0],password = x[1])
    if tot!=0 and (val/tot)<eff:
        bot.upload_photo(y,caption = f'Failure on {dval1}')
        os.rename(f"{y+str('.REMOVE_ME')}",f"{y}")
except:
    messagebox.showerror('Error','Instagram Setup Incomplete')
    
