import random

#delete wp1 if not needed
class Fighter:

    def __init__(self, name, hp, catchphrase, dex = 3, ac = 10):
        self.name = name
        self.hp = hp
        self.catchphrase = catchphrase
        # self.weapon_type = weapon_type (in __init__ weapon_type,)
        self.dex = dex
        self.ac = ac

    def attack(self, target):
        # roll random num 1-20 + dex compare to ac
        if self.hp > 0:
            x = random.randint(1,20) + self.dex
            if x == 4:
                print(f"Oops")
            # if atk roll >= ac attack hits
            if x >= target.ac:
                print(f"{self.name} hits {target.name} with {x} to hit")
                target.damage(self)
            # else attack misses
            else:
                print(f"{self.name} has missed with {x} to hit")
        return self

    def damage(self, attacker):
        # roll random num 1-6 + dex -= hp
        x = random.randint(1,6) + self.dex
        self.hp -= x
        print(f"{attacker.name} did {x} damage to {self.name}")
        # return hp
        if self.hp == 1:
            print("Finish Him!")
        elif self.hp <=0:
            print(f"{self.name} dropped to 0 HP")
        print(f"{self.name} is at {self.hp} HP")
        return self

    #CLASS METHODS
    @classmethod
    def game(self):
        # while both hp above 0 run round
        while max.hp > 0 and chris.hp > 0:
            Fighter.round()
        if max.hp<=0:
            print("Chris Won!")
            print(chris.catchphrase)
        if chris.hp<=0:
            print("Max Won!")
            print(max.catchphrase)

    def round():
        print("-" * 35)
        order = random.choice(["max", "chris"])
        #max attack
        if order == "max":
            max.attack(chris)
            chris.attack(max)
        else:
            chris.attack(max)
            max.attack(chris)


# class Master:
#     def __init__(self):
#         self.wp1 = Weapon("Scimitar", 1, 6)
#         self.wp2 = Weapon("Pistol", 2, 10)


# class Knight:
#     def __init__(self):
#         self.wp1 = Weapon("Shortsword", 1, 6)
#         self.wp2 = Weapon("Kunai", 2, 10)


# # WEAPONS

# class Weapon:
#     def __init__(self, name, cooldown, dmg_type2, dmg_type1 = 1):
#         self.name = name
#         self.cooldown = cooldown
#         self.dmg_type1 = dmg_type1
#         self.dmg_type2 = dmg_type2

#     def damage(self, attacker):
#         # roll random num 1-6 + dex -= hp
#         y = Weapon.dmg_type1()
#         z = Weapon.dmg_type2()
#         x = random.randint(y,z) + self.dex
#         self.hp -= x
#         print(f"{attacker.name} did {x} damage to {self.name}")
#         # return hp
#         if self.hp == 1:
#             print("Finish Him!")
#         elif self.hp <=0:
#             print(f"{self.name} dropped to 0 HP")
#         return self


# scimitar = Weapon("Scimitar", 1, 6)
# shortsword = Weapon("Shortsword", 1, 6)
# pistol = Weapon("Pistol", 2, 10)
# kunai = Weapon("Kunai", 2, 10)









max = Fighter("Max", 20, "asdfasdfasdfasdfasdf")
# , Master
chris = Fighter("Christian", 20, "If I end up in a break-out room, I'm leaving!")
# , Knight


Fighter.game()