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
            print('Entrada inválida. Por favor, digite um NÚMERO (ex: 50.00 ou 100).')
            time.sleep(0.5)

# --- Corpo Principal do Programa ---
print('--- CONVERSOR DE MOEDAS (REAL para DÓLAR) ---')
print('Este programa converte um valor em Reais para Dólares.')
print('=' * 50)

# Definindo a constante da taxa de câmbio
TAXA_CAMBIO_DOLAR = 5.48 # R$ por U$ 1.00 (considerando o valor do enunciado)

# Coletando a quantia em Reais com validação
quantia_reais = get_float_nao_negativo('Quanto dinheiro você tem na carteira? R$ ')

print(f'\nConvertendo R$ {quantia_reais:.2f} para Dólares...')
time.sleep(1.5)

# Calculando a quantidade de Dólares
quantia_dolares = quantia_reais / TAXA_CAMBIO_DOLAR

# Exibindo o resultado
print('\n--- RESULTADO DA CONVERSÃO ---')
print(f'Com R$ {quantia_reais:.2f} na carteira e considerando que U$ 1.00 = R$ {TAXA_CAMBIO_DOLAR:.2f},')
print(f'você conseguiria comprar U$ {quantia_dolares:.2f} Dólares.')
print('------------------------------\n')

print('--- FIM DO PROGRAMA ---')
time.sleep(0.5)