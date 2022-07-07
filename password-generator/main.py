from password import Password


if __name__ == "__main__":
  while True:
    print('Preencha os dados abaixo para gerar uma senha aleatória')

    try:
      length = int(input('Tamanho da senha: '))
    except ValueError:
      print('Digite um número inteiro para o tamanho da senha!!!', end='\n\n')
      continue

    password = Password(length).create_password()

    print('A senha gerada foi: ', password, sep='\n', end='\n\n')