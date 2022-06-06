"""
Criar um sistema de perguntas e respostas
"""
questions = {
  'Pergunta 1': {
    'text': 'Quanto é 2 + 2?',
    'alternatives': {
      'a': 5,
      'b': 6,
      'c': 4,
      'd': 7
    },
    'answer': 'c'
  },
  'Pergunta 2': {
    'text': 'Quanto é 5 * 5?',
    'alternatives': {
      'a': 30,
      'b': 25,
      'c': 45,
      'd': 10
    },
    'answer': 'b'
  },
}
correctAnswers = 0

for title, question in questions.items():
  print(f'{title}: {question["text"]}', 'Escolha uma das opções a baixo:', sep='\n')

  for alternative, value in question['alternatives'].items():
    print(f'({alternative}): {value}')

  answer = input('Digite sua resposta: ')

  if answer == question['answer']:
    print('Parabéns, sua resposta está correta :)')
    correctAnswers += 1
  else:
    print("Infelizmente sua resposta está errada :(")

  print()

print(f'Sua pontuação final foi: {correctAnswers}/{len(questions)}')