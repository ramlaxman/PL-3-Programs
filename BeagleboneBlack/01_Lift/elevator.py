#!/usr/bin/python 
##########################################################
# * Python code for Traffic Signal Simulation using
# * Beaglebone Black running Debian 7 Linux distribution
##########################################################
# * Developed by MicroEmbedded Technologies
##########################################################
 

import sys
import time
import select
from liftpins import *
from gpio import * 


def liftLEDExit (gpio):
	gpioSetVal(gpio, val="0")
	gpioUnexport(gpio)
	return 
	
def liftLEDInit (gpio):
	gpioExport(gpio)
	gpioSetDir(gpio, flag="out")
 	gpioSetVal(gpio, val="0")
 	return
 	
def liftLEDOn (gpio):
	gpioSetVal(gpio, val="1")
	return 
	
def liftLEDOff (gpio):
	gpioSetVal(gpio, val="0")
	return 


def liftButtonExit (gpio):
	gpioUnexport(gpio)
	return 
	
def liftButtonInit (gpio):
	gpioExport(gpio)
	gpioSetDir(gpio, flag="in")
 	gpioSetEdge(gpio, flag="falling")
 	return



def liftInitAll():
	for i in range(0, NO_OF_DIR_LEDS):
		liftLEDInit(str(dir_leds[i]))
			
	for i in range(0, NO_OF_FLOORS):
		liftLEDInit(str(pos_leds[i]))
		liftLEDInit(str(lift_leds[i]))
		liftButtonInit(str(lift_buttons[i]))
	return	



def liftExitAll():
	for i in range(0, NO_OF_DIR_LEDS):
		liftLEDExit(str(dir_leds[i]))
			
	for i in range(0, NO_OF_FLOORS):
		liftLEDExit(str(pos_leds[i]))
		liftLEDExit(str(lift_leds[i]))
		liftButtonExit(str(lift_buttons[i]))
	print "\n=== Demonstration END ===\n"
	return	


def liftDefaultPos():
	liftLEDOn(str(pos_leds[DEFAULT_LIFT_POS]))
	return 



def liftDirUp():
	for i in range(0, NO_OF_DIR_LEDS):
		liftLEDOn(str(dir_leds[i]))
		time.sleep(0.5)
	for i in range(0, NO_OF_DIR_LEDS):
		liftLEDOff(str(dir_leds[i]))
	return



def liftDirDown():
	for i in range(NO_OF_DIR_LEDS, 0, -1):
		liftLEDOn(str(dir_leds[i-1]))
		time.sleep(0.5)
	for i in range(0, NO_OF_DIR_LEDS):
		liftLEDOff(str(dir_leds[i]))
	return



def GetButtonVal(): 
	try:		
		fo0 = open(SYSFS_GPIO_DIR + "/gpio" + str(LIFT_BUTTON_0) + "/value" ,"r")  
		fo0.read(2)
		floor_set[0]["fd"] = fo0
		
		fo1 = open(SYSFS_GPIO_DIR + "/gpio" + str(LIFT_BUTTON_1) + "/value" ,"r")  
		fo1.read(2)
		floor_set[1]["fd"] = fo1
		
		fo2 = open(SYSFS_GPIO_DIR + "/gpio" + str(LIFT_BUTTON_2) + "/value" ,"r")  
		fo2.read(2)
		floor_set[2]["fd"] = fo2
		
		fo3 = open(SYSFS_GPIO_DIR + "/gpio" + str(LIFT_BUTTON_3) + "/value" ,"r")  
		fo3.read(2)
		floor_set[3]["fd"] = fo3
		
		print "\nWaiting for button press ..."
		r, w, ex = select.select([], [], [fo0, fo1, fo2, fo3])
		
		for i in range(len(floor_set)):
			if floor_set[i]["fd"] in ex:
				print "LIFT button is pressed for floor # %d" % i
				liftLEDOn(str(floor_set[i] ["led"]))
				time.sleep(1)
				but = i
				fo = floor_set[i]["fd"]		
				fo.seek(0, 0);
				str1 = fo.read(1)
				#print "Button Pressed ! Value = ", str1
		fo0.close()
		fo1.close()
		fo2.close()
		fo3.close()
		return but
	
	except IOError:
                return


try:
	print "\nLift Operation Simulation using Python\n"
	print  "-----------------------------------------------\n" 	
	liftInitAll()
	liftDefaultPos()

	cur_flr = DEFAULT_LIFT_POS
	
	while True:
		new_flr = GetButtonVal()
		if new_flr > cur_flr:
			tmp = cur_flr
			print "LIFT going UP to floor #%d" %new_flr
			while (tmp != new_flr):
				liftDirUp()
				time.sleep(0.01)
				liftLEDOff(str(pos_leds[tmp]))
				tmp += 1
				liftLEDOn(str(pos_leds[tmp]))
				time.sleep(0.5)
		elif new_flr < cur_flr:
			tmp = cur_flr
			print "LIFT going DOWN to floor #%d" %new_flr
			while (tmp != new_flr):
				liftDirDown()
				time.sleep(0.01)
				liftLEDOff(str(pos_leds[tmp]))
				tmp -= 1
				liftLEDOn(str(pos_leds[tmp]))
				time.sleep(0.5)
		
		cur_flr = new_flr
		liftLEDOff(str(lift_leds[new_flr]))	
		time.sleep(1)
		 
	liftExitAll()
	exit()
except KeyboardInterrupt:
	liftExitAll()	
	print "Program Exit due to CTRL-C"
	exit()
    	sys.exit(0)


