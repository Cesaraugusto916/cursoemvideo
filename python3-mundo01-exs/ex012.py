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
            print('Entrada inválida. Por favor, digite um NÚMERO (ex: 99.90 ou 150).')
            time.sleep(0.5)

# --- Corpo Principal do Programa ---
print('--- CALCULADORA DE DESCONTOS ---')
print('Este programa calcula o novo preço de um produto com um percentual de desconto.')
print('=' * 50)

# Definindo a constante do percentual de desconto
PERCENTUAL_DESCONTO = 0.05 # 5%

# Coletando o preço original do produto com validação
preco_original = get_float_nao_negativo('Digite o preço original do produto: R$ ')

print(f'\nCalculando desconto de {PERCENTUAL_DESCONTO:.0%} para o produto de R$ {preco_original:.2f}...')
time.sleep(1.5)

# Calculando o valor do desconto
valor_desconto = preco_original * PERCENTUAL_DESCONTO

# Calculando o novo preço com desconto
# Novo preço = Preço original - Valor do desconto
# Ou de forma mais concisa: novo_preco = preco_original * (1 - PERCENTUAL_DESCONTO)
novo_preco = preco_original - valor_desconto

# Exibindo os resultados detalhados
print('\n--- DETALHES DO DESCONTO ---')
print(f'Preço Original: R$ {preco_original:.2f}')
print(f'Percentual de Desconto: {PERCENTUAL_DESCONTO:.0%}') # Exibe 5%
print(f'Valor do Desconto: R$ {valor_desconto:.2f}')
print(f'Novo Preço (com desconto): R$ {novo_preco:.2f}')
print('----------------------------\n')

print('--- FIM DO PROGRAMA ---')
time.sleep(0.5)