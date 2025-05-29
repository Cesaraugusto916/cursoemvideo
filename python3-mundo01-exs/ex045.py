import random
import time
x = random.randint(1, 3)

input('Digite algo para começar\n'
      'Digite: ')
print('Inicializando...')
time.sleep(2)
print('Oi!')
time.sleep(2)
nome = input('Qual é o seu nome?\n'
             'Digite: ')
time.sleep(2)
print(f'Prazer te conhecer, {nome}!')
time.sleep(2.5)
decisao = input('Você quer jogar um jogo comigo?\n'
                '(s) para sim\n'
                '(n) para não\n'
                'Digite: ').lower()
time.sleep(2)
if decisao == 's':
    print('Que legal! Vamos jogar JoKenPô!')
    time.sleep(3)
    print('Estou pensando na minha escolha...')
    time.sleep(4)
    print('Pronto, decidi.')
    time.sleep(3)
    esc = int(input('Escolha a sua!\n'
                    '(1) para PEDRA\n'
                    '(2) para PAPEL\n'
                    '(3) para TESOURA\n'
                    'Digite: '))

    if esc == 1 and x == 1:
        print('Você selecionou PEDRA')
        time.sleep(2)
        print(f'Eu pensei em PEDRA!')
        time.sleep(2)
        print('Deu EMPATE!')
        time.sleep(5)
        print('Tchau!')
    elif esc == 1 and x == 2:
        print('Você selecionou PEDRA')
        time.sleep(2)
        print(f'Eu pensei em PAPEL!')
        time.sleep(2)
        print('Você PERDEU!')
        time.sleep(5)
        print('Tchau!')
    elif esc == 1 and x == 3:
        print('Você selecionou PEDRA')
        time.sleep(2)
        print(f'Eu pensei em TESOURA!')
        time.sleep(2)
        print('Você GANHOU!')
        time.sleep(5)
        print('Tchau!')
    elif esc == 2 and x == 1:
        print('Você selecionou PAPEL')
        time.sleep(2)
        print(f'Eu pensei em PEDRA!')
        time.sleep(2)
        print('Você GANHOU!')
        time.sleep(5)
        print('Tchau!')
    elif esc == 2 and x == 2:
        print('Você selecionou PAPEL')
        time.sleep(2)
        print(f'Eu pensei em PAPEL!')
        time.sleep(2)
        print('Deu EMPATE!')
        time.sleep(5)
        print('Tchau!')
    elif esc == 2 and x == 3:
        print('Você selecionou PAPEL')
        time.sleep(2)
        print(f'Eu pensei em TESOURA!')
        time.sleep(2)
        print('Você PERDEU!')
        time.sleep(5)
        print('Tchau!')
    elif esc == 3 and x == 1:
        print('Você selecionou TESOURA')
        time.sleep(2)
        print(f'Eu pensei em PEDRA!')
        time.sleep(2)
        print('Você PERDEU!')
        time.sleep(5)
        print('Tchau!')
    elif esc == 3 and x == 2:
        print('Você selecionou TESOURA')
        time.sleep(2)
        print(f'Eu pensei em PAPEL!')
        time.sleep(2)
        print('Você GANHOU!')
        time.sleep(5)
        print('Tchau!')
    elif esc == 3 and x == 3:
        print('Você selecionou TESOURA')
        time.sleep(2)
        print(f'Eu pensei em TESOURA!')
        time.sleep(2)
        print('Deu EMPATE!')
        time.sleep(5)
        print('Tchau!')
    else:
        time.sleep(2)
        print('Seleção inválida')
        time.sleep(5)
        print('Tchau!')
else:
    print('Ah, que pena.')
    time.sleep(2)
    print('Tchau!')
    time.sleep(10)