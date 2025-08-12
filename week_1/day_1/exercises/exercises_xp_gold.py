import random

# ------ Exercise 1

spring = {3,4,5}
summer = {6,7,8}
fall = {9,10,11}
winter = {12,1,2}

user_month = int(input("Enter a month (1-12): "))

while user_month not in range(1, 12):
    user_month = int(input("Invalid month. Please enter a month (1-12): "))

if user_month in spring:
    print("It's spring!")
elif user_month in summer:
    print("It's summer!")
elif user_month in fall:
    print("It's fall!")
else:
    print("It's winter!")

# ------ Exercise 2

for i in range(1,21):
    print(i)

for i in range(1,21):
    if i % 2 == 0: print(i)

# ------ Exercise 3

name = "zakaria"

user_name = input("Enter your name: ").lower()

while user_name != name:
    user_name = input("Incorrect name. Please try again: ").lower()

print("Welcome, " + name + "!")

# ------ Exercise 4

names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']

name = input("Enter a name: ").capitalize()

if name in names:
    print("The index ", names.index(name))

# ------ Exercise 5

numbers = []

for i in range(1,4):
    number = int(input("Enter a number: "))
    numbers.append(number)

print("The greatest number is: ", max(numbers))


# ------ Exercise 6

user_number = int(input("Enter a number between 1 and 9: "))

while user_number not in range(1,10):
    user_number = int(input("Invalid input! please enter a number between 1 and 9: "))

random_number = random.randint(1,9)

if user_number == random_number: print("Winner!")
else: print("Better luck next time.")
