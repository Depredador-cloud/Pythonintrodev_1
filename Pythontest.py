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
Usa el código con precaución.


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
