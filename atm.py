"""
Ref: https://dojopuzzles.com/problems/caixa-eletronico/

Desenvolva um programa que simule a entrega de notas quando um cliente efetuar um saque em um caixa eletrônico.
Os requisitos básicos são os seguintes:

    Entregar o menor número de notas;
    É possível sacar o valor solicitado com as notas disponíveis;
    Saldo do cliente infinito;
    Quantidade de notas infinito (pode-se colocar um valor finito de cédulas para aumentar a dificuldade do problema);
    Notas disponíveis de R$ 100,00; R$ 50,00; R$ 20,00 e R$ 10,00

Exemplos:

    Valor do Saque: R$ 30,00 – Resultado Esperado: Entregar 1 nota de R$20,00 e 1 nota de R$ 10,00.
    Valor do Saque: R$ 80,00 – Resultado Esperado: Entregar 1 nota de R$50,00 1 nota de R$ 20,00 e 1 nota de R$ 10,00. 
"""
from is_number import isNumber

availableBills = [100, 50, 20, 10, 5, 2]

def bills(bill, userWithdraw):
  quantityBills = {'quantity': 0, 'bill': bill}

  while userWithdraw >= bill:
    userWithdraw -= bill
    quantityBills['quantity'] += 1

  return quantityBills, userWithdraw

def withdraw(userWithdraw):
  withdraw = []

  for bill in availableBills:
    if userWithdraw < bill:
      continue

    quantityBills, rest = bills(bill, userWithdraw)

    userWithdraw = rest
    withdraw.append(quantityBills)

    if rest == 0 or rest == 1:
      break

  return withdraw

print('Os cálculos serão feitos com números INTEIROS')
userWithdraw = input('Valor do saque: R$ ')
print()

if not isNumber(userWithdraw):
  print('Somente números são aceitos!!')
  exit()

userWithdraw = int(userWithdraw)

withdraw = withdraw(userWithdraw)
withdrawLen = len(withdraw)

print('Saque', end=': ')

for index, quantityBill in enumerate(withdraw):
  quantity, bill = quantityBill.values()
  message = 'nota' if quantity == 1 else 'notas'

  print(f'{quantity} {message} de R$ {round(float(bill), 2)}', end=', ' if withdrawLen > 1 and index + 1 != withdrawLen else '\n')