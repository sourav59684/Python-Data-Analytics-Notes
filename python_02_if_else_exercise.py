"""
Python Conditional Statements - Practice Problems
==================================================
Topics Covered:
    A. Simple IF
    B. IF-ELSE
    C. Nested IF-ELSE
    D. ELIF (Multiple Conditions)
    E. Complex Conditions (AND / OR / NOT)
    F. Interview-Level Logic Questions
"""

# =============================================================================
# A. SIMPLE IF (Single Condition)
# =============================================================================

# 1. Check if a number is positive.
def check_positive():
    a = int(input("Enter any number: "))
    if a > 0:
        print("Positive number")
    else:
        print("Negative number")

# 2. Check voting eligibility (age >= 18).
def check_voting_eligibility():
    age = int(input("Enter your age: "))
    if age >= 18:
        print("Eligible to Vote")
    else:
        print("Not Eligible to Vote")

# 3. Check if a number is divisible by 7.
def check_divisible_by_7():
    num = int(input("Enter any number: "))
    if num % 7 == 0:
        print("Divisible by 7")
    else:
        print("Not Divisible by 7")

# 4. Print "Pass" if marks > 40.
def check_pass():
    marks = int(input("Enter your marks: "))
    if marks > 40:
        print("Pass")
    else:
        print("Fail")

# 5. Check if a number is greater than 100.
def check_greater_than_100():
    num = int(input("Enter any number: "))
    if num > 100:
        print("Number is greater than 100")
    else:
        print("Number is not greater than 100")

# 6. Display a message if temperature exceeds 45°C.
def check_temperature():
    temp = float(input("Enter temperature (°C): "))
    if temp > 45:
        print("Warning: Temperature exceeds 45°C!")

# 7. Check if a string length is more than 8 characters.
def check_string_length():
    s = input("Enter a string: ")
    if len(s) > 8:
        print("String length is more than 8 characters")
    else:
        print("String length is 8 characters or fewer")

# 8. Print "Logged In" if password matches "admin123".
def check_password():
    password = input("Enter password: ")
    if password == "admin123":
        print("Logged In")
    else:
        print("Incorrect password")

# 9. Check if a number is a multiple of 10.
def check_multiple_of_10():
    num = int(input("Enter any number: "))
    if num % 10 == 0:
        print("Number is a multiple of 10")
    else:
        print("Number is not a multiple of 10")

# 10. Warn if account balance is below minimum limit.
def check_balance():
    balance = float(input("Enter your account balance: "))
    min_limit = 1000.0
    if balance < min_limit:
        print("Warning: Account balance is below minimum limit.")
    else:
        print("Account balance is sufficient.")


# =============================================================================
# B. IF-ELSE (Two Conditions)
# =============================================================================

# 11. Check whether a number is even or odd.
def check_even_odd():
    num = int(input("Enter any number: "))
    if num % 2 == 0:
        print("Even number")
    else:
        print("Odd number")

# 12. Find the largest of two numbers.
def find_largest_of_two():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    if num1 > num2:
        print(f"{num1} is the largest.")
    elif num2 > num1:
        print(f"{num2} is the largest.")
    else:
        print("Both numbers are equal.")

# 13. Check driving license eligibility.
def check_driving_eligibility():
    age = int(input("Enter your age: "))
    if age >= 18:
        print("Eligible for driving license")
    else:
        print("Not eligible for driving license")

# 14. Print "Pass" or "Fail" based on marks (>= 40 to pass).
def check_pass_fail():
    marks = int(input("Enter your marks: "))
    if marks >= 40:
        print("Pass")
    else:
        print("Fail")

# 15. Check whether a number is positive, negative, or zero.
def check_sign():
    num = int(input("Enter any number: "))
    if num > 0:
        print("Positive number")
    elif num < 0:
        print("Negative number")
    else:
        print("Zero")

# 16. Check whether a character is a vowel or consonant.
def check_vowel_consonant():
    char = input("Enter a character: ")
    if char.lower() in "aeiou":
        print("Vowel")
    else:
        print("Consonant")

# 17. Check if a year is a leap year.
def check_leap_year():
    year = int(input("Enter a year: "))
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")

# 18. Validate password (>= 8 chars, has letter + digit).
def validate_password():
    password = input("Enter password: ")
    has_digit = any(char.isdigit() for char in password)
    has_alpha = any(char.isalpha() for char in password)
    if len(password) >= 8 and has_digit and has_alpha:
        print("Valid Password")
    else:
        print("Invalid Password")

# 19. Determine whether salary is taxable (threshold: 50,000).
def check_taxable_salary():
    salary = float(input("Enter your salary: "))
    taxable_threshold = 50000.0
    if salary > taxable_threshold:
        print("Salary is taxable.")
    else:
        print("Salary is not taxable.")

# 20. Check whether a number is greater than 50.
def check_greater_than_50():
    num = int(input("Enter any number: "))
    if num > 50:
        print("Number is greater than 50")
    else:
        print("Number is not greater than 50")


# =============================================================================
# C. NESTED IF-ELSE
# =============================================================================

# 21. Find the largest of three numbers.
def find_largest_of_three():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    num3 = float(input("Enter third number: "))
    if num1 >= num2 and num1 >= num3:
        print(f"{num1} is the largest.")
    elif num2 >= num1 and num2 >= num3:
        print(f"{num2} is the largest.")
    else:
        print(f"{num3} is the largest.")

# 22. Check whether a number is positive, negative, or zero.
def check_positive_negative_zero():
    num = float(input("Enter a number: "))
    if num > 0:
        print("Positive number")
    elif num < 0:
        print("Negative number")
    else:
        print("Zero")

# 23. Assign grades based on marks.
#     A → marks >= 90 | B → marks >= 75 | C → marks >= 60 | Fail → below 60
def assign_grade():
    marks = float(input("Enter marks: "))
    if marks >= 90:
        print("Grade: A")
    elif marks >= 75:
        print("Grade: B")
    elif marks >= 60:
        print("Grade: C")
    else:
        print("Grade: Fail")

# 24. Identify triangle type: equilateral, isosceles, or scalene.
def identify_triangle():
    side1 = float(input("Enter length of side 1: "))
    side2 = float(input("Enter length of side 2: "))
    side3 = float(input("Enter length of side 3: "))
    if side1 == side2 == side3:
        print("Equilateral triangle")
    elif side1 == side2 or side2 == side3 or side1 == side3:
        print("Isosceles triangle")
    else:
        print("Scalene triangle")

# 25. Identify character type: uppercase, lowercase, digit, or special.
def identify_char_type():
    char = input("Enter a character: ")
    if char.isupper():
        print("Uppercase letter")
    elif char.islower():
        print("Lowercase letter")
    elif char.isdigit():
        print("Digit")
    else:
        print("Special character")

# 26. Calculate electricity bill using slab-wise rates.
#     0-100 units  → ₹0.50/unit
#     101-200 units → ₹0.75/unit
#     200+ units   → ₹1.00/unit
def calculate_electricity_bill():
    units = float(input("Enter units consumed: "))
    if units <= 100:
        total_bill = units * 0.50
    elif units <= 200:
        total_bill = 50 + (units - 100) * 0.75
    else:
        total_bill = 125 + (units - 200) * 1.0
    print(f"Total electricity bill: ₹{total_bill:.2f}")

# 27. Validate login using username and password.
def validate_login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username == "admin" and password == "admin123":
        print("Login successful")
    else:
        print("Invalid username or password")

# 28. Check student result (all subjects >= 40, average >= 40).
def check_student_result():
    s1 = float(input("Enter marks for subject 1: "))
    s2 = float(input("Enter marks for subject 2: "))
    s3 = float(input("Enter marks for subject 3: "))
    avg = (s1 + s2 + s3) / 3
    if avg >= 40 and s1 >= 40 and s2 >= 40 and s3 >= 40:
        print("Pass")
    else:
        print("Fail")

# 29. Find the second largest among three numbers.
def find_second_largest():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    num3 = float(input("Enter third number: "))
    numbers = sorted([num1, num2, num3])
    print(f"Second largest: {numbers[1]}")

# 30. Check loan eligibility (age >= 21, salary >= 25000, credit score >= 700).
def check_loan_eligibility():
    age = int(input("Enter your age: "))
    salary = float(input("Enter your salary: "))
    credit_score = int(input("Enter your credit score: "))
    if age >= 21 and salary >= 25000 and credit_score >= 700:
        print("Eligible for loan")
    else:
        print("Not eligible for loan")


# =============================================================================
# D. ELIF (Multiple Conditions)
# =============================================================================

# 31. Print day name using day number (1–7).
def print_day_name():
    days = {1: "Monday", 2: "Tuesday", 3: "Wednesday",
            4: "Thursday", 5: "Friday", 6: "Saturday", 7: "Sunday"}
    day_num = int(input("Enter day number (1-7): "))
    print(days.get(day_num, "Invalid day number. Please enter 1-7."))

# 32. Print month name using month number (1–12).
def print_month_name():
    months = {1: "January", 2: "February", 3: "March", 4: "April",
              5: "May", 6: "June", 7: "July", 8: "August",
              9: "September", 10: "October", 11: "November", 12: "December"}
    month_num = int(input("Enter month number (1-12): "))
    print(months.get(month_num, "Invalid month number. Please enter 1-12."))

# 33. Display grade based on percentage.
#     A → 90+  | B → 80+  | C → 70+  | D → 60+  | F → below 60
def display_grade():
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

# 34. Display bonus percentage based on experience.
#     10+ years → 20% | 5+ years → 10% | else → No bonus
def display_bonus():
    experience_years = int(input("Enter years of experience: "))
    if experience_years >= 10:
        print("Bonus: 20%")
    elif experience_years >= 5:
        print("Bonus: 10%")
    else:
        print("No bonus.")

# 35. Identify traffic signal meaning.
def identify_traffic_signal():
    signal = input("Enter traffic signal color (red/yellow/green): ").lower()
    signals = {"red": "Stop", "yellow": "Caution", "green": "Go"}
    print(signals.get(signal, "Invalid color. Enter red, yellow, or green."))

# 36. Categorize temperature as Cold / Warm / Hot.
def categorize_temperature():
    temperature = float(input("Enter temperature (°C): "))
    if temperature < 15:
        print("Cold")
    elif temperature < 25:
        print("Warm")
    else:
        print("Hot")

# 37. Categorize employee based on salary range.
def categorize_salary():
    salary = float(input("Enter employee salary: "))
    if salary < 30000:
        print("Low salary")
    elif salary < 50000:
        print("Medium salary")
    else:
        print("High salary")

# 38. Print discount percentage based on purchase amount.
def print_discount():
    amount = float(input("Enter purchase amount: "))
    if amount >= 1000:
        print("Discount: 20%")
    elif amount >= 500:
        print("Discount: 10%")
    else:
        print("No discount.")

# 39. Identify number type: single-digit / double-digit / multi-digit.
def identify_digit_type():
    num = int(input("Enter a number: "))
    if 0 <= num < 10:
        print("Single-digit number")
    elif num < 100:
        print("Double-digit number")
    else:
        print("Multi-digit number")

# 40. Assign performance rating: Poor / Average / Good / Excellent.
def assign_performance_rating():
    rating = float(input("Enter performance rating (0-10): "))
    if rating < 4:
        print("Performance: Poor")
    elif rating < 7:
        print("Performance: Average")
    elif rating < 9:
        print("Performance: Good")
    else:
        print("Performance: Excellent")


# =============================================================================
# E. COMPLEX CONDITIONS (AND / OR / NOT)
# =============================================================================

# 41. Check whether a number is divisible by both 5 and 11.
def check_divisible_5_and_11():
    num = int(input("Enter any number: "))
    if num % 5 == 0 and num % 11 == 0:
        print("Divisible by both 5 and 11")
    else:
        print("Not divisible by both 5 and 11")

# 42. Check loan eligibility (age >= 21, salary >= 25000, credit score >= 700).
def check_loan_eligibility_complex():
    age = int(input("Enter your age: "))
    salary = float(input("Enter your salary: "))
    credit_score = int(input("Enter your credit score: "))
    if age >= 21 and salary >= 25000 and credit_score >= 700:
        print("Eligible for loan")
    else:
        print("Not eligible for loan")

# 43. Validate login using username AND password.
def validate_login_complex():
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username == "admin" and password == "admin123":
        print("Login successful")
    else:
        print("Invalid username or password")

# 44. Check student pass: all subjects >= 40 AND average >= 50.
def check_student_pass_complex():
    m1 = float(input("Enter marks for subject 1: "))
    m2 = float(input("Enter marks for subject 2: "))
    m3 = float(input("Enter marks for subject 3: "))
    avg = (m1 + m2 + m3) / 3
    if m1 >= 40 and m2 >= 40 and m3 >= 40 and avg >= 50:
        print("Student has passed")
    else:
        print("Student has failed")

# 45. Check if a number lies between 10 and 100 (exclusive).
def check_between_10_and_100():
    num = int(input("Enter a number: "))
    if 10 < num < 100:
        print("Number lies between 10 and 100")
    else:
        print("Number does not lie between 10 and 100")

# 46. Check exam eligibility: attendance >= 75% OR medical certificate available.
def check_exam_eligibility():
    attendance = float(input("Enter attendance percentage: "))
    medical = input("Do you have a medical certificate? (yes/no): ").lower()
    if attendance >= 75 or medical == "yes":
        print("Eligible for exam")
    else:
        print("Not eligible for exam")

# 47. Validate a date (DD/MM/YYYY), including leap year logic.
def validate_date():
    date = int(input("Enter date (1-31): "))
    month = int(input("Enter month (1-12): "))
    year = int(input("Enter year: "))

    if month < 1 or month > 12 or date < 1:
        print("Invalid date")
        return

    if month in (1, 3, 5, 7, 8, 10, 12):
        max_day = 31
    elif month in (4, 6, 9, 11):
        max_day = 30
    else:
        is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
        max_day = 29 if is_leap else 28

    if date <= max_day:
        print("Valid date")
    else:
        print("Invalid date")

# 48. Check whether an email format is valid.
def validate_email():
    email = input("Enter email address: ")
    if "@" in email and "." in email and email.index("@") < email.rindex("."):
        print("Valid email format")
    else:
        print("Invalid email format")

# 49. Determine insurance eligibility (age < 60, good health, income >= 30000).
def check_insurance_eligibility():
    age = int(input("Enter your age: "))
    health = input("Enter health status (good/average/poor): ").lower()
    income = float(input("Enter your income: "))
    if age < 60 and health == "good" and income >= 30000:
        print("Eligible for insurance")
    else:
        print("Not eligible for insurance")

# 50. Check leap year using complete leap year logic.
def check_leap_year_complete():
    year = int(input("Enter a year: "))
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")


# =============================================================================
# F. INTERVIEW-LEVEL LOGIC QUESTIONS
# =============================================================================

# 51. Calculate income tax using slabs.
#     <= 2,50,000 → 0%  | <= 5,00,000 → 5%  | above → 20%
def calculate_income_tax():
    income = float(input("Enter your annual income: "))
    if income <= 250000:
        tax = 0
    elif income <= 500000:
        tax = (income - 250000) * 0.05
    else:
        tax = (income - 500000) * 0.20 + 12500
    print(f"Income tax payable: ₹{tax:.2f}")

# 52. ATM withdrawal program with balance validation.
def atm_withdrawal():
    balance = float(input("Enter your account balance: "))
    withdrawal = float(input("Enter amount to withdraw: "))
    if withdrawal > balance:
        print("Insufficient funds.")
    else:
        balance -= withdrawal
        print(f"Withdrawal successful. Remaining balance: ₹{balance:.2f}")

# 53. Check promotion eligibility (experience >= 5 yrs AND rating >= 8).
def check_promotion_eligibility():
    experience = int(input("Enter years of experience: "))
    rating = float(input("Enter performance rating (0-10): "))
    if experience >= 5 and rating >= 8:
        print("Eligible for promotion")
    else:
        print("Not eligible for promotion")

# 54. Grading system: A (>=90), B (>=80), C (below 80).
def grading_system():
    marks = float(input("Enter marks: "))
    if marks >= 90:
        print("Grade: A")
    elif marks >= 80:
        print("Grade: B")
    else:
        print("Grade: C")

# 55. Validate strong password (>= 8 chars, letter + digit + special character).
def validate_strong_password():
    password = input("Enter password: ")
    special_chars = "!@#$%^&*()-_+="
    has_alpha = any(c.isalpha() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in special_chars for c in password)
    if len(password) >= 8 and has_alpha and has_digit and has_special:
        print("Strong password ✓")
    else:
        print("Weak password. Must be 8+ chars with letters, digits, and special characters.")

# 56. Calculate delivery charges based on location and order amount.
#     Local:     >= 100 → free  | < 100 → ₹5
#     Non-local: >= 100 → ₹10  | < 100 → ₹15
def calculate_delivery_charge():
    amount = float(input("Enter order amount: "))
    location = input("Enter delivery location (local/non-local): ").lower()
    if location == "local":
        charge = 0 if amount >= 100 else 5
    else:
        charge = 10 if amount >= 100 else 15
    print(f"Delivery charge: ₹{charge}")

# 57. Determine online exam qualification based on cutoff score.
def check_exam_qualification():
    score = float(input("Enter exam score: "))
    cutoff = float(input("Enter cutoff score: "))
    if score >= cutoff:
        print("Qualified ✓")
    else:
        print("Not qualified ✗")

# 58. Movie ticket pricing based on age and show time.
#     Matinee: child(<12) → ₹5  | adult(<60) → ₹10  | senior → ₹7
#     Evening: child(<12) → ₹7  | adult(<60) → ₹12  | senior → ₹10
def movie_ticket_pricing():
    age = int(input("Enter your age: "))
    show = input("Enter show time (matinee/evening): ").lower()
    if show == "matinee":
        price = 5 if age < 12 else (10 if age < 60 else 7)
    else:
        price = 7 if age < 12 else (12 if age < 60 else 10)
    print(f"Ticket price: ₹{price}")

# 59. Determine bank account type based on balance.
def determine_account_type():
    balance = float(input("Enter your account balance: "))
    if balance < 1000:
        account_type = "Basic Savings Account"
    elif balance < 5000:
        account_type = "Regular Savings Account"
    elif balance < 10000:
        account_type = "Premium Savings Account"
    else:
        account_type = "Platinum Savings Account"
    print(f"Account type: {account_type}")

# 60. Menu-driven calculator using if-elif-else.
def menu_calculator():
    print("\n--- Calculator Menu ---")
    print("1. Add\n2. Subtract\n3. Multiply\n4. Divide")
    choice = int(input("Enter your choice (1-4): "))
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == 1:
        print(f"Result: {num1 + num2}")
    elif choice == 2:
        print(f"Result: {num1 - num2}")
    elif choice == 3:
        print(f"Result: {num1 * num2}")
    elif choice == 4:
        if num2 != 0:
            print(f"Result: {num1 / num2:.4f}")
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Invalid choice.")
