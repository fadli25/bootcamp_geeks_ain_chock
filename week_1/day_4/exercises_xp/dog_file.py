from exercises_xp import Dog
import random

class PetDog(Dog):
    def __init__(self, name, age, weight,trained = False):
        super().__init__(name, age, weight)
        self.trained = trained

    def train(self):
        print(self.bark())
        self.trained = True
    
    def play(self, *args):
        dog_names = [name + " " for name in args]
        print(f"{dog_names} all play together.")

    def do_a_trick(self):
        my_list = ["does a barrel roll","stands on his back legs","shakes your hand","plays dead"]

        print(f"{self.name} {my_list[random.randint(0,len(my_list) - 1)]}")




