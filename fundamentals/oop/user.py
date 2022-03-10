class User:
    def __init__(self, name):
        self.name = name
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.account_balance}")
        return self

    def tranfer_money(self, amount, user):
        self.account -= amount
        user.account += amount
        self.display_user_balance()
        user.display_user_balance()
        return self


armando = User("Armando L Montiel")
fez = User("DarthPikaFez")
mando = User("Mando Mundo")


# guido.make_deposit(863659)
# guido.make_withdrawal(800080)
# guido.display_user_balance()
# ^^ practice


armando.make_deposit(1200).make_deposit(800).make_deposit(90).make_withdrawal(2000).display_user_balance()

fez.make_deposit(2000).make_deposit(1200).make_withdrawal(250).make_withdrawal(400).display_user_balance()

mando.make_deposit(65000).make_withdrawal(1000).make_withdrawal(1600).make_withdrawal(9000).display_user_balance().tranfer_money(1000,armando)
