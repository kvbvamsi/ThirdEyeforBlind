import RPi.GPIO as GPIO
import time 

import cv2

import pyttsx3
 
def speak(text):
    engine = pyttsx3.init()
    engine.rate = 1000
    engine.say(text)
    engine.runAndWait()

#thres = 0.85 # Threshold to detect object

classNames = []
classFile = "/home/vamsi/Desktop/Object_Detection_Files/coco.names"
with open(classFile,"rt") as f:
    classNames = f.read().rstrip("\n").split("\n")

configPath = "/home/vamsi/Desktop/Object_Detection_Files/ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt"
weightsPath = "/home/vamsi/Desktop/Object_Detection_Files/frozen_inference_graph.pb"

net = cv2.dnn_DetectionModel(weightsPath,configPath)
net.setInputSize(320,320)
net.setInputScale(1.0/ 127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)
def getObjects(img, thres, nms, draw=True, objects=[]):
    classIds, confs, bbox = net.detect(img,confThreshold=thres,nmsThreshold=nms)
    #print(classIds,bbox)
    if len(objects) == 0: objects = classNames
    objectInfo =[]
    if len(classIds) != 0:
        for classId, confidence,box in zip(classIds.flatten(),confs.flatten(),bbox):
            className = classNames[classId - 1]
            if className in objects:
                objectInfo.append([box,className])
                if (draw):
                    cv2.rectangle(img,box,color=(0,255,0),thickness=2)
                    cv2.putText(img,classNames[classId-1].upper(),(box[0]+10,box[1]+30),
                    cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
                    cv2.putText(img,str(round(confidence*100,2)),(box[0]+200,box[1]+30),
                    cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
                    #outclass.append(className)

    return img,objectInfo



GPIO.setwarnings(False)
TRIG = int(21)
ECHO = int(20)

servoPIN = int(12)
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

servo = GPIO.PWM(servoPIN, 50) # GPIO 12 for PWM with 50Hz
servo.start(7.5) # Initialization

GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

def zero():
    servo.ChangeDutyCycle(2.5) # 0 Degrees 

def fortyfive():
    servo.ChangeDutyCycle(14.5) # 45 Degree
    
def ninety():
    servo.ChangeDutyCycle(7.5) # 90 Degree

def one():
    #servo.ChangeDutyCycle(12.5) # 180 Degrees
    cap = cv2.VideoCapture(0)
    cap.set(3,640)
    cap.set(4,480)
    #cap.set(10,70)
    success, img = cap.read()
    result, objectInfo = getObjects(img,0.45,0.2, objects=['person'])
    print(objectInfo[0][1])
    speak(objectInfo[0][1])
    cv2.imshow("Output",img)
    cv2.waitKey(1)

 
while True:
    GPIO.output(TRIG, False)
    time.sleep(0.2)
    GPIO.output(TRIG, True)
    time.sleep(0.4)
    GPIO.output(TRIG, False)
    
    StartTime = time.time()
    StopTime = time.time()
 
    while GPIO.input(ECHO) == 0:
        StartTime = time.time()
 
    while GPIO.input(ECHO) == 1:
        StopTime = time.time()

    TimeElapsed = StopTime - StartTime
    distance = (TimeElapsed * 34300) / 2
    distance= int (distance)
    print('distance:',distance)
    x=2.5
    for ill in range(3):
        if(distance <= 100):
            one()
        else:
            x+=5
            servo.ChangeDutyCycle(2.5)
        
    time.sleep(0.1)
 


