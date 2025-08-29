# ------ Exercise 1

print(("Hello World\n" * 4).strip())

# ------ Exercise 2

print(pow(99,3) * 8)

# ------ Exercise 3

name = "zakaria"
user_name = input("Enter your name:").lower()

if name == user_name:
    print("Wow! we have the same name!")
else:
    print("Your name is good but my name is better lol!")

# ------ Exercise 4

height = int(input("Enter your height in cm: "))

if height > 145:
    print("Your are tall enough to ride.")
else:
    print("Your are not tall enough to ride")

# ------ Exercise 5

my_fav_numbers = {1,5,33,53,64}

my_fav_numbers.add(12)
my_fav_numbers.add(77)

my_fav_numbers.remove(77)

friend_fav_numbers = {2, 5, 12, 77}

our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)

# ------ Exercise 6

# We can't add more integers to tuples when they created because tuples are immutable.

# ------ Exercise 7

basket = ["Banana", "Apples", "Oranges", "Blueberries"]

basket.remove("Banana")

basket.remove("Blueberries")

basket.append("Kiwi")

basket.insert(0, "Apples")

basket.count("Apples")

basket.clear()

print(basket)

# ------ Exercise 8

sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]

while "Pastrami sandwich" in sandwich_orders:
        sandwich_orders.remove("Pastrami sandwich")

finished_sandwiches = []

for sandwich in sandwich_orders:
    finished_sandwiches.append(sandwich)

for sandwich in finished_sandwiches:
    print("I made your " + sandwich)

