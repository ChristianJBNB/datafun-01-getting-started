"""

Purpose: Project 1, Writing Scripts to collect discriptive data

Author: Christian Jackson

This is the first project for the class and it focuses on the basics of Python

First we collect 3 values using user input from the terminal

Second we create useful output using the input we collected to determine things such as sum, smallest, etc

Third we create conditional statements that give different responses based on the manpulated data that we recieved
Based on the manipulated data, different responses happen

"""
import math  

from util_datafun_logger import setup_logger
logger, logname = setup_logger(__file__)

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

#Creation of List 
avg_ppg_list = [avg_ppg1,avg_ppg2,avg_ppg3]

#Using the three values, print useful (well-labeled) output (use f-strings!)

#Sum
sum = avg_ppg1 + avg_ppg2 + avg_ppg3
logger.info(f"\nThe sum of the three NBA players points per game combined is: {sum:.1f}")

#Average
average = sum/len(avg_ppg_list)
logger.info(f"\nThe average points per game of the three NBA Players combined is: {average:.1f}")

#Product
product = avg_ppg1 * avg_ppg2 * avg_ppg3
logger.info(f"\nThe product of the three NBA players points per game combined is: {product:.1f}")

#Smallest
smallest = min(avg_ppg1, avg_ppg2, avg_ppg3)
logger.info(f"\nThe least/smallest amount of average points per game is: {smallest:.1f}")

#Largest
largest = max(avg_ppg1, avg_ppg2, avg_ppg3)
logger.info(f"\nThe most/largest amount of average points per game is: {largest:.1f}")

#Range
logger.info(f"\nThe range of points per game by the NBA players is:  {smallest:.1f} - {largest:.1f}")

#Part 3 - Project 1

#Conditional Statements

if smallest < 10:
    logger.info("Averaging less than 5 points a game is pretty bad for the NBA")
elif smallest == 10 :
    logger.info("Averaging exactly 10 points a game is pretty average for the NBA")
else:
    logger.info("Averaging more than 10 points a game is really good for the NBA")

if average >= 20:
    logger.info("Those three NBA players can really score the ball well")
else:
    logger.info("Better luck next time")

if sum < 25:
    logger.info("Thats pretty low, might want to get those numbers up")
else:
    logger.info("Not bad, not bad")

# Use built-in open() function to read log file and print it to the terminal
with open(logname, 'r') as file_wrapper:
    print(file_wrapper.read())