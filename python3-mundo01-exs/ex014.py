import time

# --- Função de Validação de Entrada ---
def get_float_valido(prompt):
    """Solicita um número real ao usuário, validando a entrada."""
    while True:
        try:
            # Aceita tanto ponto quanto vírgula como separador decimal
            valor_str = input(prompt).replace(',', '.')
            valor = float(valor_str)
            return valor
        except ValueError:
            print('Entrada inválida. Por favor, digite um NÚMERO (ex: 25.5 ou 0).')
            time.sleep(0.5)

# --- Corpo Principal do Programa ---
print('--- CONVERSOR DE TEMPERATURAS ---')
print('Este programa converte uma temperatura de Celsius para Fahrenheit.')
print('=' * 50)

# Coletando a temperatura em Celsius com validação
temperatura_celsius = get_float_valido('Digite a temperatura em Celsius (ºC): ')

print(f'\nConvertendo {temperatura_celsius:.2f}ºC para Fahrenheit...')
time.sleep(1.5)

# Definindo constantes para a fórmula (melhora a legibilidade)
FATOR_MULTIPLICACAO = 9 / 5
INCREMENTO_FAHRENHEIT = 32

# Calculando a temperatura em Fahrenheit
temperatura_fahrenheit = (temperatura_celsius * FATOR_MULTIPLICACAO) + INCREMENTO_FAHRENHEIT

# Exibindo o resultado
print('\n--- RESULTADO DA CONVERSÃO ---')
print(f'A temperatura de {temperatura_celsius:.2f}ºC equivale a {temperatura_fahrenheit:.2f}ºF.')
print('------------------------------\n')

print('--- FIM DO PROGRAMA ---')
time.sleep(0.5)