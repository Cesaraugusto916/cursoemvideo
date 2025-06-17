import time

# --- Função de Validação de Entrada ---
def get_inteiro_valido(prompt):
    """Solicita um número inteiro ao usuário, validando a entrada."""
    while True:
        try:
            valor_str = input(prompt)
            valor = int(valor_str)
            return valor
        except ValueError:
            print('Entrada inválida. Por favor, digite um NÚMERO INTEIRO.')
            time.sleep(0.5)

# --- Corpo Principal do Programa ---
print('--- GERADOR DE TABUADA APRIMORADO ---')
print('Este programa mostra a tabuada de um número inteiro até um limite definido.')
print('=' * 60)

# Coletando o número principal para a tabuada
numero = get_inteiro_valido('Digite um número inteiro para ver sua tabuada: ')

# Coletando o limite da tabuada, com padrão 10
limite_tabuada = 10 # Define o valor padrão
while True:
    limite_str = input(f'Até que número você quer a tabuada (padrão é {limite_tabuada})? ')
    if limite_str.strip() == '': # Se o usuário pressionar Enter sem digitar nada
        print(f"Limite padrão de {limite_tabuada} utilizado.")
        break # Sai do loop, usando o valor padrão
    try:
        limite_digitado = int(limite_str)
        if limite_digitado > 0: # O limite deve ser um número inteiro positivo
            limite_tabuada = limite_digitado
            break # Sai do loop com o limite definido pelo usuário
        else:
            print('Entrada inválida! O limite deve ser um número inteiro positivo. Usando 10 como padrão.')
            # Não precisamos do 'break' aqui se quisermos que ele continue pedindo até ter uma entrada válida ou padrão
            # Mas, para manter a lógica de "usar padrão e seguir", podemos quebrar aqui também.
            # Se você quiser que ele continue pedindo, remova o 'break' daqui e continue o loop.
            break # Usar o padrão e seguir em frente
    except ValueError:
        print('Entrada inválida. Por favor, digite um NÚMERO INTEIRO ou pressione Enter para usar o padrão.')
        time.sleep(0.5)

print(f'\nPreparando a tabuada de {numero} até {limite_tabuada}...')
time.sleep(1.5)

# Exibindo a tabuada usando um loop 'for'
print(f'\n--- TABUADA DO {numero} (até {limite_tabuada}) ---')
for i in range(1, limite_tabuada + 1): # Loop do 1 até o limite (inclusive)
    print(f'{numero:^4} x {i:2} = {numero * i:>4}')
    time.sleep(0.3) # Adiciona o atraso de 0.3 segundos entre cada linha
print('----------------------------------\n')

print('--- FIM DO PROGRAMA ---')
time.sleep(0.5)