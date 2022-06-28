from account.account import Account
from types import Union


class SavingsAccount(Account):
  def withdraw(self, value: Union[int, float]):
    if self.balance < value:
      raise ValueError(f'O valor para retirada (R$ {value:.2}) é maior que o saldo disponível (R$ {self.balance:.2})')

    self.balance -= value