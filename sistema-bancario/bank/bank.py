from client.client import Client
from account.checking_account import CheckingAccount
from account.savings_account import SavingsAccount
from types import Union


class Bank:
  def __init__(self, name: str):
    self._name = name
    self._agencies = ['5264826', '2603056', '4152067', '2568794']
    self._clients = []
    self._current_client = None

  @property
  def name(self):
    return self._name

  @property
  def current_client(self):
    return self._current_client

  @property
  def agencies(self):
    return self._agencies

  @property
  def clients(self):
    return self._clients

  @clients.setter
  def clients(self, client: Client):
    self._clients.append(client)

  def is_authenticated(self, agency: str, cpf: str, account_number: str) -> bool:
    if agency not in self.agencies:
      return False

    try:
      self._current_client = [client for client in self.clients if client.cpf == cpf][0]

      if self.current_client.account.number != account_number:
        return False
    except IndexError:
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