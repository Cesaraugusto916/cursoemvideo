import time

# --- Função de Validação de Entrada para Números Inteiros (geral) ---
def get_inteiro(prompt):
    while True:
        try:
            valor_str = input(prompt)
            numero = int(valor_str)
            return numero # Retorna o número inteiro válido
        except ValueError:
            print('Entrada inválida. Por favor, digite um NÚMERO INTEIRO.')
            time.sleep(1)

# --- Corpo Principal do Programa ---
print('--- MAIOR E MENOR VALORES ---')
print('Este programa lerá três números e identificará o maior e o menor entre eles.')
print('=' * 50)

# Solicita os três números inteiros com validação
n1 = get_inteiro('Digite o primeiro número inteiro: ')
n2 = get_inteiro('Digite o segundo número inteiro: ')
n3 = get_inteiro('Digite o terceiro número inteiro: ')

print('\nAnalisando os números...')
time.sleep(1.5)

# --- Identificando o maior e o menor usando funções built-in (método Pythônico) ---
menor_valor = min(n1, n2, n3)
maior_valor = max(n1, n2, n3)

print('\n--- RESULTADO ---')
print(f'O menor valor digitado foi: {menor_valor}')
print(f'O maior valor digitado foi: {maior_valor}')
print('-------------------\n')

print('--- FIM DO PROGRAMA ---')
time.sleep(1)

# --- OPCIONAL: Se você quisesse manter a ordenação como um "bônus" ---
# Basta calcular o meio_valor e imprimir:
# meio_valor = (n1 + n2 + n3) - menor_valor - maior_valor
# print(f'Os números em ordem crescente são: {menor_valor}, {meio_valor}, {maior_valor}')