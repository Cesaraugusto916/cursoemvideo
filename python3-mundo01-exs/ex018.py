import math
import time

# --- Função de Validação de Entrada para Números Flutuantes ---
# Não precisa ser positivo aqui, pois ângulos podem ser negativos.
def get_float_valido(prompt):
    while True:
        try:
            valor_str = input(prompt).replace(',', '.') # Aceita vírgula como decimal
            valor = float(valor_str)
            return valor
        except ValueError:
            print('Entrada inválida. Por favor, digite um NÚMERO (ex: 45 ou 90.5).')
            time.sleep(1)

# --- Corpo Principal do Programa ---
print('--- CALCULADORA DE SENO, COSSENO E TANGENTE ---')
print('Este programa calculará o seno, cosseno e tangente de um ângulo.')
print('=' * 60)

# Solicita o ângulo ao usuário com validação
angulo_graus = get_float_valido('Digite o valor do ângulo em graus: ')

print(f'\nCalculando para o ângulo {angulo_graus}°...')
time.sleep(1.5)

# Converte o ângulo de graus para radianos, pois as funções trigonométricas esperam radianos
angulo_radianos = math.radians(angulo_graus)

# Calcula seno e cosseno
seno = math.sin(angulo_radianos)
cosseno = math.cos(angulo_radianos)

print('\n--- RESULTADOS ---')
print(f'Ângulo em graus: {angulo_graus}°')
print(f'Seno: {seno:.2f}')
print(f'Cosseno: {cosseno:.2f}')

# --- Tratamento especial para a tangente ---
# Tangente é indefinida para 90° e 270° (+/- múltiplos de 180°).
# Para evitar float muito grandes ou erros em Python, verifica-se o cosseno
# Se o cosseno for muito próximo de zero, a tangente é indefinida.
# Usa math.isclose para comparação de floats, que é mais seguro que '== 0'
if math.isclose(cosseno, 0.0, abs_tol=1e-9): # abs_tol é a tolerância para considerar próximo de zero
    print('Tangente: INDEFINIDA (Cosseno muito próximo de zero)')
else:
    tangente = math.tan(angulo_radianos)
    print(f'Tangente: {tangente:.2f}')

print('-------------------\n')
print('--- FIM DO PROGRAMA ---')
time.sleep(1)