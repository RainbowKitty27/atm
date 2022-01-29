class atm:
    def __init__(self, name, amount, cardNumber):
        self.name=name
        self.amount=amount
        self.cardNumber=cardNumber
Account=atm("Sara",10000, 1096547289)
print(Account.name)
print(Account.cardNumber)
print(Account.amount)