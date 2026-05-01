# Python Basics — Input, Output & Arithmetic (Problems 1–20)

# =============================================================================
# A. PRINT & INPUT
# =============================================================================

# 1. Print "Hello Python".
print("Hello Python")

# 2. Take a name as input and greet the user.
name = input("Enter your name: ")
print(f"Welcome, {name}")

# 3. Take a number as input and print it.
age = int(input("Enter your age: "))
print(f"Your age is: {age}")

# 4. Take two numbers and print them on separate lines.
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print(f"First number : {num1}")
print(f"Second number: {num2}")

# 5. Take name and age as input and print a formatted sentence.
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(f"My name is {name} and my age is {age}.")


# =============================================================================
# B. INTEGER ARITHMETIC
# =============================================================================

# 6. Take an integer and print its square.
num = int(input("Enter a number: "))
print(f"Square of {num} = {num ** 2}")

# 7. Take two integers and print their sum.
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print(f"Sum of {num1} and {num2} = {num1 + num2}")

# 8. Take two integers and print addition, subtraction, and multiplication.
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print(f"Addition       : {num1 + num2}")
print(f"Subtraction    : {num1 - num2}")
print(f"Multiplication : {num1 * num2}")

# 9. Take a number and print it back.
num = int(input("Enter a number: "))
print(f"The number entered is: {num}")

# 10. Take an integer and print its double.
num = int(input("Enter a number: "))
print(f"Double of {num} = {num * 2}")


# =============================================================================
# C. FLOAT ARITHMETIC
# =============================================================================

# 11. Take a float value as input and print it.
num = float(input("Enter a float number: "))
print(f"Float entered: {num}")

# 12. Take two float numbers and print their sum.
num1 = float(input("Enter first float number: "))
num2 = float(input("Enter second float number: "))
print(f"Sum = {num1 + num2}")

# 13. Take a float number and print its half.
num = float(input("Enter a number: "))
print(f"Half of {num} = {num / 2}")

# 14. Take length and width (float) and print the area of a rectangle.
length = float(input("Enter length: "))
width = float(input("Enter width: "))
print(f"Area of rectangle = {length * width}")

# 15. Take radius (float) and print the area of a circle. (π = 3.14)
radius = float(input("Enter radius: "))
PI = 3.14
print(f"Area of circle = {PI * radius ** 2}")


# =============================================================================
# D. MIXED INT & FLOAT
# =============================================================================

# 16. Take one integer and one float as input and print both.
num1 = int(input("Enter an integer: "))
num2 = float(input("Enter a float number: "))
print(f"Integer : {num1}")
print(f"Float   : {num2}")

# 17. Take total marks (int) and number of subjects (int), print average as float.
total_marks = int(input("Enter total marks: "))
num_subjects = int(input("Enter number of subjects: "))
print(f"Average marks = {total_marks / num_subjects:.2f}")

# 18. Take price (float) and quantity (int), print total cost.
price = float(input("Enter price per item: "))
quantity = int(input("Enter quantity: "))
print(f"Total cost = {price * quantity:.2f}")

# 19. Take one int and one float, print their sum.
num1 = int(input("Enter an integer: "))
num2 = float(input("Enter a float number: "))
print(f"Sum = {num1 + num2}")

# 20. Take salary (float) and bonus (int), print final salary.
salary = float(input("Enter salary: "))
bonus = int(input("Enter bonus: "))
print(f"Final salary = {salary + bonus:.2f}")
