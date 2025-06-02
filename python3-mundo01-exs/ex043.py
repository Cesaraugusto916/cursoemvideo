import time

print('--- CALCULADORA DE ÍNDICE DE MASSA CORPORAL (IMC) ---')

# --- Validação de Entrada para Peso ---
# Loop para garantir que o peso seja um número válido e positivo
while True:
    try:
        p_str = input('Digite o seu peso (kg): ').replace(',', '.') # Permite vírgula como separador decimal
        p = float(p_str)
        if p <= 0:
            print('Peso inválido! O peso deve ser um valor positivo.')
            time.sleep(1) # Pequena pausa para a mensagem ser lida
        else:
            break # Sai do loop se o peso for válido
    except ValueError:
        print('Entrada inválida. Por favor, digite um NÚMERO para o peso (ex: 70.5).')
        time.sleep(1)

# --- Validação de Entrada para Altura ---
# Loop para garantir que a altura seja um número válido e positivo, e diferente de zero
while True:
    try:
        a_str = input('Digite a sua altura (m): ').replace(',', '.') # Permite vírgula como separador decimal
        a = float(a_str)
        if a <= 0:
            print('Altura inválida! A altura deve ser um valor positivo e diferente de zero.')
            time.sleep(1)
        else:
            break # Sai do loop se a altura for válida
    except ValueError:
        print('Entrada inválida. Por favor, digite um NÚMERO para a altura (ex: 1.75).')
        time.sleep(1)

# --- Cálculo do IMC ---
imc = p / (a ** 2)

# --- Exibição do Resultado e Status do IMC ---
print(f'\nSeu IMC é: {imc:.2f}')

# Lógica para determinar o status do IMC
if imc < 18.5:
    print('Status: Abaixo do Peso')
elif 18.5 <= imc < 25: # Podemos simplificar a condição 'imc >= 18.5 and imc < 25'
    print('Status: Peso Ideal')
elif 25 <= imc < 30:
    print('Status: Sobrepeso')
elif 30 <= imc < 40:
    print('Status: Obesidade')
else: # imc >= 40
    print('Status: Obesidade Mórbida')

print('\n--- FIM DO PROGRAMA ---')
time.sleep(2)