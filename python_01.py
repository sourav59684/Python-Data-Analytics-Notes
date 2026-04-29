# %%
# 1. Write a program to print “Hello Python” on the screen.
print ("Hello Python")

# %%
# 2. Take a name as input and print:
name = input ("Enter Your Name : ")
print ("Welcome ",name)

# %%
# 3. Take a number as input and print it.
age = int(input ("Enter Your Age : "))
print ("Your age is : ",age)

# %%
# 4. Take two numbers as input and print both numbers on separate lines.
num1 = int(input ("Enter first no. : "))
num2 = int(input ("Enter second no. : "))
print ("First no. : ",num1)
print ("Second no. : ",num2)

# %%
# 5. Take a name and age as input and print:
# My name is ___ and my age is ___
name = input ("Enter Your Name : ")
age = int(input ("Enter Your Age :"))
print ("My name is : ",name," and my age is : ",age)

# %%
# 6. Take an integer as input and print its square.
num2 = int(input ("Enter a number :"))
print ("square of ",num2, " is ", num2*num2)


# %%
# 7. Take two integers as input and print their sum.
num3 = int(input ("Enter first number :"))
num4 = int(input ("Enter second number :"))
print ("sum of ",num3, "and ",num4," is : ",num3+num4)

# %%
# 8. Take two integers and print:
# Addition
# Subtraction
# Multiplication
num1 = int(input ("Enter first number :"))
num2 = int(input ("Enter second number :"))
print ("Addition of ",num1, "and ",num2," is : ",num1+num2)
print ("Subtraction of ",num1, "and ",num2," is : ",num1-num2)
print ("Multiplication of ",num1, "and ",num2," is : ",num1*num2)

# %%
# 9. Take a number and print:
# The number entered is <number>
num = int(input ("Enter a number :"))
print ("The number entered is : ",num)

# %%
# 10. Take an integer and print its double.
num = int(input ("Enter a number :"))
print ("Double of ",num," is : ",num*2)

# %%
# 11. Take a float value as input and print it.
num = float(input ("Enter a float number :"))
print ("The float number entered is : ",num)


# %%
# 12. Take two float numbers and print their sum.
num1 = float(input ("Enter first float number :"))
num2 = float(input ("Enter second float number :"))
print ("Sum of ",num1, " and ",num2, " is : ",num1+num2)

# %%
# 13. Take a float number and print its half value.
num = float(input ("Enter second number :"))
print (num/2)

# %%
# 14. Take length and width (float) as input and print the area of a rectangle.
length = float(input ("Enter length of rectangle :"))
width = float(input ("Enter width of rectangle :"))
print ("Area of rectangle is : ",length*width)

# %%
# 15. Take radius as float input and print the area of a circle.
# (Use π = 3.14)
radius = float(input ("Enter radius of circle :"))
pi = 3.14
print ("Area of circle is : ",pi*radius*radius)

# %%
# 16. Take one integer and one float as input and print both.
num1 = int(input ("Enter an integer :"))
num2 = float(input ("Enter a float number :"))
print ("Integer entered is : ",num1)
print ("Float number entered is : ",num2)

# %%
# 17. Take total marks (int) and number of subjects (int) and print the average as float.
total_marks = int(input ("Enter total marks :"))
num_subjects = int(input ("Enter number of subjects :"))
print ("Average marks is : ",float(total_marks)/num_subjects)

# %%
# 18. Take price (float) and quantity (int) and print the total cost.
price = float(input ("Enter price of item :"))
quantity = int(input ("Enter quantity :"))
print ("Total cost is : ",price*quantity)

# %%
# 19. Take two numbers (one int, one float) and print their sum.
num1 = int(input ("Enter an integer :"))
num2 = float(input ("Enter a float number :"))
print ("Sum is : ",num1+num2)

# %%
# 20. Take salary (float) and bonus (int) and print the final salary.
salary = float(input ("Enter salary :"))
bonus = int(input ("Enter bonus :"))
print ("Final salary is : ",salary+bonus)
