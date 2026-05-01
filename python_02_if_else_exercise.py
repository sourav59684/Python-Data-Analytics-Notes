# %% A. Python IF (Single Condition)

# 1. Write a Python program to check if a number is positive.
a = int (input("Enter any number : "))
if a > 0:
    print("Positive number")
else:
    print("Negative number")
    
# %%
# 2. Print "Eligible to vote" if age is 18 or above.
age = int (input("Enter your age : "))
if age >= 18:
    print ("Eligible to Vote")
else :
    print ("Not Eligible to Vote")

# %%
# 3. Check if a number is divisible by 7.
num = int (input("Enter any number : "))
if num % 7 == 0:
    print("Divisible by 7")
else:
    print("Not Divisible by 7")

# %%
# 4. Print "Pass" if marks are greater than 40.
marks = int (input("Enter your marks : "))
if marks > 40:
    print("Pass")
else:
    print("Fail")

# %%
# 5. Check if a number is greater than 100.
num = int (input("Enter any number : "))
if num > 100:
    print("Number is greater than 100")
else:
    print("Number is not greater than 100")

# %%
# 6. Display a message if temperature exceeds 45°C.
temp = float(input("Enter temperature: "))
if temp > 45:
    print("Temperature exceeds 45°C")

# %%
# 7. Check if a string length is more than 8 characters.
s = input("Enter a string: ")
if len(s) > 8:
    print("String length is more than 8 characters")

# %%
# 8. Print "Logged In" if password matches "admin123".
password = input("Enter password: ")
if password == "admin123":
    print("Logged In")

# %%
# 9. Check if a number is a multiple of 10.
num = int (input("Enter any number : "))
if num % 10 == 0:
    print("Number is a multiple of 10")

# %%
# 10. Print a warning if balance is below minimum limit.
balance = float(input("Enter your account balance: "))
min_limit = 1000.0
if balance < min_limit:
    print("Warning: Account balance is below minimum limit.")
else:    print("Account balance is sufficient.")


# %% B. Python IF–ELSE (Two Conditions)

# 11. Check whether a number is even or odd.
num = int (input("Enter any number : "))
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")

# %%
# 12. Find the largest of two numbers.
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
if num1 > num2:
    print(num1," is largest.")
elif num2 > num1:
    print(num2, " is largest.")
else:
    print("Both numbers are equal.")

# %%
# 13. Check whether a person is eligible for driving license.
age = int (input("Enter your age : "))
if age >= 18:
    print("Eligible for driving license")
else:    print("Not eligible for driving license")

# %%
# 14. Print "Pass" or "Fail" based on marks.
marks = int (input("Enter your marks : "))
if marks >= 40:
    print("Pass")
else:    print("Fail")

# %%
# 15. Check whether a number is positive or negative.
num = int (input("Enter any number : "))
if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("Zero")

# %%
# 16. Check whether a character is a vowel or consonant.
char = input("Enter a character: ")
if char.lower() in 'aeiou':
    print("Vowel")
else:    print("Consonant")

# %%
# 17. Check if a year is leap or not.
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year.")
else:    print(year, "is not a leap year.")

# %%
# 18. Print "Valid Password" or "Invalid Password".
password = input("Enter password: ")
if len(password) >= 8 and any(char.isdigit() for char in password) and any(char.isalpha() for char in password):
    print("Valid Password")
else:    print("Invalid Password")

# %%
# 19. Determine whether salary is taxable or not.
salary = float(input("Enter your salary: "))
taxable_threshold = 50000.0
if salary > taxable_threshold:
    print("Salary is taxable.")
else:
    print("Salary is not taxable.")

# %%
# 20. Check whether a number is greater than 50 or not.
num = int (input("Enter any number : "))
if num > 50:
    print("Number is greater than 50")
else:    print("Number is not greater than 50")


# %% C. Python NESTED IF–ELSE

# 21. Find the largest of three numbers.
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
if num1 >= num2 and num1 >= num3:
    print(num1, "is the largest.")
elif num2 >= num1 and num2 >= num3:
    print(num2, "is the largest.")
else:
    print(num3, "is the largest.")

# %%
# 22. Check whether a number is positive, negative, or zero.
num = float(input("Enter a number: "))
if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("Zero")

# %%
# 23. Assign grades:
# A → marks ≥ 90
# B → marks ≥ 75
# C → marks ≥ 60
# Fail → below 60
marks = float(input("Enter marks: "))
if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
else:
    print("Grade: Fail")

# %%
# 24. Check whether a triangle is equilateral, isosceles, or scalene.
side1 = float(input("Enter the length of the first side: "))
side2 = float(input("Enter the length of the second side: "))
side3 = float(input("Enter the length of the third side: "))
if side1 == side2 == side3:
    print("The triangle is equilateral.")
elif side1 == side2 or side2 == side3 or side1 == side3:
    print("The triangle is isosceles.")
else:
    print("The triangle is scalene.")

# %%
# 25. Check whether a character is uppercase, lowercase, digit, or special character.
char = input("Enter a character: ")
if char.isupper():
    print("Uppercase letter")
elif char.islower():
    print("Lowercase letter")
elif char.isdigit():
    print("Digit")
else:
    print("Special character")

# %%
# 26. Calculate electricity bill using slab-wise rates.
units = float(input("Enter electricity bill amount: "))
if units <= 100:
    total_bill = units * 0.5
elif units <= 200:
    total_bill = 50 + (units - 100) * 0.75
else:
    total_bill = 125 + (units - 200) * 1.0
print("Total electricity bill: $", total_bill)

# %%
# 27. Validate login using username and password.
username = input("Enter username: ")
password = input("Enter password: ")
if username == "admin" and password == "admin123":
    print("Login successful")
else:    print("Invalid username or password")

# %%
# 28. Check student result using marks of 3 subjects.
subject1 = float(input("Enter marks for subject 1: "))
subject2 = float(input("Enter marks for subject 2: "))
subject3 = float(input("Enter marks for subject 3: "))
average_marks = (subject1 + subject2 + subject3) / 3
if average_marks >= 40 and subject1 >= 40 and subject2 >= 40 and subject3 >= 40:
    print("Pass")
else:
    print("Fail")

# %%
# 29. Find the second largest number among three numbers.
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
if (num1 >= num2 and num1 <= num3) or (num1 <= num2 and num1 >= num3):
    print(num1, "is the second largest.")
elif (num2 >= num1 and num2 <= num3) or (num2 <= num1 and num2 >= num3):
    print(num2, "is the second largest.")
else:
    print(num3, "is the second largest.")

# %%
# 30. Check loan eligibility using age, salary, and credit score.
age = int(input("Enter your age: "))
salary = float(input("Enter your salary: "))
credit_score = int(input("Enter your credit score: "))
if age >= 21 and salary >= 25000 and credit_score >= 700:
    print("Eligible for loan")
else:    print("Not eligible for loan")

# %% D. Python ELIF (Multiple Conditions)

# 31. Print day name using day number (1–7).
day_num = int(input("Enter day number (1-7): "))
if day_num == 1:
    print("Monday")
elif day_num == 2:
    print("Tuesday")
elif day_num == 3:
    print("Wednesday")
elif day_num == 4:
    print("Thursday")
elif day_num == 5:
    print("Friday")
elif day_num == 6:
    print("Saturday")
elif day_num == 7:
    print("Sunday")
else:
    print("Invalid day number. Please enter a number between 1 and 7.")

# %%
# 32. Print month name using month number.
month_num = int(input("Enter month number (1-12): "))
if month_num == 1:
    print("January")
elif month_num == 2:
    print("February")
elif month_num == 3:
    print("March")
elif month_num == 4:
    print("April")
elif month_num == 5:
    print("May")
elif month_num == 6:
    print("June")
elif month_num == 7:
    print("July")
elif month_num == 8:
    print("August")
elif month_num == 9:
    print("September")
elif month_num == 10:
    print("October")
elif month_num == 11:
    print("November")
elif month_num == 12:
    print("December")
else:
    print("Invalid month number. Please enter a number between 1 and 12.")

# %%
# 33. Display grade based on percentage.
percentage = float(input("Enter percentage: "))
if percentage >= 90:
    print("Grade: A")
elif percentage >= 80:
    print("Grade: B")
elif percentage >= 70:
    print("Grade: C")
elif percentage >= 60:
    print("Grade: D")
else:
    print("Grade: F")

# %%
# 34. Display bonus percentage based on experience years.
experience_years = int(input("Enter years of experience: "))
if experience_years >= 10:
    print("Bonus: 20%")
elif experience_years >= 5:
    print("Bonus: 10%")
else:
    print("No bonus.")

# %%
# 35. Identify traffic signal meaning.
signal_color = input("Enter traffic signal color (red/yellow/green): ").lower()
if signal_color == "red":
    print("Stop")
elif signal_color == "yellow":
    print("Caution")
elif signal_color == "green":
    print("Go")
else:    print("Invalid signal color. Please enter red, yellow, or green.")

# %%
# 36. Categorize temperature as Cold / Warm / Hot.
temperature = float(input("Enter temperature in °C: "))
if temperature < 15:
    print("Cold")
elif temperature < 25:
    print("Warm")
else:
    print("Hot")

# %%
# 37. Categorize employee based on salary range.
salary = float(input("Enter employee salary: "))
if salary < 30000:
    print("Low salary")
elif salary < 50000:
    print("Medium salary")
else:
    print("High salary")

# %%
# 38. Print discount percentage based on purchase amount.
amount = float(input("Enter purchase amount: "))
if amount >= 1000:
    print("Discount: 20%")
elif amount >= 500:
    print("Discount: 10%")
else:    print("No discount.")

# %%
# 39. Identify number type: single-digit / double-digit / multi-digit.
num = int(input("Enter a number: "))
if num >= 0 and num < 10:
    print("Single-digit number")
elif num < 100:
    print("Double-digit number")
else:
    print("Multi-digit number")

# %%
# 40. Assign performance rating: Poor / Average / Good / Excellent.
rating = float(input("Enter performance rating (0-10): "))
if rating < 4:
    print("Performance: Poor")
elif rating < 7:
    print("Performance: Average")
elif rating < 9:
    print("Performance: Good")
else:
    print("Performance: Excellent")

# %% E. Python COMPLEX CONDITIONS (AND / OR / NOT)

# 41. Check whether a number is divisible by 5 and 11.
num = int(input("Enter any number: "))
if num % 5 == 0 and num % 11 == 0:
    print("Number is divisible by both 5 and 11")
else:    print("Number is not divisible by both 5 and 11")

# %%
# 42. Check if a person is eligible for loan:
# age ≥ 21
# salary ≥ 25,000
# credit score ≥ 700
age = int(input("Enter your age: "))
salary = float(input("Enter your salary: "))
credit_score = int(input("Enter your credit score: "))
if age >= 21 and salary >= 25000 and credit_score >= 700:
    print("Eligible for loan")
else:    print("Not eligible for loan")

# %%
# 43. Validate login using username AND password.
username = input("Enter username: ")
password = input("Enter password: ")
if username == "admin" and password == "admin123":
    print("Login successful")
else:    print("Invalid username or password")

# %%
# 44. Check student pass condition:
# All subjects ≥ 40
# Average ≥ 50
marks1 = float(input("Enter marks for subject 1: "))
marks2 = float(input("Enter marks for subject 2: "))
marks3 = float(input("Enter marks for subject 3: "))
average_marks = (marks1 + marks2 + marks3) / 3
if marks1 >= 40 and marks2 >= 40 and marks3 >= 40 and average_marks >= 50:
    print("Student has passed")
else:
    print("Student has failed")

# %%
# 45. Check if a number lies between 10 and 100.
num = int(input("Enter a number: "))
if num > 10 and num < 100:
    print("Number lies between 10 and 100")
else:
    print("Number does not lie between 10 and 100")

# %%
# 46. Check exam eligibility:
# attendance ≥ 75% OR
# medical certificate available
attendance = float(input("Enter attendance percentage: "))
medical_certificate = input("Do you have a medical certificate? (yes/no): ").lower()
if attendance >= 75 or medical_certificate == "yes":
    print("Eligible for exam")
else:
    print("Not eligible for exam")

# %%
# 47. Validate a date using conditions.
date = int(input("Enter date (1-31): "))
month = int(input("Enter month (1-12): "))
year = int(input("Enter year: "))

if month < 1 or month > 12 or date < 1:
    print("Invalid date")
else:
    if month in (1, 3, 5, 7, 8, 10, 12):
        max_day = 31
    elif month in (4, 6, 9, 11):
        max_day = 30
    else:
        # February
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            max_day = 29
        else:
            max_day = 28

    if date <= max_day:
        print("Valid date")
    else:
        print("Invalid date")

# %%
# 48. Check whether an email format is valid.
email = input("Enter email address: ")
if "@" in email and "." in email and email.index("@") < email.rindex("."):
    print("Valid email format")
else:    print("Invalid email format")

# %%
# 49. Determine insurance eligibility using age, health status, and income.
age = int(input("Enter your age: "))
health_status = input("Enter your health status (good/average/poor): ").lower()
income = float(input("Enter your income: "))
if age < 60 and health_status == "good" and income >= 30000:
    print("Eligible for insurance")
else:    print("Not eligible for insurance")

# %%
# 50. Check leap year using complete leap year logic.
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year.")
else:    print(year, "is not a leap year.")

# %% F. INTERVIEW-LEVEL PYTHON LOGIC QUESTIONS

# 51. Write a Python program to calculate income tax using slabs.
income = float(input("Enter your annual income: "))
if income <= 250000:
    tax = 0
elif income <= 500000:
    tax = (income - 250000) * 0.05
else:
    tax = (income - 500000) * 0.2 + 12500
print("Income tax to be paid: $", tax)

# %%
# 52. Create an ATM withdrawal program with balance checks.
balance = float(input("Enter your account balance: "))
withdrawal = float(input("Enter the amount to withdraw: "))
if withdrawal > balance:
    print("Insufficient funds")
else:
    balance -= withdrawal
    print("Withdrawal successful. Remaining balance: $", balance)

# %%
# 53. Check promotion eligibility using experience and performance.
experience_years = int(input("Enter years of experience: "))
performance_rating = float(input("Enter performance rating (0-10): "))
if experience_years >= 5 and performance_rating >= 8:
    print("Eligible for promotion")
else:    print("Not eligible for promotion")

# %%
# 54. Implement a grading system using nested if–else.
marks = float(input("Enter marks: "))
if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
else:
    print("Grade: C")

# %%
# 55. Validate strong password using multiple conditions.
password = input("Enter password: ")
if len(password) >= 8 and any(char.isdigit() for char in password) and any(char.isalpha() for char in password) and any(char in "!@#$%^&*()-_+=" for char in password):
    print("Strong password")
else:    print("Weak password. A strong password must be at least 8 characters long and include letters, numbers, and special characters.")

# %%
# 56. Calculate delivery charges based on location and order amount.
amount = float(input("Enter order amount: "))
location = input("Enter delivery location (local/non-local): ").lower()
if location == "local":
    if amount >= 100:
        delivery_charge = 0
    else:
        delivery_charge = 5
else:
    if amount >= 100:
        delivery_charge = 10
    else:
        delivery_charge = 15
print("Delivery charge: $", delivery_charge)

# %%
# 57. Determine online exam qualification.
exam_score = float(input("Enter exam score: "))
cuttoff_score = float(input("Enter cutoff score: "))
if exam_score >= cuttoff_score:
    print("Qualified for online exam")
else:    print("Not qualified for online exam")

# %%
# 58. Create movie ticket pricing logic based on age & show time.
age = int(input("Enter your age: "))
show_time = input("Enter show time (matinee/evening): ").lower()
if show_time == "matinee":
    if age < 12:
        price = 5
    elif age < 60:
        price = 10
    else:
        price = 7
else:
    if age < 12:
        price = 7
    elif age < 60:
        price = 12
    else:        price = 10
print("Ticket price: $", price)

# %%
# 59. Determine bank account type based on balance.
balance = float(input("Enter your account balance: "))
if balance < 1000:
    account_type = "Basic Savings Account"
elif balance < 5000:
    account_type = "Regular Savings Account"
elif balance < 10000:
    account_type = "Premium Savings Account"
else:
    account_type = "Platinum Savings Account"
print("Account type: ", account_type)

# %%
# 60. Create a menu-driven program using if–elif–else.
print("Menu:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
choice = int(input("Enter your choice (1-4): "))
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
if choice == 1:
    result = num1 + num2
    print("Result: ", result)
elif choice == 2:
    result = num1 - num2
    print("Result: ", result)
elif choice == 3:
    result = num1 * num2
    print("Result: ", result)
elif choice == 4:
    if num2 != 0:
        result = num1 / num2
        print("Result: ", result)
    else:
        print("Error: Division by zero is not allowed.")