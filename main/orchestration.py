import shutil
import time
import os
import runpy
from emailme import sendmail


# Paths,
imgdir = "/opt/frtsys/intruder"
Imgsrc = '/opt/frtsys/intruder/image.jpg'
Vidsrc = '/opt/frtsys/outputvideo/output.avi'



while True:

#Check if intruder was captured
    checkDir = os.listdir(imgdir)

    if len(os.listdir(imgdir)) != 0:
        #dodaj update status = 4. (intruder detected)
        time.sleep(1)
        #os.system('python3 /home/bigfella/master/facerecorg/capturetest.py')
        runpy.run_path(path_name='/opt/frtsys/main/recordvideo.py')
        #Define Pics Label / timestamp of event
        Imgdst = f'/opt/frtsys/usbsimulation/{time.strftime("%d_%m_%Y-%H_%M_%S")}.jpg'
        shutil.move(Imgsrc, Imgdst)
        time.sleep(5)
        sendmail(Imgdst)
        time.sleep(1)
        shutil.move(Vidsrc, f'/opt/frtsys/usbsimulation/{time.strftime("%d_%m_%Y-%H_%M_%S")}.avi' )
        os.system('python3 /opt/frtsys/main/recognition.py')
        # could check if image.jpg spawned again and delete for optimal
        
    time.sleep(2)





