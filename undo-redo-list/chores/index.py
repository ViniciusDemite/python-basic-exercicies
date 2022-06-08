chores = []
removedChores = []

def createChore():
  chore = input('Adicione uma tarefa a lista: ')
  print(end='\n\n')
  chores.append(chore)

  return None

def undoChore():
  if len(chores) == 0:
    raise ValueError('Não há items na lista!!!')

  removedChores.append(chores.pop())

  return None

def redoChore():
  if len(removedChores) == 0:
    raise ValueError('Não há items a serem refeitos!!!')

  chores.append(removedChores.pop(0))

  return None