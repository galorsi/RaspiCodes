import RPi.GPIO as GPIO
import time

LedPin = 11

GPIO.setmode(GPIO.BOARD)
GPIO.setup(LedPin,GPIO.OUT)
GPIO.output(LedPin, GPIO.HIGH)

try:
    while True:
        print 'led on, status low: '
        GPIO.output(LedPin,GPIO.LOW)
        time.sleep(3)
        print 'led off, status high: '
        GPIO.output(LedPin,GPIO.HIGH)
        time.sleep(3)
except KeyboardInterrupt:
    GPIO.output(LedPin, GPIO.HIGH)
    GPIO.cleanup()
