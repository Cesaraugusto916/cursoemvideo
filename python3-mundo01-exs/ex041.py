import time
from datetime import date # Importa o módulo date para obter o ano atual

print('--- CLASSIFICADOR DE CATEGORIAS DE NATAÇÃO ---')

# --- Obter o ano atual dinamicamente ---
ano_atual = date.today().year

# --- Validação de Entrada para Ano de Nascimento ---
while True:
    try:
        ano_nascimento_str = input('Digite o ano de nascimento do atleta: ')
        ano = int(ano_nascimento_str)

        # Validação do ano: não pode ser futuro e deve ser um ano razoável (ex: entre 1900 e o ano atual)
        if ano < 1900 or ano > ano_atual: # Considera 1900 como um limite inferior razoável
            print(f'Ano de nascimento inválido! Digite um ano entre 1900 e {ano_atual}.')
            time.sleep(1)
        else:
            break # Sai do loop se o ano for válido
    except ValueError:
        print('Entrada inválida. Por favor, digite um NÚMERO INTEIRO para o ano (ex: 2005).')
        time.sleep(1)

# --- Cálculo da Idade ---
idade = ano_atual - ano

# --- Exibição da Idade e Classificação da Categoria ---
print(f'\nIdade do atleta: {idade} anos.')

# Lógica para determinar a categoria de acordo com o enunciado
if idade <= 9:
    print('Categoria: MIRIM')
elif idade <= 14: # Já sabemos que idade > 9
    print('Categoria: INFANTIL')
elif idade <= 19: # Já sabemos que idade > 14
    print('Categoria: JUNIOR')
elif idade <= 25: # Já sabemos que idade > 19 (e enunciado pede 'Até 25')
    print('Categoria: SÊNIOR')
else: # Idade > 25 (enunciado pede 'Acima')
    print('Categoria: MASTER')

print('\n--- FIM DA CLASSIFICAÇÃO ---')
time.sleep(2)