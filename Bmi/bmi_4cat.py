#!/usr/bin/env python3
# Include the library functions to use LEDs.
from time import sleep
from gpiozero import LED

# ToDo: fix issue with bad input - if anything is other than positive integers.
# ToDo: the calculation of the BMI should be done as a function
# ToDo: Change individual LEDs to  RGB LED
# ToDo: Confirm the "Out of Scope" error from pylint is a PEP8 error

# Function convert_lbs_to_kg uses standard conversion factor to take input as lbs and return value in kg.
def convert_lbs_to_kg(lbs):
    return lbs*0.4536

# Function convert_inches_to_meters uses standard conversion factor to take input as inches and return value in meters.
def convert_inches_to_meters(inches):
    return inches/39.37

# Function calculate_bmi uses standard formula to return bmi value from input values of kg and meters.
def calculate_bmi(kg, meters):
    return kg / (meters**2)

# Function get_int_from_user returns an entered value as integer and it should assign that value to
# a variable corresponding to the prompt that is passed as an argument.
def get_int_from_user(prompt):
    return int(input(prompt))

# Function display_message will display the message passed as an argument followed by a blank line.
def display_message(message):
    print(message)
    return 1

# Establish a pin connection for 3 LEDs (red 17, yellow 27, green 22
#                                        and blue 23)
# Note the numbers above come from pinout.xyz for 4 BCM pins
# used for LEDs.
red_led = LED(17)       # Red LED used for Obese category
yellow_led = LED(27)    # Yellow LED used for Overweight category
green_led = LED(22)     # Green LED used for Normal BMI category
blue_led = LED(23)      # Blue LED used for Underweight category

# Display welcome message for user.
display_message("Welcome To The Python-based BMI calculator. \n")

# Get weight from user.
lbs = get_int_from_user("Enter your weight in lbs as a whole number: ")

# Convert weight from lbs to kg.
# kg = lbs * 0.4536    (approximately)
kg = convert_lbs_to_kg(lbs)

# Get height in inches from user (will get converted later).
inches = get_int_from_user("Enter your height in inches as a whole number: ")

# Convert height from inches to meters.
meters = convert_inches_to_meters(inches)

bmi = calculate_bmi(kg, meters)

# Display result to user.
# For the LED lights:
#   Underweight and Obese should light the RED LED.
#   Overweight should light the YELLOW LED.
#   Normal weight should light the GREEN LED.
display_message(("\nYour BMI = %4.2f" %(bmi) + " kg/m2\n"))

# If bmi < 18.5
if bmi < 18.5:
    display_message("Underweight")
    blue_led.on()
    sleep(5)

#elIf  bmi >= 18.5 and bmi < 25
elif  bmi >= 18.5 and bmi < 25:
    print("Normal")
    green_led.on()
    sleep(5)

# If bmi >= 25 and bmi < 30
elif bmi >= 25 and bmi < 30:
    print("Overweight")
    yellow_led.on()
    sleep(5)

# If bmi >=30
if bmi >= 30:
    print("Obese")
    red_led.on()
    sleep(5)
