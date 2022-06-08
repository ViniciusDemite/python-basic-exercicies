"""
Faça uma lista de tarefas com as seguintes opções:
    adicionar tarefa
    listar tarefas
    opção de desfazer (a cada vez que chamarmos, desfaz a última ação)
    opção de refazer (a cada vez que chamarmos, refaz a última ação)
    ['Tarefa 1', 'Tarefa 2']
    ['Tarefa 1'] <- Desfazer
    ['Tarefa 1', 'Tarefa 2'] <- Refazer
    input <- Nova tarefa
"""
from chores.index import chores
from options.index import chosenOption, action

while True:
  try:
    option = chosenOption()
  except ValueError as error:
    print(error.args[0])
    continue

  if option == 4:
    exit()

  try:
    action(option)

    if len(chores) == 0:
      print('Não há items na lista!!!', end='\n\n')
      continue

    print('Tarefas:')

    for chore in chores:
      print(f'- {chore}', end='\n\n' if chore == chores[-1] else '\n')
  except ValueError as error:
    print(error.args[0], end='\n\n')
  except Exception as ex:
    print('Houve um erro inesperado', end='\n\n')