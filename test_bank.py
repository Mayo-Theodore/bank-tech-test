import pytest
from bank import BankAccount

def test_deposit():
    #Tests that client can deposit money
    client = BankAccount()
    client.deposit('1000', '10/01/2023')
    assert client.balance == 1000
    assert client.credit == 1000
    assert client.debit == 0
    assert client.date == '10/01/2023'

def test_withdrawal():
    # Tests that client can withdraw money 
    client = BankAccount()
    client.deposit('1000', '10/01/2023')
    client.withdraw('500', '14/01/2023')
    assert client.balance == 500
    assert client.credit == 0
    assert client.debit == 500
    assert client.date == '14/01/2023'

def test_get_statement():
    #Tests that client can view their statement
    client = BankAccount()
    client.deposit('1000', '10/01/2023')
    client.deposit('2000', '13/01/2023')
    client.withdraw('500', '14/01/2023')
    assert client.get_statement() == "date || credit || debit || balance"
"14/01/2023 || || 500.00 || 2500.00"
"13/01/2023 || 2000.00 || || 3000.00"
"10/01/2023 || 1000.00 || || 1000.00"