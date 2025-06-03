import time

# --- Função de Validação de Entrada para Números Inteiros (geral) ---
def get_inteiro(prompt):
    while True:
        try:
            valor_str = input(prompt)
            numero = int(valor_str)
            return numero  # Retorna o número inteiro válido
        except ValueError:
            print('Entrada inválida. Por favor, digite um NÚMERO INTEIRO.')
            time.sleep(1)

# --- Corpo Principal do Programa ---
print('--- VERIFICADOR DE PAR OU ÍMPAR ---')
print('Este programa verifica se um número inteiro é PAR ou ÍMPAR.')
print('=' * 50)

# Solicita o número inteiro ao usuário com validação
numero_digitado = get_inteiro('Digite um número inteiro qualquer: ')

print(f'\nAnalisando o número {numero_digitado}...')
time.sleep(1.5)

# --- Verificação e Saída ---
if numero_digitado % 2 == 0:
    print(f'O número {numero_digitado} é PAR!')
else:
    print(f'O número {numero_digitado} é ÍMPAR!')

print('\n--- FIM DO PROGRAMA ---')
time.sleep(1)