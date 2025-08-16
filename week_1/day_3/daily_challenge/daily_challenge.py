class Farm:
    def __init__(self, farm_name):
        self.name = farm_name
        self.animals = []
    
    def add_animal(self, animal_type,count= 1):
        for animal in self.animals:
            if animal["animal_type"] == animal_type:
                animal["count"] += count
                break
        else:
            self.animals.append({"animal_type":animal_type,"count":count})

    def get_info(self):
        string = ""
        
        for animal in self.animals:
            string += animal['animal_type'] + " : " + str(animal["count"]) +"\n"

        return f"{self.name}\n\n{string}\n\n\tE-I-E-I-0!"
    
    def get_animal_types(self):
        return self.animals.sort(key=lambda animal : animal['animal_type'])

    def get_short_info(self):
        string = "McDonald's farm has "
        for animal in self.animals:
            string += animal["animal_type"] + "s" if animal["count"] > 1 else animal["animal_type"]
            string += ", " if animal["animal_type"] == self.animals[-1]["animal_type"] else "."

        return string
            

macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())

macdonald.get_animal_types()
print(macdonald.get_info())
print(macdonald.get_short_info())

