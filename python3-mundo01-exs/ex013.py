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
            print('Entrada inválida. Por favor, digite um NÚMERO (ex: 1500.00 ou 2350).')
            time.sleep(0.5)

# --- Corpo Principal do Programa ---
print('--- CALCULADORA DE REAJUSTE SALARIAL ---')
print('Este programa calcula o novo salário com base em um percentual de aumento.')
print('=' * 50)

# Definindo a constante do percentual de aumento
PERCENTUAL_AUMENTO = 0.15 # 15%

# Coletando o salário atual do funcionário com validação
salario_atual = get_float_nao_negativo('Digite o salário atual do funcionário: R$ ')

print(f'\nCalculando reajuste de {PERCENTUAL_AUMENTO:.0%} para o salário R$ {salario_atual:.2f}...') #:.0% formata como porcentagem inteira
time.sleep(1.5)

# Calculando o valor do aumento
valor_aumento = salario_atual * PERCENTUAL_AUMENTO

# Calculando o novo salário
# Novo salário = Salário atual + Valor do aumento
# Ou de forma mais concisa: novo_salario = salario_atual * (1 + PERCENTUAL_AUMENTO)
novo_salario = salario_atual + valor_aumento

# Exibindo os resultados detalhados
print('\n--- DETALHES DO REAJUSTE ---')
print(f'Salário Original: R$ {salario_atual:.2f}')
print(f'Percentual de Aumento: {PERCENTUAL_AUMENTO:.0%}') # Exibe 15%
print(f'Valor do Aumento: R$ {valor_aumento:.2f}')
print(f'Novo Salário: R$ {novo_salario:.2f}')
print('----------------------------\n')

print('--- FIM DO PROGRAMA ---')
time.sleep(0.5)