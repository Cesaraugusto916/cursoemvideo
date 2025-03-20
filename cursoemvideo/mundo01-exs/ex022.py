nome = str(input("Digite seu nome: ")).strip()

print("Todas as letras maúsculas: ", nome.upper())
print('Todas as letras minúsculas: ', nome.lower())
print('Quantas letras: ', len(nome.replace(" ","")))
primeironome = nome[:nome.find(' ')]
print('Letras do primeiro nome: ', len(primeironome))

