import pytest
# from bank import BankAccount, InsufficientBalance, MaximumDeposit

# @pytest.fixture
# def new_bank_account():
#     '''Returns a BankAccount instance with a balance of zero'''
#     return BankAccount()

# def test_default_initial_amount(new_bank_account):
#     assert new_bank_account.balance == 0

# def test_insufficient_balance(new_bank_account):
#     '''Tests that client cannot withdraw more than balance'''
#     with pytest.raises(InsufficientBalance):
#         new_bank_account.withdraw(100, '11/01/2023')

# def test_max_deposit_limit(new_bank_account):
#     '''Tests that client cannot deposit more than limit'''
#     with pytest.raises(MaximumDeposit):
#         new_bank_account.deposit(35000, '12/01/2023')

# def test_deposit(new_bank_account):
#     '''Tests that client can deposit money'''
#     assert new_bank_account.deposit(1000, '10/01/2023') == {'10/01/2023': {'date': '10/01/2023', 'credit': '1000.00', 'debit': '', 'balance': '1000.00'}}

# def test_deposit(monkeypatch):
#     '''Mocks deposit'''
#     def mockreturn():
#         return {'10/01/2023': {'date': '10/01/2023', 'credit': '1000.00', 'debit': '', 'balance': '1000.00'}}
#     monkeypatch.setattr(BankAccount, "deposit", mockreturn)
#     mock_deposit = BankAccount.deposit()
#     assert mock_deposit == {'10/01/2023': {'date': '10/01/2023', 'credit': '1000.00', 'debit': '', 'balance': '1000.00'}}

def test_mocking_withdrawal(monkeypatch):
    import bank
    monkeypatch.setattr('bank.BankAccount.deposit', lambda: {'10/01/2023': {'date': '10/01/2023', 'credit': '1000.00', 'debit': '', 'balance': '1000.00'}})
    assert bank.BankAccount.get_statement() == ""
  


# def test_withdrawal(new_bank_account):
#     '''Tests that client can withdraw money '''
#     new_bank_account.deposit(1000, '10/01/2023')
#     assert new_bank_account.withdraw(500, '14/01/2023') == {'10/01/2023': {'date': '10/01/2023', 'credit': '1000.00', 'debit': '', 'balance': '1000.00'}, '14/01/2023': {'date': '14/01/2023', 'credit': '', 'debit': '500.00', 'balance': '500.00'}}

# def test_mocking_deposit(monkeypatch):
#     monkeypatch.setattr('bank.BankAccount.deposit', lambda: {'10/01/2023': {'date': '10/01/2023', 'credit': '1000.00', 'debit': '', 'balance': '1000.00'}})
#     assert BankAccount.deposit() ==  {'10/01/2023': {'date': '10/01/2023', 'credit': '1000.00', 'debit': '', 'balance': '1000.00'}}




# def test_get_statement(new_bank_account):
#     '''Tests that client can view their statement '''
#     new_bank_account.deposit(1000, '10/01/2023')
#     new_bank_account.deposit(2000, '13/01/2023')
#     new_bank_account.withdraw(500, '14/01/2023')
#     assert new_bank_account.balance == 2500.00
#     display_transactions = "date || credit || debit || balance \n14/01/2023 ||  || 500.00 || 2500.00 \n13/01/2023 || 2000.00 ||  || 3000.00 \n10/01/2023 || 1000.00 ||  || 1000.00"
#     assert new_bank_account.get_statement() == display_transactions

# @pytest.mark.parametrize("deposit,withdraw,expected", [
#     (30, 10, 20),
#     (20, 2, 18),
# ])
# def test_transactions(deposit, withdraw, expected):
#     my_account = BankAccount()
#     my_account.deposit(deposit, '21/01/2023')
#     my_account.withdraw(withdraw, '22/01/2023')
#     assert my_account.balance == expected