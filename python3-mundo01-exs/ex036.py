casa = float(input('Qual o valor da casa? '))
sal = float(input('Qual é o seu salário? '))
t = int(input('Em quantos anos você irá pagar? '))
prest = casa / (t * 12)

print(f'Sua prestação será de R${prest:.2f}')

if prest > (sal * 0.3):
    print('Seu empréstimo foi NEGADO.')
else:
    print('Seu empréstimo foi APROVADO!')



