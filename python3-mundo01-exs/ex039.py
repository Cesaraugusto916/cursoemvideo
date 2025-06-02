import time
from datetime import date # Importa o módulo date para obter o ano atual

print('--- SISTEMA DE ALISTAMENTO MILITAR ---')

# --- Obter o ano atual dinamicamente ---
ano_atual = date.today().year

# --- Função de Validação de Entrada para Ano de Nascimento ---
def get_ano_nascimento(prompt):
    while True:
        try:
            ano_nascimento_str = input(prompt)
            ano = int(ano_nascimento_str)

            # Validação do ano: não pode ser futuro e deve ser um ano razoável (ex: entre 1900 e o ano atual)
            if ano < 1900 or ano > ano_atual:
                print(f'Ano de nascimento inválido! Digite um ano entre 1900 e {ano_atual}.')
                time.sleep(1)
            else:
                return ano # Retorna o ano válido
        except ValueError:
            print('Entrada inválida. Por favor, digite um NÚMERO INTEIRO para o ano (ex: 2005).')
            time.sleep(1)

# --- Função para perguntar se deseja continuar ---
def perguntar_continuar():
    while True:
        try:
            opcao_str = input('\nDeseja verificar outra idade? (1 para SIM / 2 para NÃO): ').strip()
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
while True: # O programa rodará continuamente até o usuário decidir sair
    print('\n' + '='*40) # Separador para nova consulta
    print('NOVA CONSULTA DE ALISTAMENTO')
    print('='*40)

    # --- Solicitação de Entrada com Validação ---
    ano_nascimento = get_ano_nascimento('Digite seu ano de nascimento: ')

    # --- Cálculo da Idade ---
    idade = ano_atual - ano_nascimento

    print(f'\nPara quem nasceu em {ano_nascimento}, a idade atual é: {idade} anos.')
    time.sleep(1)

    # --- Lógica de Alistamento ---
    if idade < 18:
        tempo_restante = 18 - idade
        print(f'Você ainda vai se alistar ao serviço militar.')
        if tempo_restante == 1:
            print(f'Ainda falta {tempo_restante} ano para o seu alistamento.')
        else:
            print(f'Ainda faltam {tempo_restante} anos para o seu alistamento.')
        ano_alistamento = ano_nascimento + 18
        print(f'Seu alistamento será em {ano_alistamento}.')
    elif idade == 18:
        print('É HORA DE SE ALISTAR AO SERVIÇO MILITAR!')
        print('Procure a junta militar mais próxima.')
    else: # idade > 18
        tempo_passado = idade - 18
        print(f'Já passou do tempo de se alistar ao serviço militar.')
        if tempo_passado == 1:
            print(f'Já se passou {tempo_passado} ano do prazo.')
        else:
            print(f'Já se passaram {tempo_passado} anos do prazo.')
        ano_alistamento_devido = ano_nascimento + 18
        print(f'Seu alistamento deveria ter sido em {ano_alistamento_devido}.')

    # --- Pergunta se o usuário quer continuar ---
    if not perguntar_continuar(): # Se a função retornar False, sai do loop
        break

print('\n--- PROGRAMA ENCERRADO ---')
time.sleep(2)