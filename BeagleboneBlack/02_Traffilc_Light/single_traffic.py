#!/usr/bin/python 
##########################################################
# * Python code for Traffic Signal Simulation using
# * Beaglebone Black running Debian 7 Linux distribution
##########################################################
# * Developed by MicroEmbedded Technologies
##########################################################
 
# Import standard python libraries 
import sys
import time


##############################################################
# GPIO Pin definitions for Traffic Light Simulation Board 
# Please refer "MicroEmbedded_BBB_Interfacing Details_New.pdf" 
# for all the PIN details
##############################################################

LED_1	=	(0 * 32) + 3		
LED_2	=	(0 * 32) + 23		
LED_3	=	(0 * 32) + 2		
LED_4	=	(0 * 32) + 26		

LED_5	=	(1 * 32) + 17		
LED_6	=	(1 * 32) + 15		
LED_7	=	(0 * 32) + 15		
LED_8	=	(1 * 32) + 14		

LED_9	=	(0 * 32) + 14		
LED_10	=	(0 * 32) + 27		
LED_11	=	(0 * 32) + 22		
LED_12	=	(2 * 32) + 1	

NORTH_GREEN		=	LED_1
NORTH_YELLOW		=	LED_5
NORTH_RED		=	LED_9

EAST_GREEN		=	LED_2
EAST_YELLOW		=	LED_6
EAST_RED		=	LED_10

SOUTH_GREEN		=	LED_3
SOUTH_YELLOW		=	LED_7
SOUTH_RED		=	LED_11

WEST_GREEN		=	LED_4
WEST_YELLOW		=	LED_8
WEST_RED		=	LED_12

# PATH of a GPIO specific sysfs interfce directory on Linux system 
SYSFS_GPIO_DIR = "/sys/class/gpio"
           	
################################################################################
# Description 	: Write the GPIO PIN value on "/sys/class/gpio/export" file.
# 		 This will export (make visible) the directory associated
#		 with particular GPIO pin under sysfs interface.
#		 e.g. if value of GPIO PIN is "23" then "/sys/class/gpio/gpio23"
#		 directory will be exported (will become visible)
# Input   	: @gpio = Value of GPIO PIN (in the form of string)
# Return	: None
# Note		: Must be called for a particular GPIO PIN before using that PIN.
################################################################################
def gpioExport (gpio): 
	try:
   		fo = open(SYSFS_GPIO_DIR + "/export","w")  
   		fo.write(gpio)
   		fo.close()
   		return
   	except IOError:
                return

#################################################################################
# Description : Exactly opposite of export() function above.
# 		 Write the GPIO PIN value on "/sys/class/gpio/unexport" file.
# 		 This will un-export (make invisible) the directory associated
#		 with particular GPIO pin under sysfs interface.
#		 e.g. if value of GPIO PIN is "23" then "/sys/class/gpio/gpio23"
#		 directory will be unexported (will become invisible)
# Input	: @gpio = Value of GPIO PIN (in the form of string)
# Return	: None
# Note		: Must be called for a particular GPIO PIN after it is used
# 		  This makes a PIN free from GPIO functionality
#################################################################################
def gpioUnexport (gpio):
	try: 
   		fo = open(SYSFS_GPIO_DIR + "/unexport","w")  
   		fo.write(gpio)
   		fo.close()
   		return
   	except IOError:
 		return
             	

################################################################################################
# Description : Write the direction ("in"/"out") on "/sys/class/gpio/gpioN/direction"
#               where "gpioN" stands for the directory already exported.
# 		 This will configure a particular GPIO PIN as an input or output pin.
# Input	: @gpio = Value of GPIO PIN (in the form of string)
# 		  @flag  = Value of direction either "in" or "out"
# Return	: None
# Note		: Make sure to export a GPIO PIN (using gpioExport) before calling this function
#################################################################################################
def gpioSetDir (gpio, flag):
	try: 
	   	fo = open(SYSFS_GPIO_DIR + "/gpio" + gpio + "/direction" ,"w")  
	   	fo.write(flag)
	   	fo.close()
	   	return
 	except IOError:
                return

################################################################################################
# Description  : Write the value ("0"/"1") on "/sys/class/gpio/gpioN/value"
#                where "gpioN" stands for the directory already exported.
# 		  This will make particular GPIO PIN as LOW or HIGH (CLEAR or SET).
# Input   	: @gpio = Value of GPIO PIN (in the form of string)
# 		  @val  = Value of GPIO either "0" or "1"
# Return	: None
# Note		: Make sure to export a GPIO PIN (using gpioExport) and
# 		  set the direction as "out" (using gpioSetDir) before calling this function
#################################################################################################
def gpioSetVal (gpio, val):
	try: 
		fo = open(SYSFS_GPIO_DIR + "/gpio" + gpio + "/value" ,"w")  
		fo.write(val)
		fo.close()
		return
	except IOError:
                return

#################################################################################
# Description  : Function to clean up a particular liftLED
#		  Means Clear the LED and unexport the GPIO PIN
# Input        : @gpio = Value of GPIO PIN (in the form of string)
# Return       : None
# Note	       : This function is called for every LED on lift simulation board
#################################################################################

def lightExit (gpio):
	gpioSetVal(gpio, val="0")
	gpioUnexport(gpio)
	return 

###################################################################################
# Description  : Function to initialize a particular liftLED
#		 Means export the GPIO PIN for LED, Set its direction as "out"
#		 and Clear the LED (Make it "OFF").
#		 Initially we keep all the LEDs in OFF status.
# Input 	: @gpio = Value of GPIO PIN (in the form of string)
# Return	: None
# Note		: This function is called for every liftLED
###################################################################################
	
def lightInit (gpio):
	gpioExport(gpio)
	gpioSetDir(gpio, flag="out")
 	gpioSetVal(gpio, val="0")
 	return

###################################################################################
# Description  : Function to make a particular liftLED ON
#		  Means make the LED "ON", by writing "1" to it's GPIO PIN
# Input  	: @gpio = Value of GPIO PIN (in the form of string)
# Return   	: None
# Note		: Make sure to initialize a particular liftLED using
# 		  liftLEDInit() before calling this function
###################################################################################
 	
def lightOn (gpio):
	gpioSetVal(gpio, val="1")
	return 

###################################################################################
# Description  : Function to make a particular liftLED OFF
#		  Means make the LED "OFF", by writing "0" to it's GPIO PIN
# Input   	: @gpio = Value of GPIO PIN (in the form of string)
# Return	: None
# Note		: Make sure to initialize a particular liftLED using
# 		  liftLEDInit() before calling this function
#####################################################################################
	
def lightOff (gpio):
	gpioSetVal(gpio, val="0")
	return 
	
###################################################################################
# Description  : Initialize all the lift LEDs
#		 Observe that each time liftLEDInit() or liftButtonInit() is called,
#		 LED/BUTTON value is converted from integer number to a string
#		 and then it is passed as a parameter.
# Input       	: None
# Return	: None
# Note		: This function should be called from the main() before starting
# 		  the lift simulation loop
#####################################################################################
	
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


###################################################################################################
# Description  : Cleanup all the lift LEDs and BUTTONs one-by-one.
#		 Observe that each time liftLEDExit() or liftButtonExit is called,
#		 LED/BUTTON is converted from integer number to a string and then
#		 it is passed as a parameter.
# Input	: None
# Return	: None
# Note		: This function can be called,
# 				1) From main() after ending the liftLED simulation loop
# 				2) From signal handler of SIGINT to clean-up and restore the
# 				   LEDs, whenever CTRL+C is pressed (mostly from BBB shell prompt)
###################################################################################################

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

##############################################################
# Description 	: This function simulates the NOETH-SOUTH  
# 		  flow of traffic by turnning the associated  
# 		  LEDs ON or OFF  
# Input		: None 
# Return	: None	 
##############################################################

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

##############################################################
# Description 	: This function simulates the EAST-WEST  
# 		  flow of traffic by turnning the associated  
# 		  LEDs ON or OFF  
# Input		: None 
# Return	: None	 
##############################################################

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
	trafficExitAll()					# Cleanup all the LED GPIOs first
	trafficInitAll()					# Initialize all LEDs and Turn them OFF
	for x in range(0, 10):					# Loop for 10 times
		print "\nNORTH-SOUTH	--> [GO]"		# Prints
		print "EAST-WEST 	--> [STOP]\n"		# Prints
		northSouthOn()					# Call function to make NORTH-SOUTH traffic ON
		time.sleep(1)					# Sleep for 1 second
		print "\nEAST-WEST	--> [GO]"		# Prints
		print "NORTH-SOUTH 	--> [STOP]\n"		# Prints
		eastWestOn()					# Call function to make EAST-WEST traffic ON
		time.sleep(1)					# Sleep for 1 second

	trafficExitAll()					# Cleanup all the LED pins 
	print "done"						# Prints
	exit()							# Exit from Program
except KeyboardInterrupt:					# CTRL-C Exception Handler to cleanup and exit safely from program
	trafficExitAll()	
	print "Program Exit due to CTRL-C"
	exit()
    	sys.exit(0)

