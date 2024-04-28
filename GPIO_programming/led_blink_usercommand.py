import RPi.GPIO as GPIO
import time

LED_PIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT) # write info to pin
GPIO.output(LED_PIN, GPIO.HIGH)

state= int(input("Enter 0 to power off , and 1 to power on LED----->: "))
 
 
if state == 0:
        GPIO.output(LED_PIN, GPIO.LOW)
        time.sleep(2)
    
        
elif state == 1:
           
        GPIO.output(LED_PIN, GPIO.HIGH) # set to 3.3
        time.sleep(1)
        
else:
     print('Wron state value: '+ str(value))
     GPIO.cleanup()
     exit()
           
time.sleep(1)
    


