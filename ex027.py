nome = input('Digite seu nome inteiro: ').strip()
pri = nome[:nome.find(' ')]
ult = nome[nome.rfind(' '):]

print(f'Seu primeiro nome é {pri} e seu ultimo nome é{ult}.')
