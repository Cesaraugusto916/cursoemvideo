from math import hypot
c1 = float(input('Digite o valor do cateto oposto: '))
c2 = float(input('Digite o valor do cateto adjacente: '))
hip = hypot(c1, c2)
print(f'A hipotenusa desse triangulo retanguloe é {hip:.2f}')