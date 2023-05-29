import mysql.connector
import subprocess

mydb = mysql.connector.connect(
  host="localhost",
  user="bigfella",
  password="G2023m2!!!",
  database="monitoring"
)

#Provjeri da li je reboot zatrazen?

mycursor = mydb.cursor()
mycursor.execute("SELECT status FROM sistem WHERE aktivnost='kameramon'")
myresult = mycursor.fetchall()

if ((3,) in myresult):
    print('rebooting system...')
    subprocess.call('/opt/frtsys/monitoring/./rebootme.sh')


else:
    print("ALL GOOD")


# POKRENUTI CRONJOB svaki minut koji ce da pokrene ps -aux | .... + ovu skriptu koja ce da iscita sadrzaj amialie fajla i na osnovu toga parsuje mysql-u.



