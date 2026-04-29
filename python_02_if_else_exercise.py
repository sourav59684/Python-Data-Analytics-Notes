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

# %%
# 22. Check whether a number is positive, negative, or zero.

# %%
# 23. Assign grades:
# A → marks ≥ 90
# B → marks ≥ 75
# C → marks ≥ 60
# Fail → below 60

# %%
# 24. Check whether a triangle is equilateral, isosceles, or scalene.

# %%
# 25. Check whether a character is uppercase, lowercase, digit, or special character.

# %%
# 26. Calculate electricity bill using slab-wise rates.

# %%
# 27. Validate login using username and password.

# %%
# 28. Check student result using marks of 3 subjects.

# %%
# 29. Find the second largest number among three numbers.

# %%
# 30. Check loan eligibility using age, salary, and credit score.



# %% D. Python ELIF (Multiple Conditions)

# 31. Print day name using day number (1–7).

# %%
# 32. Print month name using month number.

# %%
# 33. Display grade based on percentage.

# %%
# 34. Display bonus percentage based on experience years.

# %%
# 35. Identify traffic signal meaning.

# %%
# 36. Categorize temperature as Cold / Warm / Hot.

# %%
# 37. Categorize employee based on salary range.

# %%
# 38. Print discount percentage based on purchase amount.

# %%
# 39. Identify number type: single-digit / double-digit / multi-digit.

# %%
# 40. Assign performance rating: Poor / Average / Good / Excellent.



# %% E. Python COMPLEX CONDITIONS (AND / OR / NOT)

# 41. Check whether a number is divisible by 5 and 11.

# %%
# 42. Check if a person is eligible for loan:
# age ≥ 21
# salary ≥ 25,000
# credit score ≥ 700

# %%
# 43. Validate login using username AND password.

# %%
# 44. Check student pass condition:
# All subjects ≥ 40
# Average ≥ 50

# %%
# 45. Check if a number lies between 10 and 100.

# %%
# 46. Check exam eligibility:
# attendance ≥ 75% OR
# medical certificate available

# %%
# 47. Validate a date using conditions.

# %%
# 48. Check whether an email format is valid.

# %%
# 49. Determine insurance eligibility using age, health status, and income.

# %%
# 50. Check leap year using complete leap year logic.



# %% F. INTERVIEW-LEVEL PYTHON LOGIC QUESTIONS

# 51. Write a Python program to calculate income tax using slabs.

# %%
# 52. Create an ATM withdrawal program with balance checks.

# %%
# 53. Check promotion eligibility using experience and performance.

# %%
# 54. Implement a grading system using nested if–else.

# %%
# 55. Validate strong password using multiple conditions.

# %%
# 56. Calculate delivery charges based on location and order amount.

# %%
# 57. Determine online exam qualification.

# %%
# 58. Create movie ticket pricing logic based on age & show time.

# %%
# 59. Determine bank account type based on balance.

# %%
# 60. Create a menu-driven program using if–elif–else.