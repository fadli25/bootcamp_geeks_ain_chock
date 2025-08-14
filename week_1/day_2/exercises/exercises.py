from functools import reduce
import random

# ------ Exercise 1

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

new_dict = dict( zip(keys,values))

print(new_dict)

# ------ Exercise 2

# 1-

family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}

def culc_price(age):
    if age < 3 : return 0
    elif 3 <= age < 12 : return 10
    return 15

for name, age in family.items():
    print(f"{name} have to pay: {culc_price(age)}$")

# 2-

family_cost = []

for name , age in family.items():
    family_cost.append(culc_price(age))

culc_price = reduce(lambda x,y: x + y, family_cost)

print(f"The family's cost is: {culc_price}$")

# bonus

new_family = {}

lenght = int(input("Enter the number of members in family: "))

for i in range(lenght):
    name = input("Enter the name: ")
    age = int(input("Enter the age: "))

    new_family[name] = age

print(new_family)

# ------ Exercise 3

brand = {
    "name": "Zara", 
    "creation_date": 1975,
    "creator_name": {"Amancio" ,"Ortega" ,"Gaona" },
    "type_of_clothes": {"men", "women", "children", "home"}, 
    "international_competitors":{ "Gap", "H&M", "Benetton"},
    "number_stores": 7000 ,
    "major_color":{ 
        "France": "blue", 
        "Spain": "red", 
        "US": {"pink", "green"}
    }
}

brand["number_stores"] = 2

print(f"The clients of {brand["name"]} are: ",end="")
for type in brand["type_of_clothes"]:
    print(type, end=" ")

brand["country_creation"] = "spain"

if "international_competitors" in brand:
    value = set(brand["international_competitors"])
    value.add("Desigual")
    brand["international_competitors"] = value

del brand["creation_date"]

print(list(brand["international_competitors"])[-1])

print(f"The major clothes in US: ",end="")
 
for cl in brand["major_color"]["US"]:
    print(cl, end=" ")

print(f"The amount of keys is: {len(brand)} ")

print(f"The keys of the dic is: {list(brand)}")

more_on_zara = {
    "creation_date": 1975,
    "number_stores": 10000
}

brand.update(more_on_zara)

print(f"Number of stores: {brand['number_stores']}")
# when we add the key called number_stores to the brand dict they override the old value and updated to the new because have the same name of the key

# ------ Exercise 4

def describe_city(city, country = "Morocco"):
    print(f"{city} is in {country}")

describe_city("casablanca")


# ------ Exercise 5

def compare():
    number = int(input("Enter a number between 1 and 99: "))

    while number > 99 or number < 1:
        number = int(input("Invalid input! please add number between 1 and 99: "))

    random_number = random.randint(1,99)

    if random == random_number : print("Success!")
    else :
        print(f"fail! your number is: {number}, and the random number is {random_number}")

compare()


# ------ Exercise 6

def make_shirt(size="large", text="I love Python"):
    print(f"The size of the shirt is {size} and the text is {text}")


make_shirt("xlarge","Hi")

make_shirt()

make_shirt("medium")

make_shirt("small","hello world!")

# ------ Exercise 7

def get_random_temp():
    return random.randint(-10,40)

# def get_random_temp(season):
#     match season:
#         case "winter":
#             return random.randint(-10,16)
#         case "summer":
#             return random.randint(24, 40)
#         case "fall":
#             return random.randint(-10, 32)
#         case "spring":
#             return random.randint(-10, 23)

#     return random.randint(-10,40)

def get_random_temp(month=0):
    seasons = {
    "winter": [12, 1, 2],
    "spring": [3, 4, 5],
    "summer": [6, 7, 8],
    "fall": [9, 10, 11]
    }
    for season in seasons:
        if month in seasons[season]:
            match season:
                case "winter":
                    return float(random.randint(-10,16))
                case "summer":
                    return float(random.randint(24, 40))
                case "fall":
                    return float(random.randint(-10, 32))
                case "spring":
                    return float(random.randint(-10, 23))


def main():
    # random_val = get_random_temp()

    # print(f"The temperature right now is {random_val} degrees Celsius.")

    # if random_val < 0 : print("Brrr, that’s freezing! Wear some extra layers today.")
    # elif random_val >= 0 and random_val <= 16 : print("Quite chilly! Don’t forget your coat.")
    # elif random_val > 16 and random_val <= 23 : print("Mild and pleasant! A light jacket should be fine.")
    # elif random_val > 23 and random_val <= 32 : print("Warm and sunny! Perfect for outdoor activities.")
    # else : print("It’s scorching! Stay hydrated and avoid direct sunlight for too long.")


    # season = input("Enter the season")
    user_month = int(input("Enter a mounth (1-12):"))

    season_from_month = get_random_temp(user_month)

    print(f"The temperature right now is {season_from_month} degrees Celsius.")
    if season_from_month < 0 : print("Brrr, that’s freezing! Wear some extra layers today.")
    elif season_from_month >= 0 and season_from_month <= 16 : print("Quite chilly! Don’t forget your coat.")
    elif season_from_month > 16 and season_from_month <= 23 : print("Mild and pleasant! A light jacket should be fine.")
    elif season_from_month > 23 and season_from_month <= 32 : print("Warm and sunny! Perfect for outdoor activities.")
    else : print("It’s scorching! Stay hydrated and avoid direct sunlight for too long.")

main()

# ------ Exercise 8


data = [
    {
        "question": "What is Baby Yoda's real name?",
        "answer": "Grogu"
    },
    {
        "question": "Where did Obi-Wan take Luke after his birth?",
        "answer": "Tatooine"
    },
    {
        "question": "What year did the first Star Wars movie come out?",
        "answer": "1977"
    },
    {
        "question": "Who built C-3PO?",
        "answer": "Anakin Skywalker"
    },
    {
        "question": "Anakin Skywalker grew up to be who?",
        "answer": "Darth Vader"
    },
    {
        "question": "What species is Chewbacca?",
        "answer": "Wookiee"
    }
]


def question():
    correct_answers = 0
    incorrect_answers = 0
    wrong_answers = []



    for dt in data:
        answer = input(f"{dt['question']} ").strip()
        if answer.lower() == dt["answer"].lower() :
            print("Correct!")
            correct_answers += 1
        else:
            print("Incorrect!")
            incorrect_answers += 1
            wrong_answers.append({
                "question": dt["question"],
                "answer": dt["answer"],
                "user_answer" : answer.capitalize()
            })


    for user_wrong_answers in wrong_answers:
        print(f"Question: {user_wrong_answers["question"]}")
        print(f"Your answer: {user_wrong_answers["user_answer"]}")
        print(f"wright answer: {user_wrong_answers["answer"]}")

    if incorrect_answers > 3:
        play_again = input("Do you want to play again? (Y)")

        if play_again.upper() == "Y" : question()


question()