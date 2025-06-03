import time

# --- Função de Validação de Entrada para Números Flutuantes Positivos ---
def get_float_positivo(prompt):
    while True:
        try:
            valor_str = input(prompt).replace(',', '.') # Aceita vírgula como decimal
            valor = float(valor_str)
            if valor <= 0:
                print('Valor inválido! Por favor, digite um valor positivo e maior que zero.')
                time.sleep(1)
            else:
                return valor
        except ValueError:
            print('Entrada inválida. Por favor, digite um NÚMERO (ex: 150.5).')
            time.sleep(1)

# --- Corpo Principal do Programa ---
print('--- CALCULADORA DE CUSTO DE VIAGEM ---')
print('Este programa calcula o preço da passagem com base na distância percorrida.')
print('=' * 60)

# Define as constantes para as regras de preço
DISTANCIA_LIMITE = 200 # km
PRECO_CURTA_VIAGEM = 0.50 # R$ por km
PRECO_LONGA_VIAGEM = 0.45 # R$ por km

# Solicita a distância da viagem com validação
distancia_km = get_float_positivo('Qual foi a distância da viagem em Km? ')

preco_por_km = 0
if distancia_km > DISTANCIA_LIMITE:
    preco_por_km = PRECO_LONGA_VIAGEM
    preco_passagem = distancia_km * PRECO_LONGA_VIAGEM
else:
    preco_por_km = PRECO_CURTA_VIAGEM
    preco_passagem = distancia_km * PRECO_CURTA_VIAGEM

print('\nCalculando o custo da passagem...')
time.sleep(1.5)

print(f'\n--- RESUMO DA VIAGEM ---')
print(f'Distância da Viagem: {distancia_km:.1f} Km')
print(f'Tarifa Aplicada: R${preco_por_km:.2f} por Km')
print(f'Custo Total da Passagem: R${preco_passagem:.2f}')
print('------------------------\n')

print('--- PROGRAMA ENCERRADO ---')
time.sleep(1)