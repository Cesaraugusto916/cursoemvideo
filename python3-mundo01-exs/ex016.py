import time
import math # Mantém o import math para trunc

# --- Função de Validação de Entrada para Números Flutuantes ---
def get_float_valido(prompt):
    while True:
        try:
            valor_str = input(prompt).replace(',', '.') # Aceita vírgula como decimal
            valor = float(valor_str)
            return valor
        except ValueError:
            print('Entrada inválida. Por favor, digite um NÚMERO REAL (ex: 6.127 ou 8).')
            time.sleep(1)

# --- Corpo Principal do Programa ---
print('--- EXTRATOR DE PARTE INTEIRA ---')
print('Este programa lerá um número real e mostrará sua porção inteira.')
print('=' * 50)

# Solicita o número real ao usuário com validação
numero_real = get_float_valido('Digite um número real qualquer: ')

print(f'\nAnalisando o número {numero_real}...')
time.sleep(1.5)

# Calcula a porção inteira usando math.trunc()
# math.trunc() é a função mais adequada para "quebrar" o número,
# pois ela simplesmente remove a parte decimal.
parte_inteira = math.trunc(numero_real)

# --- Exibição do resultado ---
print('\n--- RESULTADO ---')
print(f'O número {numero_real} tem a parte inteira {parte_inteira}.')
print('-------------------\n')

# --- Nota sobre int() (Opcional) ---
# Para números positivos, int() também funciona:
# parte_inteira_int = int(numero_real)
# print(f'(Usando int(): {parte_inteira_int})')
# Mas para números negativos, int() arredonda para zero, enquanto trunc() apenas remove a parte decimal:
# Ex: int(-3.7) -> -3
#     trunc(-3.7) -> -3
# Ex: int(-3.1) -> -3
#     trunc(-3.1) -> -3
# Ambos se comportam igual para negativos. Para números negativos, floor() seria diferente.
# Ex: math.floor(-3.1) -> -4
# Ex: math.floor(-3.7) -> -4


print('--- FIM DO PROGRAMA ---')
time.sleep(1)