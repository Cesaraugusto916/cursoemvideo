d = float(input('Qual foi a distancia em Km? '))
if d > 200:
    print(f'Passagem: R${d*0.45:.2f}')
else:
    print(f'Passagem: R${d*0.50:.2f}')