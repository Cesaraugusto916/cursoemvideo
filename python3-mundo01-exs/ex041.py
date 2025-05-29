ano = int(input('Digite o ano de nascimento: '))
idade = 2025 - ano
print(f'Sua idade: {idade:.0f}')

if idade < 9:
    print('Categoria: MIRIM')
elif idade >= 9 and idade < 14:
    print('Categoria: INFANTIL')
elif idade >= 14 and idade < 19:
    print('Categoria: JUNIOR')
elif idade >= 19 and idade < 20:
    print('Categoria: SÊNIOR')
elif idade >= 20:
    print('Categoria: MASTER')
else:
    print('Idade inválida')