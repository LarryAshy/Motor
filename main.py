
import RPi.GPIO as GPIO
import sys
import time
GPIO.setmode(GPIO.BCM)


GPIO.setup(4,GPIO.OUT)
GPIO.setup(3,GPIO.OUT)

while True:
    GPIO.output(4, GPIO.LOW)
    GPIO.output(3, GPIO.HIGH)
    time.sleep(0.5)

    GPIO.output(4, GPIO.HIGH)
    GPIO.output(3, GPIO.LOW)
    time.sleep(0.5)
    GPIO.cleanup()

#GPIO.output(4, GPIO.HIGH)
#p=GPIO.PWM(4,50)
#p.start(80)

# # Import required libraries
# import sys
# import time
# import RPi.GPIO as GPIO
#
# # Use BCM GPIO references
# # instead of physical pin numbers
# #GPIO.setmode(GPIO.BCM)
# mode=GPIO.getmode()
# print " mode ="+str(mode)
# GPIO.cleanup()
#
# # Define GPIO signals to use
# # Physical pins 11,15,16,18
# # GPIO17,GPIO22,GPIO23,GPIO24
#
# StepPinForward=16
# StepPinBackward=18
# sleeptime=1
#
# GPIO.setmode(GPIO.BOARD)
# GPIO.setup(StepPinForward, GPIO.OUT)
# GPIO.setup(StepPinBackward, GPIO.OUT)
#
# def forward(x):
#     GPIO.output(StepPinForward, GPIO.HIGH)
#     print "forwarding running  motor "
#     time.sleep(x)
#     GPIO.output(StepPinForward, GPIO.LOW)
#
# def reverse(x):
#     GPIO.output(StepPinBackward, GPIO.HIGH)
#     print "backwarding running motor"
#     time.sleep(x)
#     GPIO.output(StepPinBackward, GPIO.LOW)
#
# print "forward motor "
# forward(5)
# print "reverse motor"
# reverse(5)
#
# print "Stopping motor"
# GPIO.cleanup()