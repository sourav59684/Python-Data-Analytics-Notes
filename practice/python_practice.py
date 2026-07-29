# #####################################################################
# # PYTHON PRACTICE PROGRAMS
# # Author: Sourav Singh
# #####################################################################

# #####################################################################
# # SECTION 1 : INPUT AND OUTPUT
# #####################################################################

# # ==========================================================
# # Q1. WAP to Print a Sequence of Even Numbers
# # ==========================================================
# # Program to print even numbers from 2 to 20 using the range function.
# print(*range(2, 21, 2))


# #####################################################################
# # SECTION 2 : CONDITIONAL STATEMENTS
# #####################################################################

# # ==========================================================
# # Q2. WAP to Find the Largest of Three Numbers
# # ==========================================================
# # Program to find the largest of three numbers using nested if-else statements.
# num1 = int(input("Enter a number: "))
# num2 = int(input("Enter another number: "))
# num3 = int(input("Enter one more number: "))

# if num1 > num2:
#     if num1 > num3:
#         print("The largest number is:", num1)
#     else:
#         print("The largest number is:", num3)
# else:
#     if num2 > num3:
#         print("The largest number is:", num2)
#     else:
#         print("The largest number is:", num3)


# # ==========================================================
# # Q3. WAP to Check if a Character is a Vowel, Consonant, or Digit
# # ==========================================================
# # Program to categorize a single character input by the user.
# char_input = input("Enter a character: ")

# if len(char_input) != 1:
#     print("Please enter a single character.")
# elif char_input.isdigit():
#     print("The character is a digit.")
# elif char_input in "aeiouAEIOU":
#     print("The character is a vowel.")
# else:
#     print("The character is a consonant.")


# #####################################################################
# # SECTION 3 : FOR LOOP PROGRAMS
# #####################################################################

# # ==========================================================
# # Q4. WAP to Print the Multiplication Table of 2
# # ==========================================================
# # Program to print a simple multiplication table using a for loop.
# multiplier = 1
# for i in range(1, 11):
#     print(2, "*", multiplier, "=", 2 * multiplier)
#     multiplier += 1


# # ==========================================================
# # Q5. WAP to Calculate the Factorial of a Number
# # ==========================================================
# # Program to calculate the factorial of a user-provided number.
# n = int(input("Enter a number: "))
# factorial = 1
# for i in range(2, n + 1):
#     factorial = factorial * i
# print("The factorial of", n, "is", factorial)


# # ==========================================================
# # Q6. WAP to Demonstrate the Pass Statement
# # ==========================================================
# # Program to show how the pass statement works as a placeholder.
# for i in range(1, 6):
#     pass
# print('hello')


# # ==========================================================
# # Q7. WAP to Demonstrate Break and Else in a Loop
# # ==========================================================
# # Program to show how a loop's else block behaves when interrupted by a break.
# for i in range(1, 5):
#     if i == 3:
#         print(i)
#         break
# else:
#     print(0)

# print(9)


# #####################################################################
# # SECTION 4 : NESTED LOOP PROGRAMS
# #####################################################################

# # ==========================================================
# # Q8. WAP to Print a Simple Number Triangle
# # ==========================================================
# # Program to print a basic right-angled triangle using numbers.
# for i in range(1, 6):
#     for j in range(1, i + 1):
#         print(j, end=' ')
#     print()


# # ==========================================================
# # Q9. WAP to Print an Inverted Number Triangle
# # ==========================================================
# # Program to print an inverted right-angled triangle using numbers.
# for i in range(5, 0, -1):
#     for j in range(1, i + 1):
#         print(j, end=' ')
#     print()


# # ==========================================================
# # Q10. WAP to Print a Triangle with Repeated Row Numbers
# # ==========================================================
# # Program to print a right-angled triangle where each row repeats its row number.
# for i in range(1, 6):
#     for j in range(1, i + 1):
#         print(i, end=' ')
#     print()


# #####################################################################
# # SECTION 5 : PRIME NUMBER PROGRAMS
# #####################################################################

# # ==========================================================
# # Q11. WAP to Find Factors and Check for Prime
# # ==========================================================
# # Program to find all factors of a number and determine if it is prime.
# num = int(input("Enter a number: "))
# factor_count = 0
# for i in range(1, num + 1):
#     if num % i == 0:
#         print(i)
#         factor_count += 1

# print("Total factors are:", factor_count)
# if factor_count == 2:
#     print(num, "is a prime number")


# # ==========================================================
# # Q12. WAP to Find All Prime Numbers from 1 to 100
# # ==========================================================
# # Program to check and count all prime numbers between 1 and 100.
# total_primes = 0
# for j in range(1, 101):
#     factor_count = 0
#     for i in range(1, j + 1):
#         if j % i == 0:
#             factor_count = factor_count + 1
            
#     if factor_count == 2:
#         print(j, "is a prime number")
#         total_primes = total_primes + 1
#     else:
#         print(j, "is not a prime number")
        
# print("Total prime numbers are:", total_primes)


# #####################################################################
# # SECTION 6 : PATTERN PROGRAMMING
# #####################################################################

# # ==========================================================
# # Q13. WAP to Print a Square Pattern of Stars
# # ==========================================================
# # Program to print a simple square grid pattern using stars.
# for i in range(1, 6):
#     for j in range(1, 6):
#         print("*", end="")
#     print()


# # ==========================================================
# # Q14. WAP to Print a Right-Angled Star Triangle
# # ==========================================================
# # Program to print a basic right-angled triangle pattern of stars.
# for i in range(1, 6):
#     for j in range(1, i + 1):
#         print("*", end="")
#     print()


# # ==========================================================
# # Q15. WAP to Print a Right-Angled Number Triangle
# # ==========================================================
# # Program to print a pattern where numbers increase across columns.
# for i in range(1, 6):
#     for j in range(1, i + 1):
#         print(j, end="")
#     print()


# # ==========================================================
# # Q16. WAP to Print a Triangle with Repeated Row Numbers
# # ==========================================================
# # Program to print a pattern where the row number is repeated.
# for i in range(1, 6):
#     for j in range(1, i + 1):
#         print(i, end="")
#     print()


# # ==========================================================
# # Q17. WAP to Print Floyd's Triangle with Numbers
# # ==========================================================
# # Program to print consecutive numbers in a triangle pattern.
# counter = 1
# for i in range(1, 5):
#     for j in range(1, i + 1):
#         print(counter, end="")
#         counter = counter + 1
#     print()


# # ==========================================================
# # Q18. WAP to Print a Right-Angled Alphabet Triangle
# # ==========================================================
# # Program to print characters starting from 'A' in a triangle shape.
# for i in range(1, 6):
#     for j in range(1, i + 1):
#         print(chr(j + 64), end="")
#     print()


# # ==========================================================
# # Q19. WAP to Print Floyd's Triangle with Alphabets
# # ==========================================================
# # Program to print consecutive characters in a triangle pattern.
# char_counter = 1
# for i in range(1, 6):
#     for j in range(1, i + 1):
#         print(chr(64 + char_counter), end="")
#         char_counter = char_counter + 1
#     print()


# # ==========================================================
# # Q20. WAP to Print an Alternating Binary Pattern
# # ==========================================================
# # Program to print alternating 1s and 0s in a triangle shape.
# binary_val = 1
# for i in range(1, 6):
#     for j in range(1, i + 1):
#         print(binary_val, end="")
#         if binary_val == 1:
#             binary_val = 0
#         else:
#             binary_val = 1
#     print()


# # ==========================================================
# # Q21. WAP to Print a Right-Aligned Star Triangle
# # ==========================================================
# # Program to print a triangle of stars aligned to the right side.
# for i in range(1, 6):
#     for s in range(5, i, -1):
#         print(" ", end="")
#     for j in range(1, i + 1):
#         print("*", end=" ")
#     print()


# #####################################################################
# # SECTION 7 : WHILE LOOP PROGRAMS
# #####################################################################

# # ==========================================================
# # Q22. WAP to Print Numbers from 1 to 20
# # ==========================================================
# # Program to print a sequence of numbers using a while loop.
# counter = 1
# while counter <= 20:
#     print(counter)
#     counter += 1


# # ==========================================================
# # Q23. WAP to Take User Input Until the User Exits
# # ==========================================================
# # Program that loops continuously to collect data until the user types 'n'.
# while True:
#     student_name = input("Enter a name: ")
#     student_course = input("Enter a course: ")
    
#     while True:
#         choice = input("Do you want to continue? (y/n): ").lower()
#         if choice == 'y':
#             break
#         elif choice == 'n':
#             exit()
#         else:
#             print("Invalid input, please enter y or n")


# #####################################################################
# # SECTION 8 : LIST PROGRAMS
# #####################################################################

# # ==========================================================
# # Q24. WAP to Find the Sum of All Elements in a List
# # ==========================================================
# # Program to iterate through a list and calculate its total sum.
# num_list = [12, 4, 5, 6, 78, 54, 21, 46, 2, 22, 95]
# print(num_list)
# print("Length of list:", len(num_list))
# print("Element at index 10:", num_list[10])

# total_sum = 0
# for x in num_list:
#     print(x, end=" ")
#     total_sum = x + total_sum
# print("\nSum of all elements in the list is:", total_sum)


# # ==========================================================
# # Q25. WAP to Find the Maximum Value in a List
# # ==========================================================
# # Program to find the largest number in a list without using max().
# val_list = [102, 4, 5, 98, 6, 78, 54, 21, -45, 46, 2, 22, 95, 222]
# maximum_val = val_list[0]

# for index in range(0, len(val_list)):
#     print(val_list[index])
#     if val_list[index] > maximum_val:
#         maximum_val = val_list[index]
        
# print("Maximum value from the list is:", maximum_val)


# #####################################################################
# # SECTION 9 : TUPLE PROGRAMS
# #####################################################################

# # ==========================================================
# # Q26. WAP to Demonstrate Tuple Slicing and Iteration
# # ==========================================================
# # Program to slice a portion of a tuple and iterate through its elements.
# my_tuple = (102, 4, 5, 98, 6, 78, 54, 21, -45, 46, 2, 22, 95, 22)
# print(my_tuple[1:6])
# for item in my_tuple:
#     print(item)


# #####################################################################
# # SECTION 10 : SET PROGRAMS
# #####################################################################

# # ==========================================================
# # Q27. WAP to Update a Set and Remove Elements
# # ==========================================================
# # Program to combine two sets and remove items using pop().
# set1 = {98, 6, 78, 54, 21, -45, 46, 2, 22, 9, 9}
# print("set1:", set1)

# set2 = {8, 78, 5, 446, 21, 122, 9}
# print("set2:", set2)

# set1.update(set2)
# print("set1 after update:", set1)
# print("set2 after update:", set2)

# set1.pop()
# set1.pop()
# print("set1 after popping two elements:", set1)


# #####################################################################
# # SECTION 11 : FUNCTIONS
# #####################################################################

# # ==========================================================
# # Q28. WAP to Find the Largest of Three Numbers using a Function
# # ==========================================================
# # Program to wrap the logic for finding the largest number into a reusable function.
# def find_largest(a, b, c):
#     if a > b and a > c:
#         print("The largest number is:", a)
#     elif b > c:
#         print("The largest number is:", b)
#     else:
#         print("The largest number is:", c)

# find_largest(1, 5, 8)


# #####################################################################
# # SECTION 12 : MINI PROJECT - TIC TAC TOE
# #####################################################################

# # ==========================================================
# # Q29. WAP to Play a Tic Tac Toe Game
# # ==========================================================
# # Program to play a full 2-player Tic Tac Toe game in the console.

# def print_board(board_list):
#     # Function to display the current state of the board in a grid format
#     print(f"\t\t {board_list[0]}   |\t{board_list[1]}  |\t{board_list[2]}")
#     print("\t\t ----------------")
#     print(f"\t\t {board_list[3]}   |\t{board_list[4]}  |\t{board_list[5]}")
#     print("\t\t ----------------")
#     print(f"\t\t {board_list[6]}   |\t{board_list[7]}  |\t{board_list[8]}")


# def play_game():
#     # Function to handle the main game logic, turns, and win detection
#     board_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#     current_player = 'x'
#     winning_combinations = [
#         (0, 1, 2), (3, 4, 5), (6, 7, 8), 
#         (0, 3, 6), (1, 4, 7), (2, 5, 8), 
#         (0, 4, 8), (2, 4, 6)
#     ]

#     while True:
#         print_board(board_list)
#         print(f"Player {current_player}'s turn: ", end="")

#         try:
#             position = int(input())
#         except ValueError:
#             print("Please enter a number between 1-9, try again.")
#             continue

#         if position in board_list:
#             board_list[position - 1] = current_player
#             game_won = False
            
#             for a, b, c in winning_combinations:
#                 if board_list[a] == board_list[b] == board_list[c]:
#                     game_won = True
#                     break

#             if game_won:
#                 print(f"Player {current_player} wins the game!")
#                 print_board(board_list)
#                 return

#             if all(isinstance(val, str) for val in board_list):
#                 print("It's a draw!")
#                 print_board(board_list)
#                 return

#             if current_player == 'x':
#                 current_player = 'o'
#             else:
#                 current_player = 'x'
#         else:
#             print("Invalid input or spot already taken, try again.")


# print("\n\t\t Welcome to Tic Tac Toe - Created by Techcoder")
# while True:
#     play_game()
#     play_again = input("\nPlay again? (y/n): ").strip().lower()
#     if play_again != 'y':
#         print("Thanks for playing!")
#         break


# #####################################################################
# # SECTION 13 : FILE HANDLING
# #####################################################################

# # ==========================================================
# # Q33. WAP to Create a File
# # ==========================================================
# # Program to create a new text file using the 'w' (write) mode.
# my_file = open('sample_file.txt', 'w')
# my_file.close()


# # ==========================================================
# # Q34. WAP to Write Data into a File
# # ==========================================================
# # Program to open a file and write a new string into it.
# my_file = open('sample_file.txt', 'w')
# my_file.write('akshay kumar\n')
# my_file.close()


# # ==========================================================
# # Q35. WAP to Read Data from a File
# # ==========================================================
# # Program to open a file in read mode and print its contents.
# my_file = open('sample_file.txt', 'r')
# file_data = my_file.read()
# print(file_data)
# my_file.close()


# # ==========================================================
# # Q36. WAP to Append Data into a File
# # ==========================================================
# # Program to append new text to an existing file without overwriting.
# my_file = open('sample_file.txt', 'a')
# my_file.write('bunty kumar\n')
# my_file.close()


# # ==========================================================
# # Q37. WAP to Use the with Statement
# # ==========================================================
# # Program to handle files safely using the 'with' context manager.
# with open('sample_file.txt', 'a+') as safe_file:
#     safe_file.write('bunty kumar\n')
#     safe_file.seek(0)
#     print(safe_file.read())

# with open ('sample_file.bin', 'wb+') as file:
#     file.write (b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09')
#     file.seek(0)
#     print(file.read())

# import pickle
# student = {
#     "name": "Sourav",
#     "age": 29,
#     "course": "Python"
# }

# with open("student.dat", "wb") as file:
#     pickle.dump(student, file)

# import pickle

# with open("student.dat", "rb") as file:
#     data = pickle.load(file)

# print(data)

# def sum_of(a,b) :
#     return a+b
# num1 = int(input("enter first number : "))
# num2 = int(input("enter second number : "))
# print (sum_of(num1, num2))

#wap to check if a number is prime or not
# def isprime(x) :
#     if x>0 :
#         check = 0
#         for i in range(1,x+1) :
#             if x%i == 0 :
#                 check = check + 1
#         if check == 2 :
#             print (x, "is a prime number")
#         else:
#             print (x, "is not a prime number")
#     else :
#         print ("enter a number greater than 0")
# isprime(3)

# def checkPrime(num):
#     for i in range(2, num):
#         if num % i == 0:
#             return "Not Prime"
#     return "Prime"

# print(checkPrime(9))

# def primeNumbers():
#     li = []
#     for i in range(1,101) :
#         count = 0
#         for j in range (1,i+1) :
#             if i%j == 0 :
#                 count = count + 1
#         if count == 2:
#             print(i , "is prime")
#             li.append(i)
#     print (li)

# # primeNumbers()

# #lambda expression
# # cube = lambda c : c**3
# # print (cube(2))

# sum_of = lambda x,y : x+y
# # print (sum_of(81,9))

# li = [4,95,7,3,465,6,21,321]
# # cube = lambda x : x**3
# # # for i in li :
# # #     print (cube(i))

# # print (list (map (cube, li)))

# square = lambda s : s**2
# even = lambda s : s%2 == 0
# # print (tuple (map   ( square, li )))
# # print (list  (filter( even  , li )))
# # print (list  (map   ( even  , li )))
# from functools import reduce
# # print (reduce (sum_of, li))
# # b = list (map(square, li))
# # print (b)
# # l = [1,2,3]
# e = list(filter (even, li))
# print (e)
# print (reduce (sum_of, map(square, filter (even, li))))

'''
mini project
store management
entity
customer (cid, cname, cadd, cmob)
product (pid, pname, price, pdesc)
orders (oid, cid ,pid, qty)
menu options:
1. add customer
2. view all customers
3. delete a customer
4. add product 
5. view all products
6. update a products
7. place an order
8. view all orders
9. view orders by cid
0. exit
'''
import pickle
#method to add info
def add_customer ():
        cus_id   = input("enter customer ID : ")
        cus_name = input("enter Customer name : ")
        cus_add  = input("enter Customer address : ")
        cus_mob  = input("enter Customer mobile : ")
        data = {cus_id : [cus_name, cus_add, cus_mob]}
        with open ('database.bin', 'ab+') as file :
            pickle.dump(data , file)
        print("\n\t data added sucessfully!\n")
        input("\nPress Enter to return to the main menu...")

#method to view customer info
def view_customer():
    print("\n\t\t Customer Details\n")
    with open("database.bin", "rb") as file:
        while True:
            try:
                record = pickle.load(file)
                print(record)
            except EOFError:
                break
        input("\nPress Enter to return to the main menu...")


#method to delete customer info
import pickle


# A METHOD TO DELETE A CUSTOMER
def delete_customer():
    file = open("database.bin", "rb")
    cid = input("Enter Customer ID To Delete : ")
    cus = dict()

    # Step 1: Read all records into one dictionary
    try:
        while True:
            data = pickle.load(file)
            cus.update(data)
    except:
        pass  # EOF reached

    file.close()

    # Step 2: Remove the customer key
    try:
        cus.pop(cid)
        print("\n\t Customer Deleted Successfully!")
    except:
        print("\n\t Customer Not Found!")

    # Step 3: OVERWRITE the file with the updated dictionary
    file = open("database.bin", "wb")
    pickle.dump(cus, file)
    file.close()

    input("\nPress Enter to return to the main menu...")

#Dashboard 
while True :
    print ("\t\t Welcome to Store Management System")
    print ("""
    1. add customer
    2. view all customers
    3. delete a customer
    4. add product
    5. view all products
    6. update a products
    7. place an order
    8. view all orders
    9. view orders by cid
    0. exit
    """)
    choice = int(input ("\t\t Choose an option to coninue : "))
    database = {}

    if choice == 0 :
            print ("\t\t Thank you!")
            break
#customer options
    if choice == 1 :
        add_customer()

    if choice == 2 :
            view_customer()

    if choice == 3 :
            delete_customer()
#product options
    if choice == 4 :
            add_product()

    if choice == 5 :
            view_product()

    if choice == 6 :
            update_product()
#order options
    if choice == 7 :
            order()

    if choice == 8 :
            view_order()

    if choice == 9 :
            order_by_cid()

    