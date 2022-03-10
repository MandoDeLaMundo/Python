class BankAccount:
    # accounts = []
    def __init__(self, int_rate = .01, balance = 0):
        self.int_rate = int_rate
        self.balance = balance
        # BankAccount.accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        if self.balance < 0:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self

    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance *= 1.01
        return self

montiel_a = BankAccount()
mundo_m = BankAccount()

montiel_a.deposit(4000).deposit(80).deposit(800).withdraw(600).yield_interest().display_account_info()
mundo_m.deposit(63000).deposit(1200).withdraw(1600).withdraw(400).yield_interest().display_account_info()


