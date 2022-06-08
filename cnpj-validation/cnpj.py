import re

multiples = (6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2)

def valid(cnpj):
  newCnpj = cleanChars(cnpj)[:-2]

  newCnpj = lastTwoDigits(newCnpj)

  return cnpj == formatCnpj(newCnpj)

def cleanChars(cnpj):
  return re.sub(r'[^0-9]', '', cnpj)

def formatCnpj(cnpj):
  return '{}.{}.{}/{}-{}'.format(cnpj[:2], cnpj[2:5], cnpj[5:8], cnpj[8:12], cnpj[12:14])

def formula(value):
  digit = 11 - (value % 11)

  return digit if digit <= 9 else 0

def calculateDigit(cnpj):
  total = 0
  startAt = 1 if len(cnpj) != len(multiples) else 0

  for index, digit in enumerate(cnpj, startAt):
    digit = int(digit)

    digit *= multiples[index]
    total += digit

  return str(formula(total))

def lastTwoDigits(cnpj):
  while len(cnpj) != 14:
    cnpj += calculateDigit(cnpj)

  return cnpj