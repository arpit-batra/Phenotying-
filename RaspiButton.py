import RPi.GPIO as GPIO
import time
import os


GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)

iname = 1
while True:
    input_state = GPIO.input(18)
    if input_state == False:
            print('Button Automatic  Pressed')
            time.sleep(0.2)
            myname=str(iname)+".jpg"
            os.system("raspistill -t 1000 -o /home/pi/camera/img"+myname)
            os.system("fswebcam /home/pi/camera/usb"+myname)
            time.sleep(4)
            iname+=1

    input_state = GPIO.input(24)
    if input_state == False:
        print('Button click  Pressed')
        time.sleep(0.2)
    input_state = GPIO.input(23)
    if input_state == False:
        print('ClickX....')
        time.sleep(0.2)