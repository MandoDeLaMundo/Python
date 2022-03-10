# FOUR PILLARS


# ENCAPSULATION
# --------------
# The idea that we can group code together
class CoffeeM:
    def __init__(self,name):
        self.name = name
        self.water_temp = 200
    def brew_now(self,beans):
        print(f"Using {beans}!")
        print("Brew now brown cow!")
    def clean(self):
        print("Cleaning!")


# INHERITANCE
# ------------
# The idea that we pass along attributes and methods from one class into a "sub-class" or child class
class CappuccinoM( CoffeeM ):
    def __init__(self,name):
        super().__init__(name)
        self.milk = "whole"
    def make_cappuccino(self,beans):
        super.brew_now(beans)
        print("Frothy!!!")


# POLYMORPHISM
# -------------
# Means "many forms"; the idea that a Child class can have a different version of a method than the Parent class.
class CappuccinoM( CoffeeM ):
    def __init__(self,name):
        super().__init__(name)
        self.milk = "whole"
    def make_cappuccino(self,beans):
        super.brew_now(beans)
        print("Frothy!!!")
    def clean(self):
        print("Cleaning the froth!")

# ABSTRACTION
# ------------
# An extension of 
class Barista:
    def __init__(self,name):
        self.name = name
        self.cafe = CoffeeM("Cafe")
    def make_coffee(self):
        self.cafe.brew_now()


