#!/usr/bin/python 
##########################################################
# * Python code for Driving a Stepper Motor Card using
# * Beaglebone Black running Debian 7 Linux distribution
##########################################################
# * Developed by MicroEmbedded Technologies
##########################################################
 

import sys
import time
import select
from stepperpins import *
from gpio import * 


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


