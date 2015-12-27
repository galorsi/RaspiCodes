import RPi.GPIO as GPIO
import time

LedPins = [11,12,13,15,16,18,19,21]

def setup():
    GPIO.setmode(GPIO.BOARD)
    for p in LedPins :
        GPIO.setup(p,GPIO.OUT)
        GPIO.output(p, GPIO.HIGH)

def cleanupeverything():
    for p in LedPins:
        GPIO.output(p, GPIO.HIGH)
    GPIO.cleanup()

def running():
    for p in LedPins:
        GPIO.output(p, GPIO.LOW)
        time.sleep(0.1)
        GPIO.output(p, GPIO.HIGH)

def running_on():
    for p in LedPins:
        GPIO.output(p, GPIO.LOW)
        time.sleep(0.1)
    for p in LedPins:
        GPIO.output(p, GPIO.HIGH)
        time.sleep(0.1)
       

def running_two():
    for i in range(len(LedPins)):
        if i == len(LedPins)-1:
            GPIO.output(LedPins[i],GPIO.LOW)
            GPIO.output(LedPins[0],GPIO.LOW)
            GPIO.output(LedPins[i-1],GPIO.HIGH)
        elif i==0:
            GPIO.output(LedPins[i],GPIO.LOW)
            GPIO.output(LedPins[i+1],GPIO.LOW)
            GPIO.output(LedPins[len(LedPins)-1],GPIO.HIGH)
        else:
            GPIO.output(LedPins[i],GPIO.LOW)
            GPIO.output(LedPins[i+1],GPIO.LOW)
            GPIO.output(LedPins[i-1],GPIO.HIGH)
        time.sleep(0.1)
        

def test():
    for i in range(len(LedPins)):
        if i == len(LedPins)-1:
            print 'end'
            print i-1, i, i+1
            print LedPins[i-1],LedPins[i], LedPins[0]
        elif i == 0:
            print 'beginning'
            print i-1, i, i+1
            print LedPins[len(LedPins)-1], LedPins[i], LedPins[i+1]
        else:
            print 'mid'
            print i-1, i, i+1
            print LedPins[i-1], LedPins[i], LedPins[i+1]
        time.sleep(0.5)
        
if __name__=='__main__':
    setup()
    try:
        while True:
            running_two()
            
    except KeyboardInterrupt:
        cleanupeverything()

    except Exception, e:
        cleanupeverything()
        print e.message
