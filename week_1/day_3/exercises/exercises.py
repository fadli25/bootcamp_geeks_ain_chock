from functools import reduce

# ------ Exercise 1

class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

cat1 = Cat("mimi",5)
cat2 = Cat("rex",3)
cat3 = Cat("jak",2)

def find_oldest(*cats):
    return reduce(lambda x , y : x if x.age > y.age else y,cats)

oldest_cat = find_oldest(cat1,cat2,cat3)

# print(f"The oldest cat {oldest_cat.name}, and is {oldest_cat.age} years old.")

# ------ Exercise 2

class Dog:
    def __init__(self, name, height):
        self.name = name
        self.heigh = height

    def bark(self):
        print(f"{self.name} goes woof!")

    def jump(self):
        print(f"{self.name} jumps {self.heigh * 2} cm high!")

# davids_dog = Dog("Rex", 50)

# davids_dog.bark()
# davids_dog.jump()

# sarahs_dog = Dog("Teacup",20)

# sarahs_dog.bark()
# sarahs_dog.jump()

# if davids_dog.heigh > sarahs_dog.heigh : print(davids_dog.name)
# else : print(sarahs_dog)
# ------ Exercise 3

class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics
    
    def sing_me_a_song(self):
        for s in self.lyrics:
            print(s)

stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])

stairway.sing_me_a_song()
# ------ Exercise 4

class Zoo:
    def __init__(self, zoo_name,):
        self.name = zoo_name
        self.animals = []

    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)

    def get_animals(self):
        for animal in self.animals:
            if animal != self.animals[-1]:
                print(animal,end=", ")
            else:
                print(animal,end=".")

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)

    def sort_animals(self):
        self.animals.sort()

new_york_zoo = Zoo("new york")

while True:
    animal = input("Which animal should we add to the zoo: ")
    if animal.lower() != "exit":
        new_york_zoo.add_animal(animal)
    else:
        break

new_york_zoo.get_animals()
new_york_zoo.sort_animals()
new_york_zoo.sell_animal("cat")
new_york_zoo.get_animals()

        
