import time

print('--- SISTEMA DE APROVAÇÃO DE EMPRÉSTIMO BANCÁRIO ---')

# --- Funções de Validação de Entrada ---
# Função para obter um número float positivo
def get_float_positivo(prompt):
    while True:
        try:
            valor_str = input(prompt).replace(',', '.') # Aceita vírgula como decimal
            valor = float(valor_str)
            if valor <= 0:
                print('Valor inválido! Por favor, digite um número positivo e maior que zero.')
                time.sleep(1)
            else:
                return valor
        except ValueError:
            print('Entrada inválida. Por favor, digite um NÚMERO (ex: 150000.00).')
            time.sleep(1)

# Função para obter um número inteiro positivo (para anos)
def get_inteiro_positivo(prompt):
    while True:
        try:
            valor_str = input(prompt)
            valor = int(valor_str)
            if valor <= 0:
                print('Valor inválido! Por favor, digite um número inteiro positivo e maior que zero.')
                time.sleep(1)
            else:
                return valor
        except ValueError:
            print('Entrada inválida. Por favor, digite um NÚMERO INTEIRO (ex: 10).')
            time.sleep(1)

# --- Corpo Principal do Programa (execução única) ---
print('\n' + '='*50)
print('SIMULAÇÃO DE EMPRÉSTIMO')
print('='*50)

# --- Solicitação de Entradas com Validação ---
valor_casa = get_float_positivo('Qual o valor da casa? R$')
salario = get_float_positivo('Qual é o seu salário mensal? R$')
anos_pagar = get_inteiro_positivo('Em quantos anos você pretende pagar? ')

# --- Cálculos ---
meses_pagar = anos_pagar * 12
prestacao_mensal = valor_casa / meses_pagar
limite_salario = salario * 0.30 # 30% do salário

print(f'\nPara uma casa de R${valor_casa:.2f} a ser paga em {anos_pagar} anos ({meses_pagar} meses):')
print(f'A prestação mensal será de: R${prestacao_mensal:.2f}')
print(f'O limite de 30% do seu salário (R${salario:.2f}) é de: R${limite_salario:.2f}')
time.sleep(2) # Pequena pausa para o usuário ler

# --- Análise e Resultado ---
if prestacao_mensal > limite_salario:
    print('\n--- EMPRÉSTIMO NEGADO ---')
    print(f'Motivo: A prestação de R${prestacao_mensal:.2f} excede 30% do seu salário.')
else:
    print('\n--- EMPRÉSTIMO APROVADO! ---')
    print('Parabéns! As condições de pagamento estão dentro do seu limite salarial.')

print('\n--- PROGRAMA ENCERRADO ---')
time.sleep(2)