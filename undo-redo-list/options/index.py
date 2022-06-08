from chores.index import createChore, undoChore, redoChore

correctOptions = [1, 2, 3, 4]

def chosenOption():
  print("Escolha uma das opções:")
  print('1 - Adicionar tarefa', '2 - Desfazer tarefa', '3 - Refazer tarefa', '4 - Sair do programa', sep='\n')
  option = input('Opção: ')

  try:
    option = optionIsValid(option)

    print(end='\n\n')
  except ValueError:
    raise

  return option

def optionIsValid(option):
  errorMessage = '\n\nEssa não é uma opção válida!!!\n\n'

  if not option.isnumeric():
    raise ValueError(errorMessage)

  if int(option) not in correctOptions:
    raise ValueError(errorMessage)

  return int(option)

def action(option):
  if option == 1:
    createChore()
  elif option == 2:
    undoChore()
  elif option == 3:
    redoChore()