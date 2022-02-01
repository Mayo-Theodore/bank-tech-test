# import pytest
# from bank import BankAccount
# from mock import MagicMock 

# def test_mocking_deposit(monkeypatch):
#     monkeypatch.setattr('bank.BankAccount.deposit', lambda: {'10/01/2023': {'date': '10/01/2023', 'credit': '1000.00', 'debit': '', 'balance': '1000.00'}})
#     assert BankAccount.deposit() ==  {'10/01/2023': {'date': '10/01/2023', 'credit': '1000.00', 'debit': '', 'balance': '1000.00'}}

# def test_mocking_withdraw(monkeypatch):
#     monkeypatch.setattr('bank.BankAccount.withdraw', lambda: {'14/01/2023': {'date': '14/01/2023', 'credit': '', 'debit': '500.00', 'balance': '500.00'}})
#     assert BankAccount.withdraw() ==  {'14/01/2023': {'date': '14/01/2023', 'credit': '', 'debit': '500.00', 'balance': '500.00'}}

# # def test_get_statement(monkeypatch):
# #     monkeypatch.setattr('bank.BankAccount.deposit', lambda: {'10/01/2023': {'date': '10/01/2023', 'credit': '1000.00', 'debit': '', 'balance': '1000.00'}})
# #     monkeypatch.setattr('bank.BankAccount.withdraw', lambda: {'14/01/2023': {'date': '14/01/2023', 'credit': '', 'debit': '500.00', 'balance': '500.00'}})
 
# def test_mocking_classes(monkeypatch):
#     monkeypatch.setattr('bank.BankAccount', MagicMock(BankAccount))
#     ba = BankAccount
#     ba.deposit.return_value = 1
#     assert ba.deposit() ==  1


