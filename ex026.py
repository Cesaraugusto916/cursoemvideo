frase = input('Digite uma frase: ').strip().lower()

print(f'A letra a aparece {frase.count('a')} vezes.')
print(f'A primeira posiçao do a: {frase.find('a')+1}')
print(f'A última posição do a: {frase.rfind('a')+1}')
