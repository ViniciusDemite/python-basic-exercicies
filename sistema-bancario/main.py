"""
Exercício com Abstração, Herança, Encapsulamento e Polimorfismo
Criar um sistema bancário (extremamente simples) que tem clientes, contas e
um banco. A ideia é que o cliente tenha uma conta (poupança ou corrente) e que
possa sacar/depositar nessa conta. Contas corrente tem um limite extra. Banco
tem clientes e contas.

Dicas:
Criar classe Cliente que herda da classe Pessoa (Herança)
    Pessoa tem nome e idade (com getters)
    Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupanca)
Criar classes ContaPoupanca e ContaCorrente que herdam de Conta
    ContaCorrente deve ter um limite extra
    Contas têm agência, número da conta e saldo
    Contas devem ter método para depósito
    Conta (super classe) deve ter o método sacar abstrato (Abstração e
    polimorfismo - as subclasses que implementam o método sacar)
Criar classe Banco para AGREGAR classes de clientes e de contas (Agregação)
Banco será responsável autenticar o cliente e as contas da seguinte maneira:
    Banco tem contas e clientes (Agregação)
    * Checar se a agência é daquele banco
    * Checar se o cliente é daquele banco
    * Checar se a conta é daquele banco
Só será possível sacar se passar na autenticação do banco (descrita acima)
"""
from client.client import Client
from account.checking_account import CheckingAccount
from account.savings_account import SavingsAccount
from bank.bank import Bank
import json


bank = Bank(name='NuBank')

def create_clients_and_accounts():
  clients = import_clients()

  for client in clients:
    params = [client['account'], client['account_number'], client['balance']]

    bank.accounts = SavingsAccount(*params) if client['account'] == 'savings' else CheckingAccount(*params)

    bank.clients = Client(name=client['name'], age=client['age'], account=bank.accounts[-1])

def import_clients() -> list:
  with open('clients.json') as file:
    data = json.load(file)

  return data['clients']

while True:
  print('Bem-vindo ao sistema bancário!!', 'Digite suas informações para acessar a conta:', sep='\n', end='\n\n')

  name = input('Nome: ')
  agency = input('Agência: ')
  account_number = input('Número da conta: ')

  if not bank.is_authenticated(agency, account_number, name):
    print(f'Client ou conta não encontrados no banco {bank.name}!!!', end='\n\n')
    continue

  print('Qual operação deseja realizar?', '1 - Depósito', '2 - Saque', '3 - Sair', sep='\n', end='\n\n')

  try:
    option = int(input('Opção: '))
  except ValueError:
    print('É necessário digitar um número correspondente as opções dadas!!!')
    continue

  if option == 3:
    print('Simulação finalizada')
    break
