import shutil
import time
import os
import numpy as np
import runpy
from emailme import sendmail


# Paths,
imgdir = "/home/bigfella/Desktop/v4/intruder"
Imgsrc = '/home/bigfella/Desktop/v4/intruder/image.jpg'
Vidsrc = '/home/bigfella/Desktop/v4/outputvideo/output.avi'



while True:

#Check if intruder was captured
    checkDir = os.listdir(imgdir)

    if len(os.listdir(imgdir)) != 0:
        time.sleep(1)
        #os.system('python3 /home/bigfella/master/facerecorg/capturetest.py')
        runpy.run_path(path_name='/home/bigfella/Desktop/v4/recordvideo.py')
        #Define Pics Label / timestamp of event
        Imgdst = f'/home/bigfella/Desktop/v4/usbsimulation/{time.strftime("%d_%m_%Y-%H_%M_%S")}.jpg'
        shutil.move(Imgsrc, Imgdst)
        time.sleep(5)
        sendmail(Imgdst)
        time.sleep(1)
        shutil.move(Vidsrc, f'/home/bigfella/Desktop/v4/usbsimulation/{time.strftime("%d_%m_%Y-%H_%M_%S")}.avi' )
        os.system('python3 /home/bigfella/Desktop/v4/recognition.py')
        # could check if image.jpg spawned again and delete for optimal
        
    time.sleep(2)





