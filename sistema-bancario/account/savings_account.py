from account.account import Account
from typing import Union


class SavingsAccount(Account):
  def withdraw(self, withdraw_value: Union[int, float]):
    if self.balance < withdraw_value:
      raise ValueError(f'O valor para retirada (R$ {withdraw_value:.2}) é maior que o saldo disponível (R$ {self.balance:.2})')

    self.balance -= withdraw_value