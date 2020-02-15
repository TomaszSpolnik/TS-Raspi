import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(5, GPIO.OUT)

p = GPIO.PWM(5, 100)
p.start(0)
try:
    while 1:
       	for dc in range(0, 21, 5):
            p.ChangeDutyCycle(dc)
            time.sleep(0.1)
        for dc in range(20, -1, -5):
            p.ChangeDutyCycle(dc)
            time.sleep(0.1)

except KeyboardInterrupt:
    pass
p.stop()
GPIO.cleanup()
