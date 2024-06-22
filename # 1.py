# 1. Study Python Syntax 
print("Hello, Python!")  # Basic print statement

# Variables and Data Types
name = "Aman"          # String (text)
age = 22                # Integer (whole number)
height = 6.2           # Float (decimal number)
is_student = True       # Boolean (True/False)

print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is Student:", is_student)

# 2. Practice Basic Scripts

# Arithmetic Operations
num1 = 10
num2 = 5
sum_result = num1 + num2
product_result = num1 * num2

print("Sum:", sum_result)
print("Product:", product_result)

# String Manipulation
message = "Welcome to Python learning!"
uppercase_message = message.upper()
substring = message[0:7]

print("Original:", message)
print("Uppercase:", uppercase_message)
print("Substring:", substring)

# Conditional Statements
temperature = 20
if temperature > 25:
    print("It's warm outside!")
else:
    print("It's a bit cool.")

# 3. Common Data Structures
fruits = ["apple", "banana", "orange"]     # List
person = {"name": "Bob", "age": 30}        # Dictionary
coordinates = (5, 10)                      # Tuple

print("Fruits:", fruits)
print("Person:", person)
print("Coordinates:", coordinates)

# Simple Loop (Iteration)
for fruit in fruits:
    print("I like", fruit)