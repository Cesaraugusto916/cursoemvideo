import random
import time

# --- Função de Validação de Entrada para Números Inteiros (geral) ---
def get_inteiro(prompt):
    while True:
        try:
            valor_str = input(prompt)
            numero = int(valor_str)
            return numero  # Retorna o número inteiro válido
        except ValueError:
            print('Entrada inválida. Por favor, digite um NÚMERO INTEIRO.')
            time.sleep(1)

# --- Corpo Principal do Programa ---
print('--- JOGO DA ADIVINHAÇÃO ---')
print('Desafie o computador! Tente adivinhar o número que ele pensou.')
print('=' * 50)

# Define os limites do jogo como constantes
NUMERO_MINIMO = 0
NUMERO_MAXIMO = 5

# O computador "pensa" em um número
numero_computador = random.randint(NUMERO_MINIMO, NUMERO_MAXIMO)

print(f'Olá, usuário! Eu acabei de pensar em um número entre {NUMERO_MINIMO} e {NUMERO_MAXIMO}.')
print('Será que você consegue adivinhar qual é?\n')

# Solicita o palpite do usuário com validação de entrada e intervalo
while True:
    palpite_usuario = get_inteiro(f'Qual número eu pensei? (Entre {NUMERO_MINIMO} e {NUMERO_MAXIMO}): ')
    if NUMERO_MINIMO <= palpite_usuario <= NUMERO_MAXIMO:
        break # Sai do loop se o palpite for válido
    else:
        print(f'Ops! Seu palpite está fora do intervalo. Por favor, digite um número entre {NUMERO_MINIMO} e {NUMERO_MAXIMO}.')
        time.sleep(1)

print('\nProcessando seu palpite...')
time.sleep(2) # Pausa para criar suspense

# --- Verificação e Saída ---
if palpite_usuario == numero_computador:
    print('=============================================')
    print(f'🎉 PARABÉNS! Você acertou! Eu pensei no número {numero_computador}! 🎉')
    print('=============================================')
else:
    print('=============================================')
    print(f'Que pena! Boa tentativa, mas você errou.')
    print(f'Eu pensei no número {numero_computador}, e você digitou {palpite_usuario}.')
    print('=============================================')

print('\n--- FIM DO JOGO ---')
time.sleep(1)