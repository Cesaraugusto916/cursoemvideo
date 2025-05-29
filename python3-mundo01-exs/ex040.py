n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1+n2)/2

if m < 5:
    print(f'Média {m:.1f}: REPROVADO')
elif m > 5 and m < 6.9:
    print(f'Média {m:.1f}: RECUPERAÇÃO')
else:
    print(f'Média {m:.1f}: APROVADO!')