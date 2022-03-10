class Pet:
    def __init__(self, name, type, tricks):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.energy = 25
        self.health = 25

    def sleep(self):
        # sleep() - increases the pets energy by 25
        self.energy += 25
        print(f"{self.name} has {self.energy} energy!")
        return self
        # pass

    def eat(self):
        # eat() - increases the pet's energy by 5 & health by 10
        self.energy += 5
        self.health += 10
        print(f"{self.name} has {self.energy} energy!")
        print(f"{self.name} is at {self.health} points of health!")
        return self
        # pass

    def play(self):
        # play() - increases the pet's health by 5
        self.health += 10
        print(f"{self.name} is at {self.health} points of health!")
        return self
        # pass

    def noise(self):
        # noise() - prints out the pet's sound
        print(f"{self.name} barks!")
        return self
        # pass

class Ninja:
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        # super().__init__(self,pet)
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

    def walk(self):
        # walks the ninja's pet invoking the play() method
        self.pet.play()
        return self
        # pass
    def feed(self):
        # feed() - feeds the ninja's pet invoking the pet eat() method
        self.pet.eat()
        return self
        # pass

    def bathe(self):
        # bathe() - cleans the ninja's pet invoking the pet noise() method
        self.pet.noise()
        return self
        # pass

remus = Pet("Remus", "dog", "paw")
mando = Ninja("Armando", "Montiel", "pizza rolls", "kibble", remus)


mando.feed().walk().bathe()