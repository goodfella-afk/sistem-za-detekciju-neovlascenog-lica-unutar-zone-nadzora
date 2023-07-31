#!/usr/bin/env python3
import os
import time
import mysql.connector
import subprocess

time.sleep(1)

#check if file has any content inside, use for checking if process is alive.
def isitempty(path):
    return os.stat(path).st_size == 0

# connect to mysql db
mydb = mysql.connector.connect(
  host="localhost",
  user="bigfella",
  password="pass",
  database="monitoring"
)

#check if reboot,start,stop is requested
mycursor = mydb.cursor()
mycursor.execute("SELECT status FROM sistem WHERE aktivnost='kameramon'")
myresult = mycursor.fetchall()

#is reboot requested
if ((3,) in myresult):
    print('rebooting system...')
    mycursor = mydb.cursor()
    time.sleep(4)
    mycursor.execute("UPDATE sistem SET status = 1 WHERE aktivnost = 'kameramon'")
    mydb.commit() #todo- could add startup script that sets status to 1 when process starts
    subprocess.call('/opt/frtsys/monitoring/./rebootme.sh')

#is start requsted
elif ((4,) in myresult):
    print('Starting system...')
    mycursor = mydb.cursor()
    mycursor.execute("UPDATE sistem SET status = 1 WHERE aktivnost = 'kameramon'")
    mydb.commit()
    subprocess.call('/opt/frtsys/monitoring/./startme.sh')

#is stop requested
elif ((5,) in myresult):
    print('Stopping system...')
    mycursor = mydb.cursor()
    mycursor.execute("UPDATE sistem SET status = 0 WHERE aktivnost = 'kameramon'")
    mydb.commit()
    subprocess.call('/opt/frtsys/monitoring/./stopme.sh')


# if there are no requests, then just update current sys status
else:
    #if recognitionlog AND orchlog are active update to 1
    if isitempty("/opt/frtsys/monitoring/recognitionlog") == 0 and isitempty("/opt/frtsys/monitoring/orchlog") == 0 :
        mycursor = mydb.cursor()
        mycursor.execute("UPDATE sistem SET status = 1 WHERE aktivnost = 'kameramon'")
        mydb.commit()
        print("Sistem Funkcionise u potpunosti !")
    else:
        mycursor = mydb.cursor()
        mycursor.execute("UPDATE sistem SET status = 0 WHERE aktivnost = 'kameramon'")
        mydb.commit()
        print ("Sistem/Jedan dio sistema ne funkcionise kako treba, potreban restart !")




#todo - make additional cronjobs and sync   

# Prva iteracija kameratest modula. 

# #Provjeri je li prazan processlog file
# def isitempty(path):
#     return os.stat(path).st_size == 0

# if isitempty("/opt/frtsys/monitoring/recognitionlog") == 0 and isitempty("/opt/frtsys/monitoring/orchlog") == 0 :
#     mycursor = mydb.cursor()
#     mycursor.execute("UPDATE sistem SET status = 1 WHERE aktivnost = 'kameramon'")
#     mydb.commit()
#     print("Sistem Funkcionise u potpunosti !")

# else:
#     mycursor = mydb.cursor()
#     mycursor.execute("UPDATE sistem SET status = 0 WHERE aktivnost = 'kameramon'")
#     mydb.commit()
#     print ("Sistem/Jedan dio sistema ne funkcionise kako treba, potreban restart !")

# # POKRENUTI CRONJOB svaki minut koji ce da pokrene ps -aux | .... + ovu skriptu koja ce da iscita sadrzaj amialie fajla i na osnovu toga parsuje mysql-u.



