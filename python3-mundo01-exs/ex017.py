import math
import time

# --- Função de Validação de Entrada para Números Flutuantes Positivos ---
def get_float_positivo(prompt):
    while True:
        try:
            valor_str = input(prompt).replace(',', '.') # Aceita vírgula como decimal
            valor = float(valor_str)
            if valor <= 0:
                print('Valor inválido! Por favor, digite um comprimento positivo e maior que zero.')
                time.sleep(1)
            else:
                return valor
        except ValueError:
            print('Entrada inválida. Por favor, digite um NÚMERO (ex: 3.5 ou 4).')
            time.sleep(1)

# --- Corpo Principal do Programa ---
print('--- CALCULADORA DE CATETOS E HIPOTENUSA ---')
print('Este programa calcula o comprimento da hipotenusa de um triângulo retângulo.')
print('=' * 60)

# Solicita os valores dos catetos com validação
cateto_oposto = get_float_positivo('Digite o comprimento do cateto oposto: ')
cateto_adjacente = get_float_positivo('Digite o comprimento do cateto adjacente: ')

print(f'\nCalculando a hipotenusa para catetos {cateto_oposto} e {cateto_adjacente}...')
time.sleep(1.5)

# Calcula a hipotenusa usando a função math.hypot()
# Esta é a forma mais recomendada, pois é otimizada para precisão.
hipotenusa = math.hypot(cateto_oposto, cateto_adjacente)

print('\n--- RESULTADO ---')
print(f'O comprimento da hipotenusa é: {hipotenusa:.2f}')
print('-------------------\n')

# --- Nota didática (opcional, apenas para explicar o Teorema de Pitágoras) ---
# Você também poderia calcular assim (mas hypot é preferível por precisão):
# hipotenusa_alternativa = math.sqrt(cateto_oposto**2 + cateto_adjacente**2)
# print(f'(Calculado via Teorema de Pitágoras: {hipotenusa_alternativa:.2f})')

print('--- FIM DO PROGRAMA ---')
time.sleep(1)