# Supposed to combine this with bankaccount


class BankAccount:
    accounts = []
    # def __init__(self, int_rate = .01, balance = 0):
    def __init__ (self,int_rate,balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if(self.balance - amount) >= 0:
            self.balance -= amount
        # if self.balance < 0:
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self

    def display_account_info(self):
        return f"{self.balance}"
        # print(f"Balance: {self.balance}")
        # return self

    def yield_interest(self):
        if self.balance > 0:
            # self.balance *= 1.01
            self.balance += (self.balance * self.int_rate)
        return self

    @classmethod
    def print_all_accounts(cls):
        for account in cls.accounts:
            account.display_account_info()


class User:
    def __init__(self, name):
        self.name = name
        # self.account = 0
        self.account = {
            "checking" : BankAccount(.02,1000),
            "savings" : BankAccount(.05,3000)
        }
        
# ---DELETE
    # def make_deposit(self, amount):
    #     self.account += amount
    #     return self

    # def make_withdrawal(self, amount):
    #     self.account -= amount
    #     return self
# DELETE---


    def display_user_balance(self):
        # print(f"User: {self.name}, Savings Balance: {self.savings}, Checking Balance: {self.checking}")
        print(f"User: {self.name}, Checking Balance: {self.account['checking'].display_account_info()}")
        print(f"User: {self.name}, Savings Balance: {self.account['savings'].display_account_info()}")
        return self

    def tranfer_money(self, amount, user):
        self.account -= amount
        user.account += amount
        self.display_user_balance()
        user.display_user_balance()





armando = User("Armando L Montiel")
fez = User("DarthPikaFez")
mando = User("Mando Mundo")



# armando.make_deposit(1200).make_deposit(800).make_deposit(90).make_withdrawal(2000).display_user_balance()

# fez.make_deposit(2000).make_deposit(1200).make_withdrawal(250).make_withdrawal(400).display_user_balance()

# mando.make_deposit(65000).make_withdrawal(1000).make_withdrawal(1600).make_withdrawal(9000).display_user_balance().tranfer_money(1000,armando)


armando.account['checking'].deposit(100)
armando.display_user_balance()