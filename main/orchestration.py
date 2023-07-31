#!/usr/bin/env python3
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
    #If there is something (image.jpg) in intruder dir, trigger following
    if len(checkDir) != 0:
        time.sleep(1)
        #Start recordvideo.py
        runpy.run_path(path_name='/opt/frtsys/main/recordvideo.py')
        #Define Pics Label / timestamp of event occurance 
        Imgdst = f'/opt/frtsys/usbsimulation/{time.strftime("%d_%m_%Y-%H_%M_%S")}.jpg'
        shutil.move(Imgsrc, Imgdst)
        time.sleep(1)
        #Send mail and parse intruder pic with timestamp as arg (attachment))
        sendmail(Imgdst)
        time.sleep(5)
        shutil.move(Vidsrc, f'/opt/frtsys/usbsimulation/{time.strftime("%d_%m_%Y-%H_%M_%S")}.avi' )
        os.system('python3 /opt/frtsys/main/recognition.py')
        # could check if image.jpg spawned again in meanwhile and delete for optimal
        
    time.sleep(2)


# todo -- RUN recognition.py from recordvideo.py after opencv windows crash, (meaning its done recording), and rename and move
# video file from recordvideo.py as well. All that to remove this need for time.sleep as this can create unncessary latency. 




