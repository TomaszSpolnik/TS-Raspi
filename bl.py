from gpiozero import LED, Buzzer, Button
buzzer = Buzzer(5)
led = LED(26)
button = Button(16)
while True:
    if button.is_pressed:
        led.on()
        buzzer.on()
    else:
        led.off()
