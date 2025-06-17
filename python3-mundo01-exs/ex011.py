import time

# --- Função de Validação de Entrada ---
def get_float_positivo(prompt):
    """Solicita um número real positivo (maior que zero) ao usuário, validando a entrada."""
    while True:
        try:
            # Aceita tanto ponto quanto vírgula como separador decimal
            valor_str = input(prompt).replace(',', '.')
            valor = float(valor_str)
            if valor > 0: # Largura e altura devem ser maiores que zero
                return valor
            else:
                print('Entrada inválida! Por favor, digite um valor numérico positivo e maior que zero.')
                time.sleep(0.5)
        except ValueError:
            print('Entrada inválida. Por favor, digite um NÚMERO (ex: 3.5 ou 4).')
            time.sleep(0.5)

# --- Corpo Principal do Programa ---
print('--- CALCULADORA DE PINTURA DE PAREDE ---')
print('Este programa calcula a área de uma parede e a quantidade de tinta necessária.')
print('=' * 60)

# Definindo a constante de rendimento da tinta
RENDIMENTO_TINTA_POR_LITRO = 2.0 # metros quadrados por litro de tinta

# Coletando as dimensões da parede com validação
largura_parede = get_float_positivo('Digite a largura da parede em metros: ')
altura_parede = get_float_positivo('Digite a altura da parede em metros: ')

print(f'\nCalculando para uma parede de {largura_parede:.2f}m x {altura_parede:.2f}m...')
time.sleep(1.5)

# Calculando a área da parede
area_parede = largura_parede * altura_parede

# Calculando a quantidade de tinta necessária
tinta_necessaria = area_parede / RENDIMENTO_TINTA_POR_LITRO

# Exibindo os resultados
print('\n--- RESULTADOS ---')
print(f'A área da parede é de: {area_parede:.2f} m²')
print(f'Considerando que cada litro de tinta pinta {RENDIMENTO_TINTA_POR_LITRO:.1f} m²:')
print(f'Você precisará de {tinta_necessaria:.2f} litros de tinta para pintar essa parede.')
print('------------------\n')

print('--- FIM DO PROGRAMA ---')
time.sleep(0.5)