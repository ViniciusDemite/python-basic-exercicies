from cnpj import valid

cnpjs = ['04.252.011/0001-10', '40.688.134/0001-61', '71.506.168/0001-11', '12.544.992/0001-05', '40.688.134/0001-81']

for cnpj in cnpjs:
  print(f'CNPJ: {cnpj}')

  if not valid(cnpj):
    print('O cnpj não é válido!!', end='\n\n')
    continue

  print('O cnpj é válido!!', end='\n\n')