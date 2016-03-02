#!/usr/bin/python 
##########################################################
# * Python code for Traffic Signal Simulation using
# * Beaglebone Black running Debian 7 Linux distribution
##########################################################
# * Developed by MicroEmbedded Technologies
##########################################################
 
 
import sys
import time
from gpio import * 
from ledpins import *

def lightExit (gpio):
	gpioSetVal(gpio, val="0")
	gpioUnexport(gpio)
	return 
	
def lightInit (gpio):
	gpioExport(gpio)
	gpioSetDir(gpio, flag="out")
 	gpioSetVal(gpio, val="0")
 	return
 	
def lightOn (gpio):
	gpioSetVal(gpio, val="1")
	return 
	
def lightOff (gpio):
	gpioSetVal(gpio, val="0")
	return 
	
	
def trafficInitAll():
	lightInit(str(NORTH_GREEN))
	lightInit(str(NORTH_YELLOW))
	lightInit(str(NORTH_RED))
	lightInit(str(EAST_GREEN))
	lightInit(str(EAST_YELLOW))
	lightInit(str(EAST_RED))
	lightInit(str(SOUTH_GREEN))
	lightInit(str(SOUTH_YELLOW))
	lightInit(str(SOUTH_RED))
	lightInit(str(WEST_GREEN))
	lightInit(str(WEST_YELLOW))
	lightInit(str(WEST_RED))
	return	

def trafficExitAll():
	lightExit(str(NORTH_GREEN))
	lightExit(str(NORTH_YELLOW))
	lightExit(str(NORTH_RED))
	lightExit(str(EAST_GREEN))
	lightExit(str(EAST_YELLOW))
	lightExit(str(EAST_RED))
	lightExit(str(SOUTH_GREEN))
	lightExit(str(SOUTH_YELLOW))
	lightExit(str(SOUTH_RED))
	lightExit(str(WEST_GREEN))
	lightExit(str(WEST_YELLOW))
	lightExit(str(WEST_RED))
	return	

def northSouthOn():
	lightOff(str(EAST_YELLOW))
	lightOff(str(WEST_YELLOW))
	lightOff(str(NORTH_RED))
	lightOff(str(SOUTH_RED))

	lightOn(str(EAST_RED))
	lightOn(str(WEST_RED))

	lightOn(str(NORTH_GREEN))
	lightOn(str(SOUTH_GREEN))

	time.sleep(10)

	lightOff(str(NORTH_GREEN))
	lightOff(str(SOUTH_GREEN))

	lightOn(str(NORTH_YELLOW))
	lightOn(str(SOUTH_YELLOW))
	time.sleep(1)
	return


def eastWestOn():
	lightOff(str(NORTH_YELLOW))
	lightOff(str(SOUTH_YELLOW))
	lightOff(str(EAST_RED))
	lightOff(str(WEST_RED))

	lightOn(str(NORTH_RED))
	lightOn(str(SOUTH_RED))

	lightOn(str(EAST_GREEN))
	lightOn(str(WEST_GREEN))

	time.sleep(10)

	lightOff(str(EAST_GREEN))
	lightOff(str(WEST_GREEN))

	lightOn(str(EAST_YELLOW))
	lightOn(str(WEST_YELLOW))
	time.sleep(1)
	return
	
	
try:		
	print "\nTraffic Signal Light Simulation using Python"
	print "-----------------------------------------------"
	trafficExitAll()
	trafficInitAll()
	for x in range(0, 10):
		print "\nNORTH-SOUTH	--> [GO]"
		print "EAST-WEST 	--> [STOP]\n"
		northSouthOn()
		time.sleep(1)
		print "\nEAST-WEST	--> [GO]"
		print "NORTH-SOUTH 	--> [STOP]\n"
		eastWestOn()
		time.sleep(1)

	trafficExitAll()	
	print "done"
	exit()
except KeyboardInterrupt:
	trafficExitAll()	
	print "Program Exit due to CTRL-C"
	exit()
    	sys.exit(0)

