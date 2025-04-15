s = float(input('Qual o salário do funcionário? R$'))
if s > 1250:
    s_aum = s * 1.1
else:
    s_aum = s * 1.15
print(f'O novo salário, com aumento, será de R${s_aum:.2f}')