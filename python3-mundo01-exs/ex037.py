import time

print('--- CONVERSOR DE BASES NUMÉRICAS ---')

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

# --- Corpo Principal do Programa (execução única) ---
print('\n' + '='*40)
print('NOVA CONVERSÃO DE BASE')
print('='*40)

# Solicita o número inteiro ao usuário, com validação
num = get_inteiro('Digite um número inteiro: ')

# Exibe as opções de conversão
print('\nEscolha uma das bases para conversão:')
print('[ 1 ] Converter para BINÁRIO')
print('[ 2 ] Converter para OCTAL')
print('[ 3 ] Converter para HEXADECIMAL')

# Solicita a opção de conversão, com validação para o intervalo
while True:
    opcao = get_inteiro('Sua opção: ') # Reutiliza a função de validação de inteiro
    if 1 <= opcao <= 3: # Valida se a opção está no range permitido
        break
    else:
        print('Opção inválida. Por favor, digite 1, 2 ou 3.')
        time.sleep(1)

print('\nRealizando conversão...')
time.sleep(1)

# Realiza a conversão e imprime o resultado
if opcao == 1:
    print(f'O número {num} convertido para BINÁRIO é igual a {bin(num)[2:]}.')
elif opcao == 2:
    print(f'O número {num} convertido para OCTAL é igual a {oct(num)[2:]}.')
elif opcao == 3:
    print(f'O número {num} convertido para HEXADECIMAL é igual a {hex(num)[2:]}.')

print('\n--- FIM DA CONVERSÃO ---')
time.sleep(2)