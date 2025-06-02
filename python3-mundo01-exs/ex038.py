import time

print('--- COMPARADOR DE DOIS NÚMEROS INTEIROS ---')

# --- Função de Validação de Entrada para Números Inteiros ---
def get_inteiro(prompt):
    while True:
        try:
            valor_str = input(prompt)
            numero = int(valor_str)
            return numero # Retorna o número inteiro válido
        except ValueError:
            print('Entrada inválida. Por favor, digite um NÚMERO INTEIRO.')
            time.sleep(1)

# --- Função para perguntar se deseja continuar ---
def perguntar_continuar():
    while True:
        try:
            opcao_str = input('\nDeseja comparar outro par de números? (1 para SIM / 2 para NÃO): ').strip()
            opcao = int(opcao_str)
            if opcao == 1:
                return True
            elif opcao == 2:
                return False
            else:
                print('Opção inválida. Digite 1 para SIM ou 2 para NÃO.')
                time.sleep(1)
        except ValueError:
            print('Entrada inválida. Por favor, digite 1 ou 2.')
            time.sleep(1)

# --- Loop Principal do Programa ---
while True:
    print('\n' + '='*40)
    print('NOVA COMPARAÇÃO')
    print('='*40)

    # --- Solicitação de Entradas com Validação ---
    num1 = get_inteiro('Digite o primeiro valor inteiro: ')
    num2 = get_inteiro('Digite o segundo valor inteiro: ')

    # --- Lógica de Comparação dos Dois Números ---
    print(f'\nComparando {num1} e {num2}...')
    time.sleep(1)

    if num1 > num2:
        print(f'O PRIMEIRO valor ({num1}) é MAIOR.')
    elif num2 > num1:
        print(f'O SEGUNDO valor ({num2}) é MAIOR.')
    else: # num1 == num2
        print('Não existe valor maior, os dois são IGUAIS.')

    # --- Pergunta se o usuário quer continuar ---
    if not perguntar_continuar():
        break

print('\n--- PROGRAMA ENCERRADO ---')
time.sleep(2)