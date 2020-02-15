import time
import RPi.GPIO as GPIO
from gpiozero import LED
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
led = LED(26)

while True:
    led.on()
    sleep(1)
    led.off()
    sleep(1)
