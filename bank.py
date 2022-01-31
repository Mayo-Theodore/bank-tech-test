class BankAccount():
    def __init__(self):
        self.balance = 0
        self.credit = 0
        self.debit = 0
        self.date = ""
        self.statement = {} 

    def deposit(self, amount, date):
        #Allows client to deposit money into account
        self.balance += float(amount)
        display_balance = '%.2f' % float(self.balance)
        self.credit = float(amount)
        display_credit = '%.2f' % float(self.credit)
        self.debit = ""
        self.date = date
        self.statement[self.date] = { "date": self.date,
            "credit": display_credit,
            "debit": self.debit,
            "balance": display_balance
        }

    def withdraw(self, amount, date):
        #Allows client to withdraw money from account
        self.balance -= float(amount)
        display_balance = '%.2f' % float(self.balance)
        self.credit = ""
        self.debit = float(amount)
        display_debit = '%.2f' % float(self.debit)
        self.date = date
        self.statement[self.date] = { "date": self.date,
            "credit": self.credit,
            "debit": display_debit,
            "balance": display_balance
        }
       
    def get_statement(self):
        # Allows client to view their transanction history in chronological
        transactions = dict(reversed(list(self.statement.items())))
        for i in transactions.values():
            print("{date} || {credit} || {debit} || {balance}".format(date=i["date"], credit=i["credit"], debit=i["debit"], balance=i["balance"]))


client = BankAccount()
client.deposit('1000', '10/01/2023')
client.deposit('2000', '13/01/2023')
client.withdraw('500', '14/01/2023')
print(client.get_statement())
