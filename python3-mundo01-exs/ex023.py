import time

# --- Função de Validação de Entrada para Números Inteiros dentro de um Intervalo ---
def get_inteiro_no_intervalo(prompt, min_val, max_val):
    while True:
        try:
            valor_str = input(prompt)
            numero = int(valor_str)
            if min_val <= numero <= max_val:
                return numero
            else:
                print(f'Valor inválido! Por favor, digite um número entre {min_val} e {max_val}.')
                time.sleep(1)
        except ValueError:
            print('Entrada inválida. Por favor, digite um NÚMERO INTEIRO.')
            time.sleep(1)

# --- Corpo Principal do Programa ---
print('--- SEPARADOR DE DÍGITOS ---')
print('Este programa separará os dígitos de um número entre 0 e 9999.')
print('=' * 50)

# Define os limites como constantes
NUM_MINIMO = 0
NUM_MAXIMO = 9999

# Solicita o número ao usuário com validação de intervalo
numero_digitado = get_inteiro_no_intervalo(f'Digite um número inteiro entre {NUM_MINIMO} e {NUM_MAXIMO}: ', NUM_MINIMO, NUM_MAXIMO)

print(f'\nAnalisando o número {numero_digitado}...')
time.sleep(1.5)

# --- Separação dos dígitos usando lógica matemática (seu método, aprimorado) ---
# Garante que os números sejam exibidos formatados corretamente
unidades = numero_digitado // 1 % 10
dezenas = numero_digitado // 10 % 10
centenas = numero_digitado // 100 % 10
milhares = numero_digitado // 1000 % 10

print('\n--- DÍGITOS SEPARADOS ---')
print(f'Milhares: {milhares}')
print(f'Centenas: {centenas}')
print(f'Dezenas: {dezenas}')
print(f'Unidades: {unidades}')
print('-------------------------\n')

print('--- FIM DO PROGRAMA ---')
time.sleep(1)