# ============================================================
#  BioSkillz CodeStart — Python Foundations | Batch 01
#  TASK 03: Loops (Session 03)
# ============================================================
#
#  Name            : Habiba Hasan
#  GitHub username : ClaireYoku
#  Date            : 24/11/26
#
#  ⚠ BEFORE YOU START
#  Practise the Session 03 examples and the Week 2 Reference
#  Guide first. Try every question yourself before asking for
#  help. Errors are part of learning!
#
#  HOW TO SUBMIT
#  1. Write your code under each question in this file.
#  2. Run the file in VS Code and make sure it works.
#  3. Rename it to:  yourname_task_03.py   (no spaces)
#                    e.g. ali_raza_task_03.py
#  4. Upload it to your GitHub repository.
#  5. Submit your GitHub link as instructed by the team.
#
#  DEADLINE: Friday, 27 November 2026, 9:00 PM (PKT)
#
#  TIP: Code shown inside comments (lines starting with #) does
#  not run. To test it, copy it below and remove the #.
# ============================================================


# ############################################################
#  PART A: SESSION EXERCISES (from the slides)
# ############################################################

# ------------------------------------------------------------
# Exercise 1: Predict the output
# ------------------------------------------------------------
# Write your prediction for each snippet. Then copy the code
# below, run it, and check.
#
# 1)  for i in range(3):
#         print("Hi", i)
#     My prediction: 
#     Hi 1
#     Hi 2
#     Hi 3
#     Real answer: 
#     Hi 0
#     Hi 1
#     Hi 2
#
# 2)  x = 0
#     for i in range(1, 4):
#         x += i * 2
#     print(x)
#     My prediction: 12
#     Actual answer: 12
#
# 3)  for i in range(3, 0, -1):
#         print(i, end="")
#     My prediction: 3 2 1
#     Actual answer: 321  
#
# 4)  for ch in "code":
#         if ch == "d": break
#         print(ch, end="")
#     My prediction: co
#     Actual answer: co
#
# 5)  for i in range(6):
#         if i % 3 == 0: continue
#         print(i, end=" ")
#     My prediction: 1 2 1 2 (remainder values)
#     Actual answer = 1 2 4 5 (i values)
# 
# 6)  for i in range(2, 10, 3):
#         print(i, end=" ")
#     My prediction: 2 5 8
#     Actual answer: 2 5 8

# ------------------------------------------------------------
# Exercise 2: Find and fix 4 bugs
# ------------------------------------------------------------
# This program should print 1 to 5, then the sum of 1 to 5
# (which is 15). It has 4 bugs. Only ONE gives an error
# message; the other three run but behave wrongly.

#     count = 1
#     while count <= 5 <-- missing ":"
#         print(count) <-- runs in an infinite loop of 1 until you tell it to add 1 after every print
#
#     for i in range(1, 5): <-- putting the range at 5 stops the loop at 4
#         total = 0 <-- putting it under ':' makes it so that every time it runs the loop, no 
#                       matter how many times, it is told that the value of total remains 0
#         total += i
#     print("Sum of 1 to 5:", total)

# Write the fixed program below, and add a comment next to
# each fix explaining the bug.

#Corrected:
count = 1
while count <= 5:
    print(count)
    count += 1 

total = 0
for i in range(1, 6):
    total += i
print("Sum of 1 to 5:", total)

# ------------------------------------------------------------
# Exercise 3: Number guessing game
# ------------------------------------------------------------
# Write a game that:
#   1. Picks a secret number from 1 to 10
#   2. Keeps asking for a guess (while loop)
#   3. Says "Too high" or "Too low" (if-elif)
#   4. Stops when the guess is correct (break)
#   5. Prints how many tries it took (counter)
#
# Start with these two lines:
#     import random
#     secret = random.randint(1, 10)
#
# Example:
#   Guess (1-10): 5
#   Too low
#   Guess (1-10): 7
#   Correct! You took 2 tries
#
# Write your code below:

import random
count = 1
secret = random.randint(1, 10)
guess = int(input("Guess (1-10): "))
while guess != secret:
    count += 1
    if guess > secret:
        print(f"Too high")
        guess = int(input("Guess (1-10): "))
    elif guess < secret:
        print(f"Too low")
        guess = int(input("Guess (1-10): "))
print(f"Correct! You took {count} tries.")

# ############################################################
#  PART B: TASKS
# ############################################################

# ------------------------------------------------------------
# Task 1: Multiplication table
# ------------------------------------------------------------
# Ask the user for a number and print its table from 1 to 10.
#
# Example:
#   Enter a number: 7
#   7 x 1 = 7
#   7 x 2 = 14
#   ...
#   7 x 10 = 70
#
# Write your code below:

num = int(input("Enter a number: "))
for t in range(1, 11):
    print(f"{num} x {t} = {num * t}")

# ------------------------------------------------------------
# Task 2: Predict the output
# ------------------------------------------------------------
# Write your prediction first, then run the code to check.
# If your prediction was wrong, write one line explaining why.
#
# 1)  for i in range(1, 4):
#         print(i * i, end=" ")
#     My prediction: 1 4 9
#     Correct: 1 4 9
#
# 2)  total = 0
#     for i in range(0, 10, 3):
#         total += i
#     print(total)
#     My prediction: 18
#     Correct: 18
#
# 3)  n = 3
#     while n > 0:
#         print(n)
#         n -= 1
#     My prediction: 3
#                    2
#                    1
#     Correct: 3
#              2
#              1
#
# 4)  for ch in "loop":
#         if ch == "o":
#             continue
#         print(ch, end="")
#     My prediction: lp
#     Correct: lp
#
# 5)  count = 0
#     for i in range(5):
#         for j in range(2):
#             count += 1
#     print(count)
#     My prediction: 8
#     Correct: 2
#              4
#              6
#              8
#              10
#     Why it was wrong: I supposed the i loop would run four times instead of five, forgot about 0.
#                       Also confused indentations. print aligned with i loop would give 10, 
#                       but within i loop would give the result of each loop
#
# 6)  for i in range(5, 0, -2):
#         print(i, end=" ")
#     My prediction: 5 3 1
#     Correct: 5 3 1
#
# ------------------------------------------------------------
# Task 3: Find and fix the bugs
# ------------------------------------------------------------
# This program should:
#   - print the sum of the even numbers from 1 to 10 (answer: 30)
#   - then count down from 10 to 1
# It has 4 bugs.
#
#     total = 0
#     for i in range(1, 10) <-- (1) missing ":" (2) stop endpoint is not included so it should be kept 11
#         if i % 2 = 0: <-- missing "="
#             total += i
#     print("Sum of even numbers 1-10:", total)
#
#     count = 10
#     while count > 0:
#         print(count) <-- count value remains constant without instruction
#
# Write the fixed program below, and add a comment next to
# each fix explaining the bug.

total = 0
for i in range(1, 11):
    if i % 2 == 0:
        total += i
print("Sum of even numbers 1-10:", total)

count = 10
while count > 0:
    print(count)
    count -= 1

# ------------------------------------------------------------
# Task 4: Character counter
# ------------------------------------------------------------
# Ask the user for a sentence. Using a loop, count and print:
#   - the number of vowels (a, e, i, o, u)
#   - the number of digits
#   - the number of spaces
#
# Example:
#   Sentence: CodeStart has 8 sessions
#   Vowels: 7
#   Digits: 1
#   Spaces: 3
#
# Hint: use .lower(), in, .isdigit() and counter variables.
#
# Write your code below:

sen = input("Sentence: ").lower()
vowels = 0
for vow in sen:
    if vow in "aeiou":
        vowels += 1
print("Vowels:", vowels)
count = 0
for dig in sen:
    if dig.isdigit():
        count += 1
print("Digits:", count)
spaces = sen.count(" ")
print("Spaces:", spaces)

# ------------------------------------------------------------
# Task 5: Your field
# ----------------------------------------------------
# Solve a small problem from YOUR field using a loop.
# Choose ONE option (or create your own):
#
#   Option A: GC content
#     Ask for a DNA sequence (e.g. ATGCGCAT). Count the G and C
#     letters with a loop and print the GC content as a
#     percentage with an f-string.
#     Example: GC content: 50.0%
#
#   Option B: Lab readings
#     Ask how many readings there are (n). Then ask for each
#     reading in a loop and print the average, minimum and
#     maximum.
#
#   Option C: Your own idea
#     Any repeated calculation from your subject. Describe it
#     in a comment first.
#
# Write your code below:

# Option A:
seq = input("DNA sequence: ").upper()
GC = 0
total_n = len(seq)
for gc in seq:
    if gc in "GC":
        GC += 1
print(f"GC content: {GC / total_n * 100}%.")