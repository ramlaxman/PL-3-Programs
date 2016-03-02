##########################################################
# * Python File for Lift Operation Simulation Add-on Card
# * for GPIO PIN Configurations and Other Definitions
##########################################################
# * Developed by MicroEmbedded Technologies
##########################################################

LED_1	=	(0 * 32) + 3		
LED_2	=	(0 * 32) + 23		
LED_3	=	(0 * 32) + 2		
LED_4	=	(0 * 32) + 26		

LED_5	=	(1 * 32) + 17		
LED_6	=	(1 * 32) + 15		
LED_7	=	(0 * 32) + 15		
LED_8	=	(1 * 32) + 14		


LED_9	=	(0 * 32) + 30
LED_10	=	(2 * 32) + 2
LED_11	=	(1 * 32) + 28
LED_12	=	(2 * 32) + 3
LED_13	=	(0 * 32) + 31
LED_14	=	(2 * 32) + 5
LED_15	=	(1 * 32) + 18



SW_1	=	(0 * 32) + 14		
SW_2	=	(0 * 32) + 27		
SW_3	=	(0 * 32) + 22		
SW_4	=	(2 * 32) + 1	




# DIRECTIN LEDS: to represent lift direction (up or down) 
LIFT_DIR_1   =    LED_9
LIFT_DIR_2   =    LED_10
LIFT_DIR_3   =    LED_11
LIFT_DIR_4   =    LED_12
LIFT_DIR_5   =    LED_13
LIFT_DIR_6   =    LED_14
LIFT_DIR_7   =    LED_15


# POSITION LEDS: LEDs to indicate the current position of Lift 
LIFT_POS_0   =    LED_5
LIFT_POS_1   =    LED_6
LIFT_POS_2   =    LED_7
LIFT_POS_3   =    LED_8


# LIFT BUTTONS: corresponding to each floor of the Lift 
LIFT_BUTTON_0   =    SW_1
LIFT_BUTTON_1   =    SW_2
LIFT_BUTTON_2   =    SW_3
LIFT_BUTTON_3   =    SW_4

# LIFT LEDS: indication for BUTTON Press on each floor 
LIFT_LED_0   =    LED_1
LIFT_LED_1   =    LED_2
LIFT_LED_2   =    LED_3
LIFT_LED_3   =    LED_4


# An array of DIRECTIN LEDS 
dir_leds = [ 	LIFT_DIR_1,
		LIFT_DIR_2,
		LIFT_DIR_3,
		LIFT_DIR_4,
		LIFT_DIR_5,
		LIFT_DIR_6,
		LIFT_DIR_7
	   ]	

# An array of POSITION LEDS 
pos_leds = [
		LIFT_POS_0,
		LIFT_POS_1,
		LIFT_POS_2,
		LIFT_POS_3
	   ]

lift_leds = [
		LIFT_LED_0,
		LIFT_LED_1,
		LIFT_LED_2,
		LIFT_LED_3
	   ]


lift_buttons = [
		 LIFT_BUTTON_0,
		 LIFT_BUTTON_1,
		 LIFT_BUTTON_2,
		 LIFT_BUTTON_3
	   ]


NO_OF_FLOORS	  =	4
NO_OF_DIR_LEDS	  =	7
DEFAULT_LIFT_POS =	0


floor_set = [
		{"fd":-1, "button":LIFT_BUTTON_0, "led":LIFT_LED_0},
		{"fd":-1, "button":LIFT_BUTTON_1, "led":LIFT_LED_1},
		{"fd":-1, "button":LIFT_BUTTON_2, "led":LIFT_LED_2},		        
		{"fd":-1, "button":LIFT_BUTTON_3, "led":LIFT_LED_3}	
             ]
