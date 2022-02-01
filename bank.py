class InsufficientBalance(Exception):
    pass

class MaximumDeposit(Exception):
    pass

class BankAccount():
    def __init__(self):
        self.balance = 0
        self.credit = 0
        self.debit = 0
        self.date = ""
        self.statement = {} 
        self.display_transactions = ""

    def deposit(self, amount, date):
        MAX_DEPOSIT = 10000
        '''Allows client to deposit money into account'''
        if amount > MAX_DEPOSIT:
            raise MaximumDeposit('Sorry, the deposit limit is {}'.format(MAX_DEPOSIT))
        self.balance += amount
        display_balance = '%.2f' % float(self.balance)
        self.credit = amount
        display_credit = '%.2f' % float(self.credit)
        self.debit = ""
        self.date = date
        self.statement[self.date] = { "date": self.date,
            "credit": display_credit,
            "debit": self.debit,
            "balance": display_balance
        }
        return self.statement

    def withdraw(self, amount, date):
        '''Allows client to withdraw money from account'''
        if self.balance < amount:
            raise InsufficientBalance('Sorry, your maximum withdrawal amount is {}'.format(self.balance))
        self.balance -= amount
        display_balance = '%.2f' % float(self.balance)
        self.credit = ""
        self.debit = amount
        display_debit = '%.2f' % float(self.debit)
        self.date = date
        self.statement[self.date] = { "date": self.date,
            "credit": self.credit,
            "debit": display_debit,
            "balance": display_balance
        }
        return self.statement

    def get_statement(self):
        '''Allows client to view their transanction history in chronological'''
        transactions = dict(reversed(list(self.statement.items())))
        load_transactions = ["date", "||", "credit", "||", "debit", "||", "balance"]
        for i in transactions.values():
            load_transactions.append("\n{date} || {credit} || {debit} || {balance}".format(date=i["date"], credit=i["credit"], debit=i["debit"], balance=i["balance"]))
        self.display_transactions = " ".join(load_transactions)
        return self.display_transactions

my_bank_account = BankAccount()
my_bank_account.deposit(1000, "10/01/2023")
print(my_bank_account.withdraw(500, "14/01/2023"))
