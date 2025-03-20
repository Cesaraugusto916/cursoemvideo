dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos kms rodados? '))
print(f'O total a pagar é R${(60 * dias)+(km * 0.15):.2f}.')
