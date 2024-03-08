"""""                                           Python Program to Check if a Number is Odd or Even

Problem Description
Write a Python Program to check whether a given number is even or odd.

What is an Even Number?
An even number is an integer that is divisible by 2 without leaving a remainder, such as 2, 4, 6, 8, 10, and so on.

What is an Odd Number?
An odd number is an integer that cannot be divided evenly by 2, leaving a remainder of 1. Examples include 1, 3, 5, 7, 9, and so on.

Problem Solution
There are several ways to check whether a given number is even or odd in Python. Let’s take a detailed look at all the approaches to check whether a given number is even or odd.

Check Even or Odd in Python using if-else and Modulus Operator
Check Even or Odd in Python using Bitwise Operator
Check Even or Odd in Python using Recursion
Check Even or Odd in Python using Lambda Function

"""


# Method 1: (Using if-else and Modulus Operator)
# In this approach, we check whether a number is even or odd using if-else statement and modulus operator.

# Program/Source Code
# Here is source code of the Python Program to determine whether a given number is even or odd using modulus operator
# . The program output is also shown below.
n = int(input("Enter a number "))
if(n%2==0):
    print(n,"number is an even")
else:
    print(n,"number is an odd")    



# Method 2: (Using Bitwise Operator)
# In this approach, we check whether a number is even or odd using bitwise operator.

# Program/Source Code
# Here is source code of the Python Program to determine whether a given number is even or odd using bitwise operator. The program output is also shown below.
n = int(input("Enter a number: "))
if n & 1:
    print(n, "is an odd number.")
else:
    print(n, "is an even number.")