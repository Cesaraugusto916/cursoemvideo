from random import choice
n1=input('Digite o nome do primeiro aluno: ')
n2=input('Digito o nome do segundo aluno: ')
n3=input('Digite o nome do terceiro aluno: ')
n4=input('Digite o nome do quarto aluno: ')
lista = [n1, n2, n3, n4]
sort = choice(lista)
print(f'O aluno sorteado foi o {sort}')
