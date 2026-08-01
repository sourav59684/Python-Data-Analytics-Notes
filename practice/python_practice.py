# =============================================================
# PYTHON PRACTICE - CORE CONCEPTS
# Covers: basics & conditionals, loops & patterns, data structures,
# functions, functional programming, file handling, exception handling
#
# Each exercise has a "Q. WAP ..." heading with the function that
# solves it. The def stays active - only the sample call below
# each function is commented out. Uncomment one call at a time
# to test it.
# =============================================================


# #############################################################
# SECTION 1 : BASICS & CONDITIONAL STATEMENTS
# #############################################################

# Q1. WAP to print a sequence of even numbers from 2 to 20.
def print_even_numbers():
    # range(start, stop, step) -> 2, 4, 6 ... 20
    print(*range(2, 21, 2))

# print_even_numbers()


# Q2. WAP to find the largest of three numbers using nested if-else.
def largest_of_three_nested():
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    num3 = int(input("Enter one more number: "))

    if num1 > num2:
        if num1 > num3:
            print("The largest number is:", num1)
        else:
            print("The largest number is:", num3)
    else:
        if num2 > num3:
            print("The largest number is:", num2)
        else:
            print("The largest number is:", num3)

# largest_of_three_nested()


# Q3. WAP to check whether a character is a vowel, a consonant, or a digit.
def check_character_type():
    char_input = input("Enter a character: ")

    if len(char_input) != 1:
        print("Please enter a single character.")
    elif char_input.isdigit():
        print("The character is a digit.")
    elif char_input in "aeiouAEIOU":
        print("The character is a vowel.")
    else:
        print("The character is a consonant.")

# check_character_type()


# #############################################################
# SECTION 2 : LOOPS & PATTERN PROGRAMMING
# #############################################################

# Q4. WAP to print the multiplication table of 2.
def multiplication_table():
    multiplier = 1
    for i in range(1, 11):
        print(2, "*", multiplier, "=", 2 * multiplier)
        multiplier += 1

# multiplication_table()


# Q5. WAP to calculate the factorial of a number.
def factorial():
    n = int(input("Enter a number: "))
    fact = 1
    for i in range(2, n + 1):
        fact = fact * i
    print("The factorial of", n, "is", fact)

# factorial()


# Q6. WAP to demonstrate the pass statement.
def demo_pass():
    # pass does nothing - it's just a placeholder
    for i in range(1, 6):
        pass
    print('hello')

# demo_pass()


# Q7. WAP to demonstrate break and else in a loop.
def demo_break_with_else():
    # the for-loop's else only runs if break was never hit
    for i in range(1, 5):
        if i == 3:
            print(i)
            break
    else:
        print(0)

# demo_break_with_else()


# Q8. WAP to print a simple number triangle.
# 1
# 1 2
# 1 2 3
def number_triangle():
    for i in range(1, 6):
        for j in range(1, i + 1):
            print(j, end=' ')
        print()

# number_triangle()


# Q9. WAP to print an inverted number triangle.
# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
def inverted_number_triangle():
    for i in range(5, 0, -1):
        for j in range(1, i + 1):
            print(j, end=' ')
        print()

# inverted_number_triangle()


# Q10. WAP to print a triangle where each row repeats its row number.
# 1
# 2 2
# 3 3 3
def repeated_row_number_triangle():
    for i in range(1, 6):
        for j in range(1, i + 1):
            print(i, end=' ')
        print()

# repeated_row_number_triangle()


# Q11. WAP to find all factors of a number and check if it is prime.
def factors_and_prime_check():
    num = int(input("Enter a number: "))
    factor_count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            print(i)
            factor_count += 1
    print("Total factors are:", factor_count)
    if factor_count == 2:
        print(num, "is a prime number")
    else:
        print(num, "is not a prime number")

# factors_and_prime_check()


# Q12. WAP to find all prime numbers from 1 to 100.
def primes_up_to_100():
    total_primes = 0
    for j in range(1, 101):
        factor_count = 0
        for i in range(1, j + 1):
            if j % i == 0:
                factor_count = factor_count + 1
        if factor_count == 2:
            print(j, "is a prime number")
            total_primes = total_primes + 1
        else:
            print(j, "is not a prime number")
    print("Total prime numbers are:", total_primes)

# primes_up_to_100()


# Q13. WAP to print a square pattern of stars.
def star_square():
    for i in range(1, 6):
        for j in range(1, 6):
            print("*", end="")
        print()

# star_square()


# Q14. WAP to print a right-angled star triangle.
def star_triangle():
    for i in range(1, 6):
        for j in range(1, i + 1):
            print("*", end="")
        print()

# star_triangle()


# Q15. WAP to print Floyd's triangle with numbers (continuously increasing).
# 1
# 23
# 456
# 78910
def floyd_triangle_numbers():
    counter = 1
    for i in range(1, 5):
        for j in range(1, i + 1):
            print(counter, end="")
            counter = counter + 1
        print()

# floyd_triangle_numbers()


# Q16. WAP to print a right-angled alphabet triangle.
# A
# AB
# ABC
def alphabet_triangle():
    # chr(65) is 'A', so chr(j + 64) gives A, B, C...
    for i in range(1, 6):
        for j in range(1, i + 1):
            print(chr(j + 64), end="")
        print()

# alphabet_triangle()


# Q17. WAP to print Floyd's triangle with alphabets (continuously increasing).
# A
# BC
# DEF
def floyd_triangle_alphabets():
    char_counter = 1
    for i in range(1, 6):
        for j in range(1, i + 1):
            print(chr(64 + char_counter), end="")
            char_counter = char_counter + 1
        print()

# floyd_triangle_alphabets()


# Q18. WAP to print an alternating binary pattern.
# 1
# 10
# 101
# 1010
def alternating_binary_pattern():
    binary_val = 1
    for i in range(1, 6):
        for j in range(1, i + 1):
            print(binary_val, end="")
            if binary_val == 1:
                binary_val = 0
            else:
                binary_val = 1
        print()

# alternating_binary_pattern()


# Q19. WAP to print a right-aligned star pyramid.
def star_pyramid():
    for i in range(1, 6):
        for s in range(5, i, -1):
            print(" ", end="")
        for j in range(1, i + 1):
            print("*", end=" ")
        print()

# star_pyramid()


# Q20. WAP to print numbers from 1 to 20 using a while loop.
def count_to_twenty():
    counter = 1
    while counter <= 20:
        print(counter)
        counter += 1

# count_to_twenty()


# Q21. WAP to take user input repeatedly until the user chooses to exit.
def input_until_exit():
    keep_going = True
    while keep_going:
        student_name = input("Enter a name: ")
        student_course = input("Enter a course: ")
        print("Saved ->", student_name, student_course)

        choice = input("Do you want to continue? (y/n): ").lower()
        if choice == 'n':
            keep_going = False

# input_until_exit()


# #############################################################
# SECTION 3 : DATA STRUCTURES (lists, tuples, sets, sorting)
# #############################################################

# Q22. WAP to find the sum of all elements in a list.
def list_sum():
    num_list = [12, 4, 5, 6, 78, 54, 21, 46, 2, 22, 95]
    print(num_list)
    print("Length of list:", len(num_list))

    total_sum = 0
    for x in num_list:
        print(x, end=" ")
        total_sum = x + total_sum
    print("\nSum of all elements in the list is:", total_sum)

# list_sum()


# Q23. WAP to find the maximum value in a list without using max().
def list_max():
    val_list = [102, 4, 5, 98, 6, 78, 54, 21, -45, 46, 2, 22, 95, 222]
    maximum_val = val_list[0]

    for index in range(0, len(val_list)):
        if val_list[index] > maximum_val:
            maximum_val = val_list[index]

    print("Maximum value from the list is:", maximum_val)

# list_max()


# Q24. WAP to demonstrate tuple slicing and iteration.
def tuple_slicing():
    my_tuple = (102, 4, 5, 98, 6, 78, 54, 21, -45, 46, 2, 22, 95, 22)
    print(my_tuple[1:6])  # elements from index 1 up to (not including) index 6
    for item in my_tuple:
        print(item)

# tuple_slicing()


# Q25. WAP to update a set and remove elements using pop().
def set_update_and_pop():
    set1 = {98, 6, 78, 54, 21, -45, 46, 2, 22, 9}
    print("set1:", set1)

    set2 = {8, 78, 5, 446, 21, 122, 9}
    print("set2:", set2)

    set1.update(set2)  # adds all elements of set2 into set1 (duplicates removed automatically)
    print("set1 after update:", set1)

    set1.pop()  # removes a random element - sets have no fixed order
    set1.pop()
    print("set1 after popping two elements:", set1)

# set_update_and_pop()


# Q26. WAP to sort a list in ascending and descending order.
def sort_a_list():
    li = [21, 354, 85, 6, 81, 2, 335, 65]

    li.sort()  # sort() changes the original list
    print("ascending:", li)

    li.sort(reverse=True)
    print("descending:", li)

    print("sorted() copy:", sorted(li))  # sorted() returns a NEW list, original stays as is

# sort_a_list()


# #############################################################
# SECTION 4 : FUNCTIONS
# #############################################################

# Q27. WAP to find the largest of three numbers using a function.
def find_largest(a, b, c):
    if a > b and a > c:
        print("The largest number is:", a)
    elif b > c:
        print("The largest number is:", b)
    else:
        print("The largest number is:", c)

# find_largest(1, 5, 8)


# Q28. WAP a function to add two numbers.
def sum_of(a, b):
    return a + b

# num1 = int(input("enter first number: "))
# num2 = int(input("enter second number: "))
# print(sum_of(num1, num2))


# Q29. WAP to check if a number is prime - Approach 1 (count all factors).
def isprime(x):
    if x > 0:
        check = 0
        for i in range(1, x + 1):
            if x % i == 0:
                check = check + 1
        if check == 2:
            print(x, "is a prime number")
        else:
            print(x, "is not a prime number")
    else:
        print("enter a number greater than 0")

# isprime(3)


# Q30. WAP to check if a number is prime - Approach 2 (stop early with return).
def checkPrime(num):
    for i in range(2, num):
        if num % i == 0:
            return "Not Prime"
    return "Prime"

# print(checkPrime(9))


# Q31. WAP to build a list of all prime numbers from 1 to 100 - Approach 3.
def primeNumbers():
    li = []
    for i in range(1, 101):
        count = 0
        for j in range(1, i + 1):
            if i % j == 0:
                count = count + 1
        if count == 2:
            print(i, "is prime")
            li.append(i)
    print(li)

# primeNumbers()


# #############################################################
# SECTION 5 : FUNCTIONAL PROGRAMMING (lambda, map, filter, reduce)
# #############################################################

from functools import reduce

# Q32. WAP a lambda function to cube a number.
cube = lambda c: c ** 3
# print(cube(2))


# Q33. WAP a lambda function to add two numbers.
sum_of_lambda = lambda x, y: x + y
# print(sum_of_lambda(81, 9))


# Q34. WAP to apply a lambda function to every element of a list using map().
li = [4, 95, 7, 3, 465, 6, 21, 321]
# print(list(map(cube, li)))


# Q35. WAP lambda functions to square a number and to check if it's even.
square = lambda s: s ** 2
even = lambda s: s % 2 == 0
# print(list(map(square, li)))
# print(list(filter(even, li)))


# Q36. WAP to combine filter, map, and reduce together.
# Step by step: keep even numbers -> square them -> add them all up
# print(reduce(sum_of_lambda, map(square, filter(even, li))))


# #############################################################
# SECTION 6 : FILE HANDLING
# #############################################################

# Q37. WAP to create a new file.
def create_file():
    my_file = open('sample_file.txt', 'w')  # 'w' creates the file (or empties it if it exists)
    my_file.close()

# create_file()


# Q38. WAP to write data into a file.
def write_to_file():
    my_file = open('sample_file.txt', 'w')
    my_file.write('akshay kumar\n')
    my_file.close()

# write_to_file()


# Q39. WAP to read data from a file.
def read_from_file():
    my_file = open('sample_file.txt', 'r')
    file_data = my_file.read()
    print(file_data)
    my_file.close()

# read_from_file()


# Q40. WAP to append data into a file without overwriting it.
def append_to_file():
    my_file = open('sample_file.txt', 'a')
    my_file.write('bunty kumar\n')
    my_file.close()

# append_to_file()


# Q41. WAP to handle files safely using the with statement.
def safe_file_handling():
    # 'with' closes the file automatically once the block ends
    with open('sample_file.txt', 'a+') as safe_file:
        safe_file.write('bunty kumar\n')
        safe_file.seek(0)  # move back to the start to read what was written
        print(safe_file.read())

# safe_file_handling()


# Q42. WAP to write and read raw bytes to a binary file.
def binary_file_demo():
    with open('sample_file.bin', 'wb+') as file:
        file.write(b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09')
        file.seek(0)
        print(file.read())

# binary_file_demo()


# Q43. WAP to save and load a Python object using pickle.
import pickle

def pickle_save_and_load_demo():
    student = {
        "name": "Sourav",
        "age": 29,
        "course": "Python"
    }

    with open("student.dat", "wb") as file:
        pickle.dump(student, file)

    with open("student.dat", "rb") as file:
        data = pickle.load(file)

    print(data)

# pickle_save_and_load_demo()


# #############################################################
# SECTION 7 : EXCEPTION HANDLING
# #############################################################

# Q44. WAP to validate age using assert inside a try-except block.
def validate_age_with_assert():
    try:
        age = int(input("enter the age: "))
        assert age > 18, "age must be 18+"
        print("welcome!")
    except AssertionError as e:
        print("error:", e)

# validate_age_with_assert()


# Q45. WAP to create and raise a custom exception class.
class AgeError(Exception):
    pass

def validate_age_with_custom_exception():
    age = int(input("enter age: "))
    if age < 18:
        raise AgeError("age should be 18+")
    print("welcome to my page")

# validate_age_with_custom_exception()

with open ('student.dat', 'rb') as file:
    print(file.read())