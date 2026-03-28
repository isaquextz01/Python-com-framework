#jogo de adivinhacao
# import random

# lista_pc = ['😘','👍','🤣']
# nossa_lista = ['😘','👍','😂']
# aleatorio = random.choice(lista_pc)
# escolha_personagem = input('teste: ')
# resultado = aleatorio ==escolha_personagem

# print('ACERTOU? -', resultado)
# print('ESCOLHA DA MAQUINA: ', aleatorio)
# print('MINHA ESCOLHA:', escolha_personagem)


listas_perguntas = [
    '',
    'qual e o metal cujo simbolo quimico e au',
    'em qual continente fica o deserto do saara?',
    'qual e o autor da obra "dom quixote"?',
    'Qual é o processo peça qual as plantas se transformam luz solar em energia química?',
]

pergunta = random.choice(listas_perguntas)

print(pergunta)

lista_respostas = [
    '1 - Ouro. O símbolo vem do latim aurum.',
    '2 - no continente africano.',
    '3 - Miguel de Cervantes.',
    '4 - Fotossíntese.',
    ]




