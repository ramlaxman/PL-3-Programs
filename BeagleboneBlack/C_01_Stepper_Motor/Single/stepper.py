10#!/usr/bin/python 
##########################################################
# * Python code for Driving a Stepper Motor Card using
# * Beaglebone Black running Debian 7 Linux distribution
##########################################################
# * Developed by MicroEmbedded Technologies
##########################################################
 

import sys
import os
import time


LED_9	=	(0 * 32) + 30		#GPIO0_30
LED_10	=	(2 * 32) + 2		#GPIO2_2
LED_11	=	(1 * 32) + 28		#GPIO1_28
LED_12	=	(2 * 32) + 3		#GPIO2_3


STEPPER_1   =    LED_9
STEPPER_2   =    LED_10
STEPPER_3   =    LED_11
STEPPER_4   =    LED_12


SYSFS_GPIO_DIR = "/sys/class/gpio"


def gpioUnexport (gpio):
	try: 
   		fo = open(SYSFS_GPIO_DIR + "/unexport","w")  
   		fo.write(gpio)
   		fo.close()
   		return
   	except IOError:
 		return
             	

def gpioExport (gpio): 
	try:
   		fo = open(SYSFS_GPIO_DIR + "/export","w")  
   		fo.write(gpio)
   		fo.close()
   		return
   	except IOError:
                return


def gpioSetDir (gpio, flag):
	try: 
	   	fo = open(SYSFS_GPIO_DIR + "/gpio" + gpio + "/direction" ,"w")  
	   	fo.write(flag)
	   	fo.close()
	   	return
 	except IOError:
                return


def gpioSetVal (gpio, val):
	try: 
		fo = open(SYSFS_GPIO_DIR + "/gpio" + gpio + "/value" ,"w")  
		fo.write(val)
		fo.close()
		return
	except IOError:
                return


def stepperExit (gpio):
	gpioSetVal(gpio, val="0")
	gpioUnexport(gpio)
	return 
	
def stepperInit (gpio):
	gpioExport(gpio)
	gpioSetDir(gpio, flag="out")
 	gpioSetVal(gpio, val="0")
 	return
 	
def stepperOn (gpio):
	gpioSetVal(gpio, val="1")
	return 
	
def stepperOff (gpio):
	gpioSetVal(gpio, val="0")
	return 



def stepperInitAll():
	stepperInit(str(STEPPER_1))
	stepperInit(str(STEPPER_2))
	stepperInit(str(STEPPER_3))
	stepperInit(str(STEPPER_4))


def stepperExitAll():
	stepperExit(str(STEPPER_1))
	stepperExit(str(STEPPER_2))
	stepperExit(str(STEPPER_3))
	stepperExit(str(STEPPER_4))
	print "\n=== Demonstration END ===\n"
	return	
	

def stepperSeq5():
	stepperOn(str(STEPPER_1))
	time.sleep(0.0001)
	stepperOff(str(STEPPER_2))
	time.sleep(0.0001)
	stepperOn(str(STEPPER_3))
	time.sleep(0.0001)
	stepperOff(str(STEPPER_4))
	time.sleep(0.0001)
	return 



def stepperSeq9():
	stepperOn(str(STEPPER_1))
	time.sleep(0.0001)
	stepperOff(str(STEPPER_2))
	time.sleep(0.0001)
	stepperOff(str(STEPPER_3))
	time.sleep(0.0001)
	stepperOn(str(STEPPER_4))
	time.sleep(0.0001)
	return 


def stepperSeq10():
	stepperOff(str(STEPPER_1))
	time.sleep(0.0001)
	stepperOn(str(STEPPER_2))
	time.sleep(0.0001)
	stepperOff(str(STEPPER_3))
	time.sleep(0.0001)
	stepperOn(str(STEPPER_4))
	time.sleep(0.0001)
	return 



def stepperSeq6():
	stepperOff(str(STEPPER_1))
	time.sleep(0.0001)
	stepperOn(str(STEPPER_2))
	time.sleep(0.0001)
	stepperOn(str(STEPPER_3))
	time.sleep(0.0001)
	stepperOff(str(STEPPER_4))
	time.sleep(0.0001)
	return 


	
def stepperDirLeft():
	stepperSeq5()
	time.sleep(0.01)
	stepperSeq9()
	time.sleep(0.01)
	stepperSeq10()
	time.sleep(0.01)
	stepperSeq6()
	time.sleep(0.01)
	return



def stepperDirRight():
	stepperSeq6()
	time.sleep(0.01)
	stepperSeq10()
	time.sleep(0.01)
	stepperSeq9()
	time.sleep(0.01)
	stepperSeq5()
	time.sleep(0.01)
	return


try:
	print "\nStepper Motor Driver using Python\n"
	print  "-----------------------------------------------\n" 	
	stepperInitAll()
	while True:
		for i in range(0, 12):
			stepperDirLeft()
		time.sleep(3)
		for i in range(0, 12):
			stepperDirRight()
		time.sleep(3)
		
	stepperExitAll
	exit()
except KeyboardInterrupt:
	stepperExitAll()	
	print "Program Exit due to CTRL-C"
	exit()
    	sys.exit(0)


