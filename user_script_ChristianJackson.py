"""

Purpose: Calculate the area of a circle.

Author: Christian Jackson

This script illustrates importing modules and using constants.

It illustrates the built-in function round().

When we install Python, it comes with the Python standard library.
Nearly all scripts will import at least one module from the standard library.

We can install additional, third-party modules using pip.
We'll do that later. 

All scripts in this repository use only the standard library.

@uses math module for pi constant

"""
import math  

from util_datafun_logger import setup_logger
logger, logname = setup_logger(__file__)

"""# Use the math module's constant for pi
pi = math.pi

# get the radius from the user - input result is always a string
# Use \n to add a blank new line to the terminal before we ask for input
radius_string = input("\nEnter the radius of a circle: ")

# convert the radius_string to a number
radius = float(radius_string)

# calculate the area using the numeric value (not the string)
area = pi * radius**2

# log the results
logger.info(f"The area of a circle with radius {radius} is {area}.")
logger.info("Eww... that's a lot of decimal places - tmi!")


# round the area to two decimal places
area = round(area, 2)

# log the results
logger.info(f"The area of a circle with radius {radius} is {area}.")
logger.info("Much better!")
"""

#Part 1- Project 1

#Collection of three 3 values
avg_ppg_input1 = input("\nEnter the average points per game of the first NBA Player: ")
avg_ppg_input2 = input("\nEnter the average points per game of the second NBA Player: ")
avg_ppg_input3 = input("\nEnter the average points per game of the third NBA Player: ")

#Conversion of input from a string to an int or a float
avg_ppg1 = float(avg_ppg_input1)
avg_ppg2 = float(avg_ppg_input2)
avg_ppg3 = float(avg_ppg_input3)

#Part 2- Project 1

#Using the three values, print useful (well-labeled) output (use f-strings!)

#Sum
sum = avg_ppg1 + avg_ppg2 + avg_ppg3
print(f"\nThe sum of the three NBA players points per game combined is: {sum:.1f}")

#Average
average = sum/3
print(f"\nThe average points per game of the three NBA Players combined is: {average:.1f}")

#Product
product = avg_ppg1 * avg_ppg2 * avg_ppg3
print(f"\nThe product of the three NBA players points per game combined is: {product:.1f}")

#Smallest
smallest = min(avg_ppg1, avg_ppg2, avg_ppg3)
print(f"\nThe least/smallest amount of average points per game is: {smallest:.1f}")

#Largest
largest = max(avg_ppg1, avg_ppg2, avg_ppg3)
print(f"\nThe most/largest amount of average points per game is: {largest:.1f}")

#Range
print(f"\nThe range of points per game by the NBA players is:  {smallest:.1f} - {largest:.1f}")

# Use built-in open() function to read log file and print it to the terminal
with open(logname, 'r') as file_wrapper:
    print(file_wrapper.read())