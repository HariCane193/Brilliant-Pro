from instabot import Bot
import mysql.connector as ms


d = open('databaseinfo.txt')
z = ''
for i in range(3):
    z+=d.readline()
#x now has host,user,password used for logging into the database
z = z.split()
w = open('usernameinfo.txt')
user = w.readline()
mycon = ms.connect(host = z[0],user = z[1],password = z[2],database = user)
mycur = mycon.cursor()
mycur.execute("Select count(status) from schedule where status = 'i'")
(val,) = mycur.fetchone()
mycur.execute("Select count(task) from schedule")
(tot,) = mycur.fetchone()
if val/tot>0.25:

    f = open('instainfo.txt')
    x = ''
    for i in range(2):
        x+=f.readline()
    #x now has host,user,password used for logging into the database
    x = x.split()
    f.close()

    g = open('photoloc.txt')
    y = g.readline()

    bot = Bot()

    bot.login(username = x[0],password = x[1])
    bot.upload_photo(y,caption = 'I failed at '+val+' tasks today :(')
