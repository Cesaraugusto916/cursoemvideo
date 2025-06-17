import time

# --- Funções de Validação de Entrada ---
def get_inteiro_positivo(prompt):
    """Solicita um número inteiro e positivo ao usuário."""
    while True:
        try:
            valor_str = input(prompt)
            valor = int(valor_str)
            if valor > 0:
                return valor
            else:
                print('Entrada inválida! Por favor, digite um número inteiro maior que zero.')
                time.sleep(0.5)
        except ValueError:
            print('Entrada inválida. Por favor, digite um NÚMERO INTEIRO.')
            time.sleep(0.5)

def get_float_positivo(prompt):
    """Solicita um número de ponto flutuante e positivo ao usuário."""
    while True:
        try:
            valor_str = input(prompt).replace(',', '.') # Aceita vírgula como decimal
            valor = float(valor_str)
            if valor >= 0: # Km pode ser 0 se não rodou
                return valor
            else:
                print('Entrada inválida! Por favor, digite um número maior ou igual a zero.')
                time.sleep(0.5)
        except ValueError:
            print('Entrada inválida. Por favor, digite um NÚMERO (ex: 120.5 ou 50).')
            time.sleep(0.5)

# --- Corpo Principal do Programa ---
print('--- CALCULADORA DE ALUGUEL DE CARROS ---')
print('Este programa calcula o valor total a pagar pelo aluguel de um carro.')
print('=' * 50)

# Definindo as constantes de preço
PRECO_POR_DIA = 60.00  # R$ por dia
PRECO_POR_KM = 0.15    # R$ por km rodado

# Coletando as entradas do usuário com validação
dias_alugados = get_inteiro_positivo('Quantos dias o carro foi alugado? ')
km_rodados = get_float_positivo('Quantos quilômetros foram rodados? ')

print(f'\nCalculando o valor para {dias_alugados} dias e {km_rodados} km...')
time.sleep(1.5)

# Calculando o custo total
custo_dias = PRECO_POR_DIA * dias_alugados
custo_km = PRECO_POR_KM * km_rodados
total_a_pagar = custo_dias + custo_km

# Exibindo o resultado
print('\n--- RESUMO DO ALUGUEL ---')
print(f'Dias alugados: {dias_alugados}')
print(f'Quilômetros rodados: {km_rodados:.2f}')
print(f'Custo por dias (R$ {PRECO_POR_DIA:.2f}/dia): R$ {custo_dias:.2f}')
print(f'Custo por KM (R$ {PRECO_POR_KM:.2f}/km): R$ {custo_km:.2f}')
print(f'O TOTAL A PAGAR é: R$ {total_a_pagar:.2f}')
print('---------------------------\n')

print('--- FIM DO PROGRAMA ---')
time.sleep(0.5)