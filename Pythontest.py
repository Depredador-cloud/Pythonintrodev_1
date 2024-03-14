#Module 1 - Getting Started with Python
#This is our first program

print("Hello World!")

#Module 2 - Working with Data Types

#Working with 4 types of Primitive data Types
  # Interger (Whole Number is positive, negative or zero) Machine start their count with ZERO. 
  # float (a foating-point number or a float is a real number, meaning that it can be either a rational or an irrational number) such as 6.1 or -232.129 (decimal)
  # String a set of characters grouped together "Hello World", "greetings" or "Welcome to github".
  # Boolean a true or false value


Tipos de datos básicos en Python:
Numéricos:

Enteros (int): Números sin decimales, como 5, 100 o -2. Son usados para contar o para representar valores discretos.
De punto flotante (float): Números con decimales, como 3.14, 9.81 o -0.5. Son usados para representar valores con precisión decimal.
Complejos (complex): Números que incluyen una parte real y una parte imaginaria, como 1+2j o 3-4j. Son usados para operaciones matemáticas avanzadas.
Cadenas (str): Secuencias de caracteres, como "Hola mundo", "Python" o "¡Hola!". Se usan para representar texto.

Booleanos (bool): Valores que solo pueden ser True o False. Se usan para representar valores lógicos.

Ejemplos:

Python
# Entero
numero_entero = 10

# De punto flotante
numero_decimal = 3.1415

# Complejo
numero_complejo = 1 + 2j

# Cadena
texto = "Hola mundo"

# Booleano
verdadero = True
falso = False

#Type command

x = 9.74
print(type(x))

­<Class'float'>

#isinstance command 
  #is a command to determine what we are working with, and determine the type of file we are using.

print(isinstance(4.5, float))   #Should return true
print(isinstance(5, int))       #Should return true
print(isinstance(72, str))      #Should return false

Num = 53
print(num)
53
print(float(num))
53.0

  
#Concatenation

who = "Christian"
how = "likes"
what = "football"

print(who + how + what)         #Should print, "Christian likes football"

#Module 3 - Multiple Assignment Operators

x, y, z = 10, 20, 30
print(x)
print(y)
print(z)

#using a For Loop with Multiple Assignment Operators

ages = {"Dave": '22', "Bob": '33', "Mark": '38'}
for key, value in ages.items():
    print(f" {key} is {value} years old")

#Module 4 - Converting Types

#Convert to integer - int()

print(int(63.62))

#Convert to Float - float()

print(float(12))

#Convert to string - str()

print(str(99))

#Module 5 - Creating Lists

employees = ['Sara', 'Tammy', 'Debbie', 'John', 'Carrie']
print(employees)

#Module 6 - Modifying Lists

employees = ['Sara', 'Tammy', 'Debbie', 'John', 'Carrie']
print(employees)
print("--------------------------------------------------------")
employees[0] = 'Mark'  #This should replace whatever is at Index 0 with Mark
print(employees)


employees = ['Sara', 'Tammy', 'Debbie', 'John', 'Carrie']
employees.insert(1, 'Dave')  #Insert 'Dave' at Index spot 1, and move others down
print(employees)


#Loop through the list, printing each item per line
employees = ['Sara', 'Tammy', 'Debbie', 'John', 'Carrie']
for x in employees:
    print(x)


#Check for an item in the list
employees = ['Sara', 'Tammy', 'Debbie', 'John', 'Carrie']
if "Tammy" in employees:
    print("Yup, she is there")

#Module 7 - Sorting and Reversing Lists

#put in alphabetical order
colors = ['blue', 'red', 'yellow', 'green']
print(colors.sort())

#Reverse alphabetical order
colors = ['blue', 'red', 'yellow', 'green']
print(colors.sort(reverse=True))

#Just reverse order
colors = ['blue', 'red', 'yellow', 'green']
print(colors.reverse())

#Sorting without changing the list for good
colors = ['blue', 'red', 'yellow', 'green']
print(sorted(colors))

#Module 8 - Slicing Lists

#slicing starting at index 1, up to index 8, counting by 2
nums = [1, 2, 3, 4, 5, 6, 7, 8]
print(nums[1:8:2])

#slicing starting at index 0, up to index, counting by 1 (default count)
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(nums[0:9])

#Module 9 - Working with Operators
#Just a few to get your mind thinking

#################   Arithmetic Operators

x = 5 + 2
print(x)

y = 5 - 2
print(y)

z = 5 * 2
print(z)

a = 8 / 2
print(a)

b = 2**2
print(b)

#################   Assignment Operators
#ADD AND...
a = 2
a += 3
print(a)

#SUBTRACT AND...
z = 20
z -= 12
print(z)

#MULTIPLY AND...
x = 8
x *= 2
print(x)

#DIVIDE AND...
b = 20
b /= 2
print(b)

#EXPONENT AND...
t = 8
t **= 2
print(t)

#################  Comparison Operators
x == 10
y == 12
print(x == y)  #True or False?

t = 22
s = 8
print(t <= s)  #True or False?

#################   Logical Operators
a = 4
print(a > 2 and a < 7)    #True or False

b = 3
print(b < 2 or b > 1)     #True or False

#################   Identity Operators
w = 2
y = 6
x = w
print(w is y)
print(w is x)

#################   Membership Operators
nums = [1,2,3,4]
print(3 in nums)

nums = [1,2,3,4]
print(5 not in nums)

#Module 9 - Working with Operators
#Just a few to get your mind thinking

#################   Arithmetic Operators

x = 5 + 2
print(x)

y = 5 - 2
print(y)

z = 5 * 2
print(z)

a = 8 / 2
print(a)

b = 2**2
print(b)

#################   Assignment Operators
#ADD AND...
a = 2
a += 3
print(a)

#SUBTRACT AND...
z = 20
z -= 12
print(z)

#MULTIPLY AND...
x = 8
x *= 2
print(x)

#DIVIDE AND...
b = 20
b /= 2
print(b)

#EXPONENT AND...
t = 8
t **= 2
print(t)

#################  Comparison Operators
x == 10
y == 12
print(x == y)  #True or False?

t = 22
s = 8
print(t <= s)  #True or False?

#################   Logical Operators
a = 4
print(a > 2 and a < 7)    #True or False

b = 3
print(b < 2 or b > 1)     #True or False

#################   Identity Operators
w = 2
y = 6
x = w
print(w is y)
print(w is x)

#################   Membership Operators
nums = [1,2,3,4]
print(3 in nums)

nums = [1,2,3,4]
print(5 not in nums)

#Module 11 - IF Statements

x = 1
y = 3
if x > y:
    print("X is greater than Y")
elif x == y:
    print("X and Y are equal")
else:
    print("Y is greater than X")


#Without IF statements

employees = ['Mark', 'Steve', 'Dave', 'Lisa', 'Jordyn']

if 'Steve' in employees:
    print("Steve is an employee")
if 'Lisa' in employees:
    print("Lisa is an employee")
if 'John' in employees:
    print("John is an employee")

print("All done with employee selection")

#Module 12 - Working with For Loops

employees = ['Mark', 'Lisa', 'John', 'Dave']
for x in employees:
    print(x)


#Using a for loop to print a range

for y in range(25):
    print(y)

for b in range(0, 100, 5):
    print(b)

#Module 13 - Working with While Loops

x = 1
while x < 10:
    print("You are the best!!")
    x += 1

#Module 14 - Nesting For Loops

# Should print the numbers once, with all the letters listed below

nums = [1, 2, 3]
letters = ['a', 'b', 'c', 'd']

for x in nums:
    print(x)
    for y in letters:
        print(y)
#Module 14 - Nesting For Loops

# Should print the numbers once, with all the letters listed below

nums = [1, 2, 3]
letters = ['a', 'b', 'c', 'd']

for x in nums:
    print(x)
    for y in letters:
        print(y)

#Module 15 - Reading Files

#Don't forget about the path where the file will be saved if creating a new one
#Don't forget about the path where the file will be searched for when opening a file

# r - Opens a file in Read Only mode
# w - Opens a file that allows Write-level access
# a - Opens file in Append mode

x = open("filename.txt", 'r')
print(x.readline())
x.close()

#Creating a new file

b = open("FileNameHere.txt", 'x')

#Module 16 - Copying Files

#   shutil - don't forget to import the module
import shutil

shutil.copy(src, dst)

#   Copies and metadata

shutil.copystat(src, dst)

import shutil
src = "SourceFile.txt"
dst = "DestinationFile.txt"
shutil.copy(src, dst)

#Module 17 - Merging Emails

#Will need the Names.txt file with a few names entered
#Will need the Message.txt flie with a message inside the file

with open("Names.txt", 'r') as name_file:
    with open("Message.txt", 'r') as message_file:

              body = message_file.read()
              for name in name_file:
                  mail = "Hey " + name + body
                  with open(name.strip() +".txt", 'w') as message_file:
                      message_file.write(mail)

#Should create however many files are in the Names.txt file and put the message from Message.txt in each new file created.

#Module 18 - Reading Console inputs and formatting outputs

txt = input("Please enter a number: ")
num = int(txt)
print("You entered the number", num)

#Module 19 - Reading Command Line Arguments

#Reading information about the file you are working on

import sys

print("The name of our file is:", (sys.argv[0]))

#Module 20 - Defining Functions

#Creating some functions

def my_first():
    print("This is my first function")

my_first()

#Module 21 - Default Arguments

#Same on that is on the slide

def student(firstname, lastname="Bigger", major="IT"):
    print(firstname, lastname, "majors in", major)

#1 argument

student("Tony")

#2 arguements

student("Stan", "Lee")

#3 arguments

student("Tony", "Stark", "physics")

#Module 22 - Keyword and Positional Arguments

#Like on the slides

def greet(name, msg="How are you today?"):
    print("Hey", name + ", " + msg)

# 2 keyword

greet(name="Dave", msg="What's going on today?")

#1 positional, 1 keyword

greet("Dave", msg = "How you doin?")

#Module 23 - Handling Exceptions

import sys

try:
    num = int(input("Please enter your favorite number: "))

except ValueError:
    print("Please only use numbers, no text")
    sys.exit()

print("You enetered the number", num)

#Module 24 - Using Math and Random Modules

#Math has tons of operations and we can't list them all out here like mentioned during the lecture

import math

num = int(input("Please enter your favorite number, and  we will tell you the square root: "))
print(math.sqrt(num))


#Random

import random

print("Print a random integer between 0 and 500:", random.randint(0, 500))

#Module 25 - Displaying Datetime and Working Directory

#import all your modules!

from datetime import date
from datetime import time
from datetime import datetime

today = date.today()
date_time = datetime.now()

print("Today's date is: ", today)
print("Can you be more specific please? ", date_time)
print("Break it down....")
print("The hour ", date_time.hour)
print("The minute ", date_time.minute)
print("The seconds ", date_time.second)

#Working directory
print("\n")
import os

dirpath = os.getcwd()
print("Your current working directory is: " + dirpath)

foldername = os.path.basename(dirpath)
print("The specific folder is: " + foldername)

