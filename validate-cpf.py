"""
Validar CPF. Abaixo temos um exemplo de como é feita a validação:

CPF = 168.995.350-09
------------------------------------------------
1 * 10 = 10           #    1 * 11 = 11 <-
6 * 9  = 54           #    6 * 10 = 60
8 * 8  = 64           #    8 *  9 = 72
9 * 7  = 63           #    9 *  8 = 72
9 * 6  = 54           #    9 *  7 = 63
5 * 5  = 25           #    5 *  6 = 30
3 * 4  = 12           #    3 *  5 = 15
5 * 3  = 15           #    5 *  4 = 20
0 * 2  = 0            #    0 *  3 = 0
                      # -> 0 *  2 = 0
         297          #             343
11 - (297 % 11) = 11  #     11 - (343 % 11) = 9
11 > 9 = 0            #
Digito 1 = 0          #   Digito 2 = 9
"""
cpf = '168.995.350-09'.replace('.', '').replace('-', '')
numbers = cpf[:-2] # 168995350

print(f'Validando CPF: {cpf}')

def calculateDigit(value):
  digit = 11 - (value % 11)
  return digit if digit <= 9 else 0

def calculateTotal(numbers):
  total = 0

  for i, number in enumerate(reversed(numbers), 2):
    total += int(number) * i

  return total

for i in range(0, 2):
  digit = str(calculateDigit(calculateTotal(numbers)))
  numbers += digit

resultCPf = numbers # 16899535009

print(f'O CPF ({cpf}) é válido :)' if cpf == resultCPf else f'O CPF ({cpf}) é inválido :(')