from account.account import Account
from typing import Union


class SavingsAccount(Account):
  def withdraw(self, withdraw_value: Union[int, float]):
    if self.balance < withdraw_value:
      raise ValueError(f'O valor para retirada (R$ {withdraw_value:.2f}) é maior que o saldo disponível (R$ {self.balance:.2f})')

    self.balance -= withdraw_value