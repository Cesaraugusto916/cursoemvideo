import time

# --- Função de Validação de Entrada ---
def get_numero_inteiro(prompt):
    """Solicita um número inteiro ao usuário, validando a entrada."""
    while True:
        try:
            valor_str = input(prompt)
            numero = int(valor_str) # Poderia ser float(valor_str) para aceitar decimais
            return numero
        except ValueError:
            print('Entrada inválida. Por favor, digite um NÚMERO INTEIRO válido.')
            time.sleep(0.5)

# --- Corpo Principal do Programa ---
print('--- SOMADOR DE DOIS NÚMEROS INTEIROS ---')
print('Este programa lê dois números e exibe a soma entre eles.')
print('=' * 50)

# Coletando os dois números com validação
primeiro_numero = get_numero_inteiro('Digite o primeiro número: ')
segundo_numero = get_numero_inteiro('Digite o segundo número: ')

print(f'\nCalculando a soma entre {primeiro_numero} e {segundo_numero}...')
time.sleep(1.5)

# Realizando a soma
soma_total = primeiro_numero + segundo_numero

# Exibindo o resultado
print('\n--- RESULTADO DA SOMA ---')
print(f'O primeiro número digitado foi: {primeiro_numero}')
print(f'O segundo número digitado foi: {segundo_numero}')
print(f'A soma entre {primeiro_numero} e {segundo_numero} é igual a: {soma_total}')
print('-------------------------\n')

print('--- FIM DO PROGRAMA ---')
time.sleep(0.5)