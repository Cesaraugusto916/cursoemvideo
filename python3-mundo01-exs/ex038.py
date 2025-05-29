n1 = int(input('Digite um valor inteiro: '))
n2 = int(input('Digite outro valor inteiro: '))
n3 = int(input('Digite o último valor inteiro: '))

if (n1 <= n2) and (n1 <= n3):
    menor = n1
elif (n2 <= n1) and (n2 <= n3):
    menor = n2
else:
    menor = n3

if (n1 >= n2) and (n1 >= n3):
    maior = n1
elif (n2 >= n1) and (n2 >= n3):
    maior = n2
else:
    maior = n3

meio = (n1 + n2 + n3) - maior - menor

print(f'A ordeom crescente dos números que vc digitou é'
      f'\nMenor: {menor} '
      f'\nMeio: {meio}'
      f'\nMaior: {maior}!')
