#!/usr/bin/env python3
import os
import time
import mysql.connector
import subprocess

time.sleep(1)

#Provjeri je li prazan processlog file
def isitempty(path):
    return os.stat(path).st_size == 0
   
mydb = mysql.connector.connect(
  host="localhost",
  user="bigfella",
  password="G2023m2!!!",
  database="monitoring"
)

#Provjeri je li zatrazen reboot, Start, Stop
mycursor = mydb.cursor()
mycursor.execute("SELECT status FROM sistem WHERE aktivnost='kameramon'")
myresult = mycursor.fetchall()

if ((3,) in myresult):
    print('rebooting system...')
    mycursor = mydb.cursor()
    time.sleep(4)
    mycursor.execute("UPDATE sistem SET status = 1 WHERE aktivnost = 'kameramon'")
    mydb.commit() # Umjesto ovog dodati skriptu na startupu koja setuje status na 1 kad se servisi podignu. (ovo je workaround)
    subprocess.call('/opt/frtsys/monitoring/./rebootme.sh')


elif ((4,) in myresult):
    print('Starting system...')
    mycursor = mydb.cursor()
    mycursor.execute("UPDATE sistem SET status = 1 WHERE aktivnost = 'kameramon'")
    mydb.commit()
    subprocess.call('/opt/frtsys/monitoring/./startme.sh')

elif ((5,) in myresult):
    print('Stopping system...')
    mycursor = mydb.cursor()
    mycursor.execute("UPDATE sistem SET status = 0 WHERE aktivnost = 'kameramon'")
    mydb.commit()
    subprocess.call('/opt/frtsys/monitoring/./stopme.sh')


else:
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

# POKRENUTI CRONJOB svaki minut koji ce da pokrene ps -aux | .... + ovu skriptu koja ce da iscita sadrzaj amialie fajla i na osnovu toga parsuje mysql-u.


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



