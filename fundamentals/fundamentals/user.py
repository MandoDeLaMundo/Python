class User:
    def __init__(self, name):
        self.name = name
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount

    def make_withdrawal(self, amount):
        self.account_balance -= amount

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.account_balance}")


armando = User("Armando L Montiel")
fez = User("DarthPikaFez")
mando = User("Mando Mundo")


# guido.make_deposit(863659)
# guido.make_withdrawal(800080)
# guido.display_user_balance()
# ^^ practice

armando.make_deposit(1200)
armando.make_deposit(800)
armando.make_deposit(90)
armando.make_withdrawal(2000)
armando.display_user_balance()

fez.make_deposit(2000)
fez.make_deposit(1200)
fez.make_withdrawal(250)
fez.make_withdrawal(400)
fez.display_user_balance()

mando.make_deposit(65000)
mando.make_withdrawal(1000)
mando.make_withdrawal(1600)
mando.make_withdrawal(9000)
mando.display_user_balance()

