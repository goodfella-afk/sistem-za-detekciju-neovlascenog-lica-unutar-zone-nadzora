import os
import time
import mysql.connector

time.sleep(1)
    
mydb = mysql.connector.connect(
  host="localhost",
  user="bigfella",
  password="G2023m2!!!",
  database="monitoring"
)

#Provjeri je li prazan processlog file
def isitempty(path):
    return os.stat(path).st_size == 0

if isitempty("/home/bigfella/Desktop/v4/monitoring/recognition") == 0 and isitempty("/home/bigfella/Desktop/v4/monitoring/logalert") == 0 :
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



