import RPi.GPIO as GPIO
import time

PIN_Button = 26
PIN_Led = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_Led, GPIO.OUT)
GPIO.setup(PIN_Button, GPIO.IN)
           
while True:
    if GPIO.input(PIN_Button) == GPIO.HIGH:
        GPIO.output(PIN_Led, GPIO.HIGH)
    
    else:
        GPIO.output(PIN_Led, GPIO.LOW)
print(GPIO.input(PIN_Button))

GPIO.cleanup()
