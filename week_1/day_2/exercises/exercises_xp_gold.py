import random

# ------ Exercise 1

birthdays = dict()

birthdays = {
    "Alice": "1990/05/12",
    "Bob": "1985/11/23",
    "Charlie": "1992/07/09",
    "Diana": "1988/03/30",
    "Ethan": "1995/12/15"
}

print("Welcome here, You can look up the birthdays of the people in the list!")

name = input("Enter the person's name: ").strip().lower().capitalize()

birthday = birthdays[name] if name in list(birthdays) else "none"

print(f"The birthdy of {name} is {birthday}")

# ------ Exercise 2

for name, birthday in birthdays.items():
    print(f"{name} born in {birthday}")
 
name = input("Enter the person's name: ").strip().lower().capitalize()

if name in list(birthdays):
    print(f"The birthdy of {name} is {birthday}")
else:
    print(f"Sorry, we don’t have the birthday information for {name}")

# ------ Exercise 3

def cont(x):
    val = 0
    for i in range(1, x + 2):
        val += int(str(x) * i)
    print(val)

cont(3)

# ------ Exercise 4

def throw_dice():
    return random.randint(1,6)

def throw_until_doubles():

    throw_1 = throw_dice();
    throw_2 = throw_dice()

    throw_times = 1

    while throw_1 != throw_2:
        throw_1 = throw_dice()
        throw_2 = throw_dice()
        throw_times += 1

    return throw_times

throw_until_doubles()

def main():

    throw_double_times = []
    
    for i in range(0,100):
        throw_double_times.append(throw_until_doubles())

    total = sum(throw_double_times)
    avg = total / 100
    
    print(f"Total throws is: {total}")
    print(f"Average throws to reach doubles:: {avg:.02f}")

main()