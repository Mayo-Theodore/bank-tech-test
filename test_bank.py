import pytest
from bank import BankAccount, AddMoney, RemoveMoney, ViewStatement, InsufficientBalance, MaximumDeposit

@pytest.fixture
def new_bank_account():
    '''Returns a new instance of Bank Account'''
    return BankAccount()

def test_default_initial_balance(new_bank_account):
    '''New bank account has an initial balance of zero'''
    assert new_bank_account.balance == 0

def test_initial_insufficient_balance(new_bank_account):
    '''User must deposit money first before being able to withdraw'''
    with pytest.raises(InsufficientBalance):
        new_bank_account.withdraw(100, '11/01/2023')

def test_max_deposit_limit(new_bank_account):
    '''User cannot deposit more money than limit'''
    with pytest.raises(MaximumDeposit):
        new_bank_account.deposit(35000, '12/01/2023')

def test_deposit(new_bank_account):
    '''User can deposit money'''
    assert new_bank_account.deposit(1000, '10/01/2023') == {'10/01/2023': {'date': '10/01/2023', 'credit': '1000.00', 'debit': '', 'balance': '1000.00'}}

@pytest.fixture
def bank_account_with_balance():
    '''Returns an instance of bank account with a balance of 1000'''
    add_money = BankAccount()
    add_money.deposit(1000, '10/01/2023')
    return add_money

def test_withdrawal_more_than_balance(bank_account_with_balance):
    '''User cannot withdraw more than balance '''
    with pytest.raises(InsufficientBalance):
        bank_account_with_balance.withdraw(2000, '11/01/2023')

def test_withdrawal(bank_account_with_balance):
    '''User can withdraw money'''
    assert bank_account_with_balance.withdraw(500, '14/01/2023') == {'10/01/2023': {'date': '10/01/2023', 'credit': '1000.00', 'debit': '', 'balance': '1000.00'}, '14/01/2023': {'date': '14/01/2023', 'credit': '', 'debit': '500.00', 'balance': '500.00'}}

@pytest.mark.parametrize("deposit,withdraw,expected", [
    (30, 10, 20),
    (20, 2, 18),
])
def test_transactions(deposit, withdraw, expected):
    '''Users account balance corresponds to the amounts deposit and withdrawn'''
    my_account = BankAccount()
    my_account.deposit(deposit, '21/01/2023')
    my_account.withdraw(withdraw, '22/01/2023')
    assert my_account.balance == expected

@pytest.fixture
def bank_account_with_multiple_transactions():
    '''Returns an instance of bank account where deposits and withdrawals have been made'''
    multiple_transactions = BankAccount()
    multiple_transactions.deposit(1000, '10/01/2023')
    multiple_transactions.deposit(2000, '13/01/2023')
    multiple_transactions.withdraw(500, '14/01/2023')
    return multiple_transactions

def test_get_statement(bank_account_with_multiple_transactions):
    '''User can view their statement after making transactions '''
    display_transactions = "date || credit || debit || balance \n14/01/2023 ||  || 500.00 || 2500.00 \n13/01/2023 || 2000.00 ||  || 3000.00 \n10/01/2023 || 1000.00 ||  || 1000.00"
    assert bank_account_with_multiple_transactions.get_statement() == display_transactions

