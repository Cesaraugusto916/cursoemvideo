import random
n_pc = random.randint(0,5)
print('Olá, usuário. Eu acabei de pensar em um número de 0 a 5!')
n_us = int(input('Qual número eu pensei?: '))
if n_us == n_pc:
    print(f'Parabéns! Você acertou! Eu pensei exatamente no {n_us}')
else:
    print(f'Boa tentativa, mas eu pensei no número {n_pc}!')