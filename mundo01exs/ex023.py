n = int(input('Digite um número de 0 a 9999: '))

uni = n // 1 % 10
dez = n // 10 % 10
cen = n // 100 % 10
mil = n // 1000 % 10

print('Unidades: ', uni)
print('Dezenas: ', dez)
print('Centenas: ', cen)
print('Milhares: ', mil)
