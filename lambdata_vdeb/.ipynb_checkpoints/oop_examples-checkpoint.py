"""OOP Eaxamples for module 2 """

import pandas as pd

class MyDataFrame(pd.DataFrame):
    def num_cells(self):
      return self.shape[0] * self.shape[1]


class BareMinimumClass:
    pass

class Complex:
    def __init__(self, realpart, imagpart):  #constructor
      """
      Constructor for Complex numbers.
      Complex numbers have a real part and imaginary part.
      """
      self.r = realpart  #attribute
      self.i = imagpart  #attribute

    def add(self, other_complex):
        self.r += other_complex.r
        self.i += other_complex.i

    def __repr__(self):
        return '({},{})'.format(self.r, self.i) 


class SocialMediaUser:
        def __init__(self, name, location, upvotes=0):
            self.name = str(name)
            self.location = location
            self.upvotes = int(upvotes)

        def receive_upvotes(self, num_upvotes=1):
            self.upvotes += num_upvotes

        def is_popular(self):  #is returns Boolean
            return self.upvotes > 100

class Animal:
    """General representation of animales"""
    def __init__(self, name, weight, diet_type):
        self.name = str(name)
        self.weight = float(weight)
        self.diet_type = diet_type

    def run(self):
        return 'Vroom, Vroom, I go Vroom'

    def eat(self, food):
        return 'Huge fan of that food ' + str(food)


class Sloth(Animal):
    """Representation of Sloth, a subclass of Animal"""
    def __init__(self, name, weight, diet_type, num_naps):
        super().__init__(name,weight,diet_type)  ##grabs parent class attributes, Animal
        self.num_naps = int(num_naps)
        

    def say_something(self):
        return "T h i s  i s  a  s l o t h  t y p i n g"

    # Example of overriding
    def run(self):
        return 'I am a slow sloth guy'


if __name__=='__main__':
 num1 = Complex(3, 5) #1st Complex
 num2 = Complex(4, 2) #Other Complex
 num1.add(num2) #Adds both Complexes
 print(num1.r, num1.i)
 """ This if statement Stops this from running unless actually called"""



 user1 =SocialMediaUser('Justin','Provo')
 user2 = SocialMediaUser('Nick', 'Logan', 200)
 user3 = SocialMediaUser('Carl', 'Costa Rica', 100000)
 user4 = SocialMediaUser('George Washington', 'Djibouti', 2)
 print('name: {}, is popular: {}, num upvotes: {}'.format(user4.name, user4.is_popular(), user4.upvotes))
 print('name: {}, is popular: {}, num upvotes: {}'.format(user3.name, user3.is_popular(), user3.upvotes))









