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
            print('Entrada inválida. Por favor, digite um NÚMERO (ex: 1500.00).')
            time.sleep(1)

# --- Corpo Principal do Programa ---
print('--- CALCULADORA DE AUMENTO SALARIAL ---')
print('Este programa calcula o novo salário com base nas regras da empresa.')
print('=' * 50)

# Define os limites e percentuais de aumento
LIMITE_SALARIAL = 1250.00
PERCENTUAL_AUMENTO_ALTO_SALARIO = 0.10  # 10%
PERCENTUAL_AUMENTO_BAIXO_SALARIO = 0.15 # 15%

# Solicita o salário do funcionário com validação
salario_atual = get_float_positivo('Qual o salário atual do funcionário? R$')

percentual_aplicado = 0
if salario_atual > LIMITE_SALARIAL:
    percentual_aplicado = PERCENTUAL_AUMENTO_ALTO_SALARIO
    salario_novo = salario_atual * (1 + PERCENTUAL_AUMENTO_ALTO_SALARIO) # s * 1.1
else:
    percentual_aplicado = PERCENTUAL_AUMENTO_BAIXO_SALARIO
    salario_novo = salario_atual * (1 + PERCENTUAL_AUMENTO_BAIXO_SALARIO) # s * 1.15

print('\nCalculando aumento...')
time.sleep(1.5)

print(f'\n--- RESUMO DO AUMENTO ---')
print(f'Salário Original: R${salario_atual:.2f}')
print(f'Percentual de Aumento Aplicado: {percentual_aplicado:.0%}') # Formata como porcentagem
print(f'Novo Salário: R${salario_novo:.2f}')
print('-------------------------\n')

print('--- PROGRAMA ENCERRADO ---')
time.sleep(1)