from client.person import Person
from account.checking_account import CheckingAccount
from account.savings_account import SavingsAccount
from types import Union


class Client(Person):
  def __init__(self, name: str, age: int, account: Union[CheckingAccount, SavingsAccount]):
    super().__init__(name, age)
    self._account = account

  @property
  def account(self):
    return self._account