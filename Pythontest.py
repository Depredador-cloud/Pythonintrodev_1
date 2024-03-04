#Module 1 - Getting Started with Python
#This is our first program

print("Hello World!")

#Module 2 - Working with Data Types

#Working with 4 types of Primitive data Types
# Interger (Whole Number is positive, negative or zero) Machine start their count with ZERO. 
# float 
# String
# Boolean 

#Type command

x = 9.74
print(type(x))

­<Class'float'>

#isinstance command

print(isinstance(4.5, float))   #Should return true
print(isinstance(5, int))       #Should return true
print(isinstance(72, str))      #Should return false

#Concatenation

who = "David"
how = "likes"
what = "football"

print(who + how + what)         #Should print, "David likes football"
