import time

# --- Corpo Principal do Programa ---
print('--- SAUDAÇÃO PERSONALIZADA ---')
print('Este programa irá ler o seu nome e dar as boas-vindas.')
print('=' * 50)

# Coletando o nome do usuário
# Usamos .strip() para remover espaços em branco no início/fim
# e .title() para capitalizar a primeira letra de cada palavra no nome.
nome_digitado = input('Olá! Por favor, digite o seu nome completo: ').strip().title()

print('\nProcessando seu nome...')
time.sleep(1.5)

# Exibindo a mensagem de boas-vindas usando f-string
# Verifica se o nome não está vazio antes de cumprimentar
if nome_digitado:
    print(f'É um grande prazer te conhecer, {nome_digitado}!')
    print('Seja muito bem-vindo(a) ao nosso programa!')
else:
    print('Parece que você não digitou um nome válido. Que pena!')

print('\n' + '=' * 50)
print('--- FIM DO PROGRAMA ---')
time.sleep(0.5)