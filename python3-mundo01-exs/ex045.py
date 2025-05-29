import random
import time

# --- Ponto de Melhoria 1: Representação das Jogadas ---
# Criamos uma lista onde o índice 0 não será usado,
# o índice 1 é 'PEDRA', 2 é 'PAPEL', 3 é 'TESOURA'.
# Isso facilita a associação do número da escolha com o texto.
jogadas = ['', 'PEDRA', 'PAPEL', 'TESOURA'] # O primeiro elemento é vazio para facilitar o mapeamento 1:PEDRA, 2:PAPEL, etc.

# A escolha do computador (x) e do usuário (esc) ainda será de 1 a 3
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
                    f'(1) para {jogadas[1]}\n' # Usamos a lista para imprimir a opção
                    f'(2) para {jogadas[2]}\n' # E aqui também
                    f'(3) para {jogadas[3]}\n' # E aqui
                    'Digite: '))

    # --- Ponto de Melhoria 2: Centralizar e Simplificar Impressões ---
    # Agora podemos imprimir a escolha do jogador e do computador uma única vez
    # antes de verificar o resultado.
    if 1 <= esc <= 3: # Garante que a escolha do usuário é válida (entre 1 e 3)
        print(f'Você selecionou {jogadas[esc]}')
        time.sleep(2)
        print(f'Eu pensei em {jogadas[x]}!')
        time.sleep(2)

        # --- Ponto de Melhoria 3: Simplificar a Lógica de Resultado ---
        # A lógica para determinar o vencedor pode ser mais concisa.
        # Empate é quando as escolhas são iguais.
        # Vitória é quando (PEDRA vs TESOURA), (PAPEL vs PEDRA), (TESOURA vs PAPEL).
        if esc == x:
            print('Deu EMPATE!')
        elif (esc == 1 and x == 3) or \
             (esc == 2 and x == 1) or \
             (esc == 3 and x == 2):
            print('Você GANHOU!')
        else:
            print('Você PERDEU!')

        # --- Ponto de Melhoria 4: Mensagem final de 'Tchau!' única ---
        # A mensagem de 'Tchau!' e o sleep podem ser centralizados no final do jogo.
        time.sleep(3) # Tempo de espera após o resultado
        print('Tchau!')
        time.sleep(2) # Tempo de espera final
    else:
        # Se a escolha do usuário não for entre 1 e 3
        time.sleep(2)
        print('Seleção inválida. Por favor, escolha 1, 2 ou 3.')
        time.sleep(3) # Tempo de espera para a mensagem de erro
        print('Tchau!') # Tchau também após erro
        time.sleep(2)

else:
    # Este 'else' é para quando o usuário não quer jogar (decisao != 's')
    # Já está com .lower() então lida com 'n' ou qualquer outra coisa que não 's'
    print('Ah, que pena.')
    time.sleep(2)
    print('Tchau!')
    time.sleep(2) # Reduzi o tempo de 10 para 2 segundos, que é mais amigável.