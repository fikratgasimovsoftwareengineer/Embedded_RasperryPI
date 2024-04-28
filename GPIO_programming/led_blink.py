import RPi.GPIO as GPIO
import time

LED_PIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT) # write info to pin





while True:
    GPIO.output(LED_PIN, GPIO.HIGH) # set to 3.3
    time.sleep(1)
    GPIO.output(LED_PIN, GPIO.LOW)
    time.sleep(1)
 
    
    
GPIO.cleanup()
