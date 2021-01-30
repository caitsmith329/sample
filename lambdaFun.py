# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 10:29:19 2020

@author: Cait Smith
"""

#Module 4, Lambda Functions Exercise 1
#Instructions: Write a lambda function, which is assigned to the variable x, 
#that accepts a Boolean value (True or False) and returns an integer 1 if True is 
#passed to the lambda function and 0 if False is passed to the lambda function. 
#That is, your lambda function definition statement should start with 
#x = lambda…

x = lambda i: 1 if i==True else(0 if i==False else 'not Boolean')
print(x(True))
print(x(False))
print(x(19))

# I used the code above to get the proper returns for entries of True or False,
# I added the 'not Boolean' to account for and handle any entries for x()
# outside of 0 or 1. 


#Module 4, Lambda Functions Exercise 2 
# Instructions: Write a lambda function using the variable y that receives a 
# list and returns the type of the first data element (with index 0) in that list. 
# That is, your lambda function definition statement should start with y = lambda…

list1 = [34.5, 67, 78, 103, 45, 97, 13, 88]
#I made the list "l' to serve as the list that variable y recieves and
# uses in the lambda operation
y = lambda k: type(k[0])
print(y(list1))
#The value returned in the console window was float, the item in index position 0 for
# list z was 34.5 so I concur with the return

#Module 4, Lambda Functions Exercise 3
# Instructions: Write a lambda function using the variable z that implements the factorial 
# function in the same fashion as the custom function from a previous knowledge check. 
# As with the custom function, the lambda function will require a recursive structure. 
# Your lambda function definition statement should start with z = lambda…

# Code referenced from "knowledge check is below" for situational awareness:
def fac(num):
    num = int(num)
    if num > 1:
        return num * fac(num - 1)
    else:
        return 1
print(fac(4))
print(fac(1))

#My code to get the same return via lambda is as follows:
import math
z = lambda b: (math.factorial(b)) if b > 1 else 1
print(z(4))
print(z(1))

