#Module 1 - Getting Started with Python
#This is our first program

print("Hello World!")

#Module 2 - Working with Data Types

#Working with 4 types of Primitive data Types
  # Interger (Whole Number is positive, negative or zero) Machine start their count with ZERO. 
  # float (a foating-point number or a float is a real number, meaning that it can be either a rational or an irrational number) such as 6.1 or -232.129 (decimal)
  # String
  # Boolean 

#Type command

x = 9.74
print(type(x))

­<Class'float'>

#isinstance command 
  #is a command to determine what we are working with, and determine the type of file we are using.

print(isinstance(4.5, float))   #Should return true
print(isinstance(5, int))       #Should return true
print(isinstance(72, str))      #Should return false

#Concatenation

who = "Christian"
how = "likes"
what = "football"

print(who + how + what)         #Should print, "Christian likes football"
