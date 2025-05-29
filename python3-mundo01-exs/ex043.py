p = float(input('Digite o seu peso (kg): '))
a = float(input('Digite a sua altura (m): '))
imc = p/(a**2)

print(f'Seu IMC é: {imc:.2f}')

if imc < 18.5:
    print('Abaixo do Peso')
elif imc >= 18.5 and imc < 25:
    print('Peso Ideal')
elif imc >= 25 and imc < 30:
    print('Sobrepeso')
elif imc >= 30 and imc < 40:
    print('Obesidade')
elif imc >= 40:
    print('Obesidade mórbida')
else:
    print('IMC inválido')