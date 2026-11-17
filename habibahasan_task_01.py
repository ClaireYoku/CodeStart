"""
==============================================================
 BioSkillz CodeStart — Python Foundations | Batch 01
 Task 01: Variables, Data Types, Input, Operators & Typecasting
==============================================================

 Name     : Habiba Hasan

 Save as  : yourname_task_01.py   (example: ali_task_01.py)
 Deadline : Friday, 20 November 2026, 9:00 PM (PKT)
 Submit   : Upload this file to YOUR OWN GitHub repository.

 How to use this file
 --------------------
 1. Write your code below each "# Your code here" line.
 2. Run the file in VS Code and check your output against
    the example output given with each task.
 3. Make sure the whole file runs without errors before
    you upload it.

 Stuck? Share a screenshot of your code and the error in the
 CodeStart discussion group. Mistakes are part of learning.

 Empowering Skills | Lead with Science
"""


# ==============================================================
# PART A: SESSION EXERCISES
#
# The exercise questions are in the Session 01 recording.
# Watch the video, note down Exercises 1, 2 and 3, and solve
# them here.
#
# Session 01 recording (YouTube playlist): https://youtube.com/playlist?list=PLOMPeCDSq-kc&si=uY9I27bFj8yUqc00
# ==============================================================

# --------------------------------------------------------------
# Exercise 1
# --------------------------------------------------------------

print("Exercise 1:")
print(7 / 2)
print(7 // 2)
print("7" + "2")
print(type(7.0))
print(2 + 3 * 4 ** 2)
print(bool("0"))

# --------------------------------------------------------------
# Exercise 2
# --------------------------------------------------------------

#Wrong:
# Name = input("Name: ")
# print("Hello", name) <--variables are case-sensitive, NameError
# Age = input("Age: ") <--In order to +1 to Age, Age must be specified as integer, TypeError
# print("Next year", Age + 1)
# print("done) <--Quotation mark missing, SyntaxError

#Right:
print("Exercise 2:")
Name = input("Name: ")
print("Hello", Name)
Age = int(input("Age: "))
print("Next year", Age + 1)
print("done")

# --------------------------------------------------------------
# Exercise 3
# --------------------------------------------------------------

print("Exercise 3:")
total_bill = int(input("Total bill: "))
print("Total bill: Rs", total_bill)
no_of_friends = int(input("Number of friends: "))
print("Number of friends:", no_of_friends)
print("Each person's share:", total_bill // no_of_friends)
print("Leftover money:", total_bill % no_of_friends) 

# ==============================================================
# PART B: TASKS
# ==============================================================

# --------------------------------------------------------------
# Task 1: Variables and Data Types
#
# Create four variables about yourself:
#   - your name   (string)
#   - your age    (integer)
#   - your height in metres (float)
#   - whether you are a student (boolean)
#
# Print each value along with its data type using type().
# Add at least one comment explaining your code.
#
# Example output:
#   Ali <class 'str'>
#   22 <class 'int'>
#   1.75 <class 'float'>
#   True <class 'bool'>
# --------------------------------------------------------------

print("Task 1:")
Name_task = "Habiba Hasan"
Age_task = int("19")
Height = float("1.62")
Student = bool("True")
print(Name_task, type(Name_task))
print(Age_task, type(Age_task))
print(Height, type(Height))
print(Student, type(Student))

# --------------------------------------------------------------
# Task 2: Temperature Converter (Input and Typecasting)
#
# Ask the user to enter a temperature in Celsius.
# Convert the input to a float, then calculate and print the
# temperature in Fahrenheit and in Kelvin.
#
#   Fahrenheit = (Celsius * 9 / 5) + 32
#   Kelvin     = Celsius + 273.15
#
# Example output:
#   Enter temperature in Celsius: 37
#   Fahrenheit: 98.6
#   Kelvin: 310.15
# --------------------------------------------------------------

print("Task 2:")
temperature = float(input("Temperature in Celsius: "))
print("Temperature in Fahrenheit:", temperature * 9 / 5 + 32)
print("Temperature in Kelvin:", temperature + 273.15)


# --------------------------------------------------------------
# Task 3: Simple Calculator (Arithmetic Operators)
#
# Ask the user to enter two numbers and convert them to floats.
# Print the result of each of these operations:
#   addition, subtraction, multiplication, division,
#   floor division, modulus and exponent (power)
#
# Example output:
#   Enter first number: 17
#   Enter second number: 5
#   Addition: 22.0
#   Subtraction: 12.0
#   Multiplication: 85.0
#   Division: 3.4
#   Floor division: 3.0
#   Modulus: 2.0
#   Power: 1419857.0
# --------------------------------------------------------------

print("Task 3:")
number_1 = int(input("First number: "))
number_2 = int(input("Second number: "))
print("Addition:", number_1 + number_2)
print("Subtraction:", number_1 - number_2)
print("Multiplication:", number_1 * number_2)
print("Division:", number_1 / number_2)
print("Floor division:", number_1 // number_2)
print("Modulus:", number_1 % number_2)
print("Power:", number_1 ** number_2)

# --------------------------------------------------------------
# Task 4: Savings Tracker (Assignment Operators)
#
# Start with a variable: savings = 1000
# Then update it step by step using assignment operators
# (+=, -=, *=), printing the new value after each step:
#   1. You receive 500 as a gift          (use +=)
#   2. You spend 300 on books             (use -=)
#   3. Your savings double by year end    (use *=)
#
# Example output:
#   Starting savings: 1000
#   After gift: 1500
#   After buying books: 1200
#   After doubling: 2400
# --------------------------------------------------------------

print("Task 4:")
Savings = int("1000")
print("Your savings:", Savings)
gift = 500
Savings += gift
print("You recieved a gift of Rs 500! Your savings now:", Savings) 
books = 300
Savings -= books
print("You spent Rs 300 on books. Your savings now:", Savings)
Savings *= 2
print("Your savings by the end of the year have doubled! Your savings:", Savings)

# --------------------------------------------------------------
# Task 5: Scholarship Check (Comparison and Logical Operators)
#
# A student qualifies for a scholarship if:
#   - their marks are 80 or more, AND
#   - their attendance is 75% or more
#
# Ask the user for their marks and attendance (convert both to
# integers). Then print True or False for each check below.
# Do not use if statements; use comparison and logical
# operators only.
#
# Example output:
#   Enter your marks: 85
#   Enter your attendance percentage: 70
#   Marks 80 or more: True
#   Attendance 75% or more: False
#   Qualifies for scholarship: False
# --------------------------------------------------------------

print("Task 5:")
marks = int(input("Your marks: "))
attendance = int(input("Your attendance in %: "))
print("Marks 80 or more:", marks >= 80)
print("Attendance 75 or more:", attendance >= 75)
print("Eligible for scholarship?", marks >= 80 and attendance >= 75)

# ==============================================================
# Before you submit, check that:
#   [ ] Your name is written at the top of this file
#   [ ] The file is saved as yourname_task_01.py
#   [ ] The whole file runs without errors
#   [ ] Your output matches the examples
# ==============================================================
