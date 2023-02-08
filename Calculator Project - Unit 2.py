# Hello! My name is Solianna Gabriel and this is my Python BMI Calculator. The purpose of this code is to tell you whether or not you are at a healthy weight. Below are some useful sources a future programmer might find useful to unerstand my code:
# https://www.w3schools.com/python/python_conditions.asp (how to use conditional statements); https://www.cdc.gov/healthyweight/assessing/bmi/adult_bmi/index.html (greater explanation of BMI)

# Sample Input: weight: 140, height: 66 | Expected Output: Your BMI is 16.78 you are underweight
# Sample Input: weight: 150, height: 68 | Expected Output: Your BMI is 22.8 you are a healthy weight

import math
# First, I imported the math function so that I could preform calulations.
print("This is a Body Mass Index (BMI) Calculator! It will prompt you for yo-ur weight and height, and let you know if you are at a healthy BMI.")
weight = float(input("How much do you weigh in pounds? "))
height = float(input("How tall are you in inches? "))
# I collected the float of the inputs and stored them into weight and height variables.
BMI = 703*(weight/(height**2))
# This is the formula for BMI.
BMI_rounded = round(BMI,2)
print("Your BMI is", float(BMI_rounded))
# I rounded the answer to 2 decimal places.
if float(BMI_rounded)<18.5: print("you are underweight")
if 18.5<=float(BMI_rounded)<=24.9: print("you are at a healthy weight")
if 25.0<=float(BMI_rounded)<=29.9: print("you are overweight")
if float(BMI_rounded)>=30.0: print("you are obese")
# These are conditional statements. You'll get one depending on your BMI (whether it's healthy or not).