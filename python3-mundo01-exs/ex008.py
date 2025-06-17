import time

# --- Função de Validação de Entrada ---
def get_float_nao_negativo(prompt):
    """Solicita um número real não negativo ao usuário, validando a entrada."""
    while True:
        try:
            # Aceita tanto ponto quanto vírgula como separador decimal
            valor_str = input(prompt).replace(',', '.')
            valor = float(valor_str)
            if valor >= 0:
                return valor
            else:
                print('Entrada inválida! Por favor, digite um valor não negativo.')
                time.sleep(0.5)
        except ValueError:
            print('Entrada inválida. Por favor, digite um NÚMERO (ex: 2.5 ou 100).')
            time.sleep(0.5)

# --- Corpo Principal do Programa ---
print('--- CONVERSOR DE MEDIDAS ---')
print('Este programa converte um valor em metros para outras unidades.')
print('=' * 50)

# Coletando o valor em metros com validação
metros = get_float_nao_negativo('Insira o valor em metros: ')

print(f'\nConvertendo {metros:.2f} metros para outras unidades...')
time.sleep(1.5)

# Definindo constantes para os fatores de conversão (melhora a legibilidade)
CM_POR_M = 100
MM_POR_M = 1000
KM_POR_M = 0.001 # Ou 1 / 1000

# Realizando as conversões
centimetros = metros * CM_POR_M
milimetros = metros * MM_POR_M
quilometros = metros * KM_POR_M

# Exibindo os resultados detalhados
print('\n--- RESULTADOS DA CONVERSÃO ---')
print(f'O valor que você digitou foi: {metros:.2f} metros')
print(f'Isso equivale a:')
print(f'{quilometros:.3f} quilômetros (km)') # Mais casas decimais para km, pois pode ser pequeno
print(f'{centimetros:.0f} centímetros (cm)')
print(f'{milimetros:.0f} milímetros (mm)')
print('------------------------------\n')

print('--- FIM DO PROGRAMA ---')
time.sleep(0.5)