ano = int(input('Digite seu ano de nascimento: '))

if (2025 - ano) > 18:
    print(f'Você passou {(2025-ano)-18} ano(s) do tempo de se alistar!')
elif (2025 - ano) == 18:
    print('Você está na idade de se alistar!')
else:
    print(f"Ainda falta {18-(2025-ano)} ano(s) para o seu alistamento!")