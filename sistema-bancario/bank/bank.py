from client.client import Client
from account.checking_account import CheckingAccount
from account.savings_account import SavingsAccount
from types import Union


class Bank:
  def __init__(self, name: str):
    self._name = name
    self._clients = []
    self._accounts = []

  @property
  def name(self):
    return self._name

  @property
  def clients(self):
    return self._clients

  @clients.setter
  def clients(self, client: Client):
    self._clients.append(client)

  @property
  def accounts(self):
    return self._accounts

  @accounts.setter
  def accounts(self, account: Union[CheckingAccount, SavingsAccount]):
    self._accounts.append(account)

  def is_authenticated(self, agency: str, client_name: str, account_number: str) -> bool:
    account = [account for account in self.accounts if account.agency == agency and account.number == account_number]
    client = [client for client in self.clients if client.name == client_name]

    if len(client) != 1 or len(account) != 1:
      return False

    return True

  def list_clients(self):
    for client in self.clients:
      print(f'Nome: {client.name}', f'Idade: {client.age}', f'Conta: {client.account}', sep='\n', end='\n\n')

  def list_accounts(self):
    for account in self.accounts:
      is_checking_account = isinstance(account, CheckingAccount)
      
      print(f'Agência: {account.agency}')
      print(f'Número da conta: {account.number}')
      print(f'Saldo: {account.balance}', end = '\n' if not is_checking_account else '\n\n')

      if isinstance(account, CheckingAccount):
        print(f'Limite: {account.limit}', end = '\n\n')