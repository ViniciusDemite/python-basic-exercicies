from account.account import Account
from typing import Union


class CheckingAccount(Account):
  def __init__(self, agency, number, balance, limit: Union[int, float] = 200):
    super().__init__(agency, number, balance)
    self._limit = limit

  @property
  def limit(self):
    return round(self._limit, 2)

  @limit.setter
  def limit(self, limit: Union[int, float]):
    self._limit = limit

  def withdraw(self, withdraw_value: Union[int, float]):
    if (self.balance + self.limit) < withdraw_value:
      raise ValueError(f'O valor para retirada (R$ {withdraw_value:.2}) excede a soma do saldo (R$ {self.balance:.2}) e limite (R$ {self.limit}) disponíveis!!!')

    self.balance -= withdraw_value