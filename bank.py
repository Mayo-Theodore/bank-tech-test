class BankAccount():
    def __init__(self):
        self.balance = 0
        self.credit = 0
        self.debit = 0
        self.date = ""
        self.statement = {} 

    def deposit(self, amount, date):
        self.balance += int(amount)
        self.credit = int(amount)
        self.date = date
        self.statement[self.date] = { "date": self.date,
            "credit": self.credit,
            "balance": self.balance
        }

    def withdraw(self, amount, date):
        self.balance -= int(amount)
        self.debit += int(amount)
        self.date = date
        self.statement[self.date] = { "date": self.date,
            "debit": self.debit,
            "balance": self.balance
        }
       
    def get_statement(self):
        # return "date || credit || debit || balance\n 10/01/2023 || 1000.00 || || 1000.00"
        # Reverse dictionary keys order to show transactions in reverse chronological order
        transactions = dict(reversed(list(self.statement.items())))
        for value in transactions.values():
            print(value)
            



client = BankAccount()
client.deposit('1000', '10/01/2023')
client.deposit('2000', '13/01/2023')
client.withdraw('500', '14/01/2023')
print(client.get_statement())
