import time

# --- Função de Validação de Entrada ---
def get_inteiro_valido(prompt):
    """Solicita um número inteiro ao usuário, validando a entrada."""
    while True:
        try:
            valor_str = input(prompt)
            numero = int(valor_str)
            return numero
        except ValueError:
            print('Entrada inválida. Por favor, digite um NÚMERO INTEIRO.')
            time.sleep(0.5)

# --- Corpo Principal do Programa ---
print('--- ANTECESSOR E SUCESSOR ---')
print('Este programa mostra o antecessor e o sucessor de um número inteiro.')
print('=' * 50)

# Coletando o número inteiro com validação
numero_digitado = get_inteiro_valido('Digite um número inteiro: ')

print(f'\nProcessando o número {numero_digitado}...')
time.sleep(1.5)

# Calculando o antecessor e o sucessor
antecessor = numero_digitado - 1
sucessor = numero_digitado + 1

# Exibindo os resultados detalhados
print('\n--- RESULTADOS ---')
print(f'Você digitou o número: {numero_digitado}')
print(f'O **antecessor** desse número é: {antecessor}')
print(f'O **sucessor** desse número é: {sucessor}')
print('------------------\n')

print('--- FIM DO PROGRAMA ---')
time.sleep(0.5)