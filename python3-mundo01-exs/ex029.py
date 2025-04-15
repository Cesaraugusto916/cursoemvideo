v = int(input('Digite a velocidade do carro em Km/h: '))
if v <= 80:
    print('Que bom, o carro não foi multado')
else:
    print(f'Que pena. O carro foi multado. Ele passou {v-80} Km/h acima da velocidade permitida')
    print(f'Sua multa será de R${(v-80)*7:.2f}')