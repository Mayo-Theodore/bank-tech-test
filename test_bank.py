import pytest
from bank import BankAccount, InsufficientBalance, MaximumDeposit

@pytest.fixture
def new_bank_account():
    '''Returns a BankAccount instance with a zero balance'''
    return BankAccount()

def test_default_initial_amount(new_bank_account):
    assert new_bank_account.balance == 0

def test_withdraw_raises_exception_on_insufficient_balance(new_bank_account):
    with pytest.raises(InsufficientBalance):
        new_bank_account.withdraw(100, '11/01/2023')

def test_deposit_raises_exception_on_deposit_limit(new_bank_account):
    with pytest.raises(MaximumDeposit):
        new_bank_account.deposit(35000, '12/01/2023')

def test_deposit(new_bank_account):
    '''Tests that client can deposit money'''
    new_bank_account.deposit(1000, '10/01/2023')
    assert new_bank_account.balance == 1000.00
    assert new_bank_account.credit == 1000.00
    assert new_bank_account.debit == ""
    assert new_bank_account.date == '10/01/2023'

def test_withdrawal(new_bank_account):
    '''Tests that client can withdraw money '''
    new_bank_account.deposit(1000, '10/01/2023')
    new_bank_account.withdraw(500, '14/01/2023')
    assert new_bank_account.balance == 500.00
    assert new_bank_account.credit == ""
    assert new_bank_account.debit == 500.00
    assert new_bank_account.date == '14/01/2023'

def test_get_statement(new_bank_account):
    '''Tests that client can view their statement '''
    new_bank_account.deposit(1000, '10/01/2023')
    new_bank_account.deposit(2000, '13/01/2023')
    new_bank_account.withdraw(500, '14/01/2023')
    assert new_bank_account.balance == 2500.00
    display_transactions = "date || credit || debit || balance \n14/01/2023 ||  || 500.00 || 2500.00 \n13/01/2023 || 2000.00 ||  || 3000.00 \n10/01/2023 || 1000.00 ||  || 1000.00"
    assert new_bank_account.get_statement() == display_transactions

@pytest.mark.parametrize("deposit,withdraw,expected", [
    (30, 10, 20),
    (20, 2, 18),
])
def test_transactions(deposit, withdraw, expected):
    my_account = BankAccount()
    my_account.deposit(deposit, '21/01/2023')
    my_account.withdraw(withdraw, '22/01/2023')
    assert my_account.balance == expected