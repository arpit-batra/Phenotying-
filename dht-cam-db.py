import sys
import Adafruit_DHT
import dropbox
from time import sleep
import picamera
from datetime import datetime
import os
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

os.environ["HPPT_PROXY"]="http://10.8.0.1:8080"
os.environ["HPPTS_PROXY"]="https://10.8.0.1:8080"

GPIO.setup(18, GPIO.OUT)

dbx=dropbox.Dropbox('RHHiVbcV6NAAAAAAAAAAEn6uPPADYdJx__BlDNgUSD9-4FyTAqzM1sFgnIvm8OpM')
filePath= "/home/pi/timestamped_pics3/New/"

while True:
    currentTime=datetime.now()
    picTime=currentTime.strftime("%d.%m.%Y-%H.%M:%S")
    picName= picTime+'.jpg'
    completeFilePath= filePath +picName
    dataName=picTime+'.txt'

    with picamera.PiCamera() as camera:
        camera.resolution=(2592,1944)
        camera.rotation= 180
        
        GPIO.output(18,GPIO.HIGH)
        camera.start_preview()
        sleep(2)
        camera.capture(completeFilePath)
        camera.stop_preview()
        print("pic taken")
        GPIO.output(18,GPIO.LOW)
        #sleep(5)
    try:
        with open(completeFilePath, "r") as f:
            dbx.files_upload(f.read(), '/pi2/'+picName, mute = True)
            print("Picuploaded")
        f.close()
    except:
        print("Error in uploading")


    #humidity, temperature = Adafruit_DHT.read_retry(22, 4)

    #print ("Temp1: {0:0.1f} C  Humidity1: {1:0.1f} %".format(temperature, humidity))
    #with open(filePath+"/Newdata.txt","a") as k:
    #    k.write("\n"+str(picTime)+"\t"+str(temperature)+" , "+str(humidity))
    #k.close()

    #try:
    #    with open(filePath+"/Newdata.txt","rb") as k:
    #        dbx.files_upload(k.read(), '/pi2/'+dataName, mute = True)
    #        print("Datauploaded")
    #    k.close()
    #except:
    #    print("Error in uploading")

    sleep(900)
