import time

v = float(input('Digite o valor do produto: R$'))

print('\n--- CONDIÇÕES DE PAGAMENTO ---')
print('(1) À vista (dinheiro/cheque): 10% de desconto')
print('(2) À vista no cartão: 5% de desconto')
print('(3) Em até 2x no cartão: preço normal')
print('(4) Em 3x ou mais no cartão: 20% de juros')
print('------------------------------\n')

# --- Melhoria 1: Validação da entrada do método de pagamento ---
met = 0 # Inicializa com um valor inválido para entrar no loop
while met not in [1, 2, 3, 4]: # Garante que o usuário escolha uma opção válida
    try:
        met = int(input('Qual a condição de pagamento? Digite o número da opção: '))
        if met not in [1, 2, 3, 4]:
            print('Opção inválida. Por favor, digite 1, 2, 3 ou 4.')
            time.sleep(1)
    except ValueError:
        print('Entrada inválida. Por favor, digite um NÚMERO.')
        time.sleep(1)

valor_final = v # Começa com o valor normal
mensagem_desconto_juros = ""

if met == 1: # Dinheiro/Cheque
    valor_final = v * 0.90
    mensagem_desconto_juros = "10% de Desconto!"
    print(f'\nOpção selecionada: À vista Dinheiro/Cheque')

elif met == 2: # À vista no Cartão
    valor_final = v * 0.95
    mensagem_desconto_juros = "5% de Desconto!"
    print(f'\nOpção selecionada: À vista no Cartão')

elif met == 3: # Em até 2x no Cartão
    print(f'\nOpção selecionada: Em até 2x no Cartão')
    x = 0
    # --- Melhoria 2: Validação da entrada de parcelas para opção 3 ---
    while x not in [1, 2]:
        try:
            x = int(input('Em quantas vezes (1 ou 2)? '))
            if x not in [1, 2]:
                print('Para esta opção, as parcelas devem ser 1 ou 2.')
                time.sleep(1)
        except ValueError:
            print('Entrada inválida. Por favor, digite um NÚMERO (1 ou 2).')
            time.sleep(1)

    valor_final = v
    mensagem_desconto_juros = "Preço Normal"
    valor_parcela = valor_final / x
    print(f'Parcelado em {x}x de R${valor_parcela:.2f}')

elif met == 4: # Em 3x ou mais no Cartão
    print(f'\nOpção selecionada: Em 3x ou mais no Cartão')
    x = 0
    # --- Melhoria 2: Validação da entrada de parcelas para opção 4 ---
    while x < 3: # Deve ser 3 ou mais
        try:
            x = int(input('Em quantas vezes (3x ou mais)? '))
            if x < 3:
                print('Para esta opção, as parcelas devem ser 3 ou mais.')
                time.sleep(1)
        except ValueError:
            print('Entrada inválida. Por favor, digite um NÚMERO (3 ou mais).')
            time.sleep(1)

    valor_final = v * 1.20
    mensagem_desconto_juros = "20% de Juros!"
    valor_parcela = valor_final / x
    print(f'Parcelado em {x}x de R${valor_parcela:.2f}')

# --- Melhoria 3: Mensagens Finais Claras ---
print(f'\n--- RESUMO DA COMPRA ---')
print(f'Preço Original: R${v:.2f}')
print(f'Valor a ser pago: R${valor_final:.2f}')
print(mensagem_desconto_juros)
print('-------------------------\n')
time.sleep(3)
print('Obrigado por utilizar o programa!')
time.sleep(1.5)