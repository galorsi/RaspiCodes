#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

SDI   = 11
RCLK  = 12
SRCLK = 13

WhichLeds = [0x01,0x02,0x04,0x08,0x10,0x20,0x40,0x80]

def print_msg():
	print 'Program is running...'
	print 'Please press Ctrl+C to end the program...'

def setup():
	GPIO.setmode(GPIO.BOARD)    # Number GPIOs by its physical location
	GPIO.setup(SDI, GPIO.OUT)
	GPIO.setup(RCLK, GPIO.OUT)
	GPIO.setup(SRCLK, GPIO.OUT)
	GPIO.output(SDI, GPIO.LOW)
	GPIO.output(RCLK, GPIO.LOW)
	GPIO.output(SRCLK, GPIO.LOW)

def hc595_in(dat):
	for bit in range(0, 8):	
		#print 'Bit: '+str(bit)+'  Dat: '+str(dat)+' '+str(bin(dat))+' Shift: '+str(dat<<bit)+' '+str(bin(dat<<bit))+' SDI: '+str(0x80 & (dat << bit))+' '+str(bin(0x80 & (dat << bit)))
		GPIO.output(SDI, 0x80 & (dat << bit))
		GPIO.output(SRCLK, GPIO.HIGH)
		time.sleep(0.001) 
		GPIO.output(SRCLK, GPIO.LOW)

def hc595_out():
	GPIO.output(RCLK, GPIO.HIGH)
	time.sleep(0.001)
	GPIO.output(RCLK, GPIO.LOW)

def loop():
	while True:
		for i in range(0, len(WhichLeds)):
			hc595_in(WhichLeds[i])
			hc595_out()
			time.sleep(0.1)
		
		for i in range(len(WhichLeds)-1, -1, -1):
			hc595_in(WhichLeds[i])
			hc595_out()
			time.sleep(0.1)

def all_off():
	for bit in range(0, 8):	
		#print 'Alloff: ' + str(bit)
		GPIO.output(SDI, 0x0)
		GPIO.output(SRCLK, GPIO.HIGH)
		time.sleep(0.001) 
		GPIO.output(SRCLK, GPIO.LOW)
	hc595_out()

def all_on():
	for bit in range(0, 8):	
		print 'Allon: ' + str(bit)
		GPIO.output(SDI, 0x80)
		GPIO.output(SRCLK, GPIO.HIGH)
		time.sleep(0.001) 
		GPIO.output(SRCLK, GPIO.LOW)
	hc595_out()

def loop2():
        all_on()
        time.sleep(3)
        all_off()
        time.sleep(3)

def destroy():   # When program ending, the function is executed. 
	all_off()
	GPIO.cleanup()

if __name__ == '__main__': # Program starting from here 
	print_msg()
	setup() 
	try:
		loop()  
	except KeyboardInterrupt:  
		destroy()  
