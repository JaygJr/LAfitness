# Include the library functions to use LEDs.
from gpiozero import LED
from time import sleep

# Establish a pin connection for 3 LEDs (red 17, yellow 27, green 22 
#                                        and blue 23)
# Note the numbers above come from pinout.xyz for 4 BCM pins
# used for LEDs.
red_led = LED(17)       # Red LED used for Obese category
yellow_led = LED(27)    # Yellow LED used for Overweight category 
green_led = LED(22)     # Green LED used for Normal BMI category
blue_led = LED(23)      # Blue LED used for Underweight category

# Display welcome message for user.
print()
print("Welcome To The Python-based BMI calculator. ")
print()

# Get weight from user.
lbs = int(input("Enter your weight in lbs as a whole number: "))

# Convert weight from lbs to kg.
# kg = lbs * 0.4536    (approximately)
kg = lbs*0.4536

# Get height in inches from user (this will be changed to feet and inches once it works for inches alone).
inches = int(input("Enter your height in inches as a whole number: "))

# Convert height from inches to meters.
meters = inches / 39.37

# print("lbs= " + str(lbs) + "  kg= " + str(kg) + " inches= " + str(inches) + " meters= " + str(meters))

# Compute BMI.
# Formula is: BMI = Weight (kg) / (Height (m))2
bmi = (kg / (meters**2))

# Display result to user.
# For the LED lights:
#   Underweight and Obese should light the RED LED.
#   Overweight should light the YELLOW LED.
#   Normal weight should light the GREEN LED.
print()
print ("Your BMI = %4.2f" %(bmi) + " kg/m2")
print()

# If bmi < 18.5
if bmi < 18.5:
    print ("Underweight")
    blue_led.on()
    sleep(5)

#elIf  bmi >= 18.5 and bmi < 25
elif  bmi >= 18.5 and bmi < 25:
    print ("Normal")
    green_led.on()
    sleep(5) 

# If bmi >= 25 and bmi < 30
elif bmi >= 25 and bmi < 30:
    print ("Overweight")
    yellow_led.on()
    sleep(5)

# If bmi >=30 
if bmi >= 30:
    print ("Obese")
    red_led.on()
    sleep(5)


