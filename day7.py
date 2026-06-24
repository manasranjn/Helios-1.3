# Functions
# Pre-Defined Function

# print() , input() , type() , len()

# User-Defined Function
# def functionName():
#     statements

def sayHello():
    print("Hello everyone")

# sayHello()

# Function without parameter
def addition():
    a = 10
    b = 20
    # print("Addition:", a + b)
    return a + b

# addition()
# addition()
# addition()
# addition()
# print(addition())
# print(addition())
# print(addition())
# print(addition())

# Function with parameter
def add(a,b):
    return a + b

# print(add(10,20))
# print(add(100,120))
# print(add(40,50))
# print(add(10,80))

# Function with default parameter
# print(add(10))

def sum(a=0, b=0):
    print(a)
    print(b)
    return a + b

# print(sum(10,20))
# print(sum(10))
# print(sum(b=100,a=20))

# Inbuilt Modules
# import math
# print(math.pi)
# print(math.sqrt(25))
# print(math.pow(2,3))
# print(math.factorial(5))

# import math as m
# print(m.pi)
# print(m.sqrt(25))
# print(m.pow(2,3))
# print(m.factorial(5))

# from math import pi, sqrt, pow, factorial
# print(pi)
# print(sqrt(25))
# print(pow(2,3))
# print(factorial(5))

# from math import *
# print(pi)
# print(sqrt(25))
# print(pow(2,3))
# print(factorial(5))

# import random as r
# print(r.randint(1,10))
# print(r.random())

# import calendar as c
# print(c.calendar(2026))
# print(c.month(2026,5))