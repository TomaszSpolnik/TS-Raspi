import time
import RPi.GPIO as GPIO
from gpiozero import Button
button = Button(16)
GPIO.setmode(GPIO.BCM)
while True:
    if button.is_pressed:
        GPIO.setup(18, GPIO.OUT)
    else:
        GPIO.cleanup()

