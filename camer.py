from picamera import PiCamera
from time import sleep
camera = PiCamera()
camera.start_preview()
sleep(5)
camera.stop_preview()

'''
import RPi.GPIO as GPIO
import time
TRIG=21
ECHO=20
GPIO.setmode(GPIO.BCM)
#GPIO.setmode(GPIO.BOARD)
print("distance measurement in progress")
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
GPIO.output(TRIG,False)
print("waiting for sensor to settle")

GPIO.setup(11,GPIO.OUT)
servo1 = GPIO.PWM(11,50) 

servo1.start(0)
print ("Welocome")
time.sleep(2)

print ("Scaning 180* degrees")

# Define variable duty

duty = 2

# Loop for duty values from 2 to 12 (0 to 180 degrees)
while duty <= 11:
    servo1.ChangeDutyCycle(duty)
    #GPIO.output(TRIG,True)
    time.sleep(0.00001)
    GPIO.output(TRIG,False)
    while GPIO.input(ECHO)==0:
        pulse_start=time.time()
    while GPIO.input(ECHO)==1:
        pulse_end=time.time()
    pulse_duration=pulse_end-pulse_start
    distance=pulse_duration*17150
    distance=round(distance,2)
    if(distance > 100):
        # object detected
        print("distance:",distance)
    time.sleep(1)
    duty = duty + 3

servo1.ChangeDutyCycle(8)
time.sleep(2)

#servo1.ChangeDutyCycle(2)
time.sleep(2)
servo1.ChangeDutyCycle(0)

#Clean things up at the end
servo1.stop()
GPIO.cleanup()
print ("Goodbye")'''






'''# Code for audio player

import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty("voices")
text = "Python is a great programming language"
engine.setProperty("rate", 150)
engine.setProperty("voice", voices[1].id)
engine.say(text)
#  engine.save_to_file(text, "python.mp3")
engine.runAndWait()
'''