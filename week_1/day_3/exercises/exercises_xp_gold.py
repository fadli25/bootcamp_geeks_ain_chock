import math
import random

# ------ Exercise 1

class Circle:
    def __init__(self,raduce = 1.0):
        self.raduce = raduce

    def perimeter(self):
        return self.raduce * math.pi * 2
    
    def area(self):
        return pow(self.raduce,2) * math.pi
    
    def definition(self):
        print(f"The geometrical of the circle is area : {self.area():.2f} and perimeter : {self.perimeter():.2f}")

# ------ Exercise 2

class MyList:
    def __init__(self,letter_list):
        self.letter_list = letter_list


    def reverced_list(self):
        return self.letter_list[::-1]
    
    def sorted_list(self):
        return sorted(self.letter_list)
    
    def random_list(self):
        return [random.randint(0,10) for i in range(len(self.letter_list))]


# ------ Exercise 3


class MenuManager:
    def __init__(self):
        self.menu = [
            {"name": "Soup", "price": 10, "spice": "B", "gluten": False},
            {"name": "Hamburger", "price": 15, "spice": "A", "gluten": True},
            {"name": "Salad", "price": 18, "spice": "A", "gluten": False},
            {"name": "French Fries", "price": 5, "spice": "C", "gluten": False},
            {"name": "Beef bourguignon", "price": 25, "spice": "B", "gluten": True},
        ]

    def add_item(self,name, price, spice, gluten):
        self.menu.append({
            "name" :name,
            "price" : price,
            "spice" : spice,
            "gluten" : gluten
        })
        print("the dish added Successfully!")

    def update_item(self, name, price, spice, gluten):
        for item in self.menu:
            if item["name"] == name:
                item["price"] = price
                item["spice"] = spice
                item["gluten"] = gluten
                print("dish updated successfully!")
                break
        else :
            print("the dish is not in the menu")

    def remove_item(self, name):
        for dish in self.menu:
            if dish["name"] == name : 
                self.menu.remove(dish)
                break

        
