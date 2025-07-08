import random
import time

# --- Melhoria 1: Representação das Jogadas (Mantida) ---
jogadas = ['', 'PEDRA', 'PAPEL', 'TESOURA']

input('Digite algo para começar\n'
      'Digite: ')
print('Inicializando...')
time.sleep(1.5)
print('Oi!')
time.sleep(1.5)

nome = input('Qual é o seu nome?\n'
             'Digite: ')
time.sleep(1.5)
print(f'Prazer te conhecer, {nome}!')
time.sleep(2)

# --- Melhoria 2: Pergunta Inicial Fora do Loop e Controle do 'while' ---
# A pergunta inicial é feita apenas uma vez.
decisao_inicial = input(f'{nome}, você quer jogar um jogo comigo?\n'
                         '(s) para sim\n'
                         '(n) para não\n'
                         'Digite: ').lower()
time.sleep(1.5)

# A variável 'jogar_novamente' agora é controlada pela resposta inicial
# E também pela pergunta de "jogar de novo" ao final de cada rodada.
jogar_novamente = (decisao_inicial == 's') # Se a decisão inicial for 's', começa jogando

if jogar_novamente:
    print('Que legal! Vamos jogar JoKenPô!')
    time.sleep(2)

# O loop 'while' agora gerencia as rodadas do jogo
while jogar_novamente:
    print('Estou pensando na minha escolha...')
    time.sleep(3)
    print('Pronto, decidi.')
    time.sleep(2)

    x = random.randint(1, 3)

    # --- Melhoria 3: Tratamento de Erro para 'int()' com um pequeno 'while' (Mantido) ---
    esc = 0
    while esc not in [1, 2, 3]:
        try:
            esc = int(input(f'{nome}, escolha a sua!\n'
                            f'(1) para {jogadas[1]}\n'
                            f'(2) para {jogadas[2]}\n'
                            f'(3) para {jogadas[3]}\n'
                            'Digite: '))
            if esc not in [1, 2, 3]:
                print('Seleção inválida. Por favor, digite 1, 2 ou 3.')
                time.sleep(1)
        except ValueError:
            print('Entrada inválida. Por favor, digite um NÚMERO (1, 2 ou 3).')
            time.sleep(1)
    time.sleep(1)

    # --- Melhoria 4: Centralizar e Simplificar Impressões (Mantida) ---
    print(f'{nome}, você selecionou {jogadas[esc]}')
    time.sleep(1.5)
    print(f'Eu pensei em {jogadas[x]}!')
    time.sleep(1.5)

    # --- Melhoria 5: Simplificar a Lógica de Resultado (Mantida) ---
    if esc == x:
        print('Deu EMPATE!')
    elif (esc == 1 and x == 3) or \
         (esc == 2 and x == 1) or \
         (esc == 3 and x == 2):
        print(f'Parabéns, {nome}! Você GANHOU!')
    else:
        print(f'Que pena, {nome}. Você PERDEU!')

    time.sleep(2)

    # --- Nova Melhoria: Pergunta "Quer jogar de novo?" ---
    # Pergunta se o usuário quer jogar outra rodada.
    jogar_novamente_input = input(f'{nome}, quer jogar de novo?\n'
                                  '(s) para sim\n'
                                  '(n) para não\n'
                                  'Digite: ').lower()
    time.sleep(1.5)

    if jogar_novamente_input == 's':
        jogar_novamente = True # Continua no loop
        print('Ótimo! Vamos para a próxima rodada!')
        time.sleep(1.5)
    elif jogar_novamente_input == 'n':
        jogar_novamente = False # Sai do loop
    else:
        print(f'Desculpe, {nome}, não entendi sua resposta. Por favor, digite "s" para sim ou "n" para não.')
        print('Assumindo que você não quer jogar de novo.') # Mensagem para evitar loop infinito em caso de entrada inválida
        jogar_novamente = False # Para garantir que saia do loop em caso de entrada inválida

# Mensagem final, seja porque o usuário não quis jogar inicialmente, ou decidiu parar.
print(f'Foi divertido jogar com você, {nome}! Tchau!')
time.sleep(2)