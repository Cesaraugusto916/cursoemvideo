v = float(input('Digite o valor: R$'))
met = int(input('Qual o método?'
                '\n(1) Dinheiro/Cheque;'
                '\n(2) Cartão'
                '\nDigite: '))

if met == 2:
    x = int(input('Em quantas vezes? '))
    if x == 1:
        print(f'Valor a ser pago: R${v*0.95:.2f}\n'
              f'5% de Desconto!')
    elif x == 2:
        print(f'Valor a ser pago: R${v:.2f}\n'
              f'Preço Normal')
    elif x >= 3:
        print(f'Valor a ser pago: R${v*1.2:.2f}\n'
              f'20% de Juros!')
else:
    print(f'Valor a ser pago: R${v*0.9}\n'
          f'10 % de Desconto!')
