from instabot import Bot
import mysql.connector as ms
import time
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
mycur.execute("Select count(status) from schedule where status = 'i'")
(val,) = mycur.fetchone()
mycur.execute("Select count(task) from schedule")
(tot,) = mycur.fetchone()
w.close()

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
if (True):
    bot.upload_photo(y,caption = f'Test on 23-11-2020')
elif tot!=0 and val/tot<eff:
    bot.upload_photo(y,caption = f'Failure on {dval1}')
os.rename(f'{y}',f'{y[:-10]}')
