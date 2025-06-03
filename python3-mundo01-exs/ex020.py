import random
import time

# --- Função de Validação de Entrada para Texto Não Vazio ---
def get_texto_nao_vazio(prompt):
    while True:
        texto = input(prompt).strip() # Remove espaços extras no início/fim
        if not texto: # Verifica se a string está vazia após o strip
            print('Entrada inválida! Por favor, digite um nome válido.')
            time.sleep(1)
        else:
            return texto

# --- Corpo Principal do Programa ---
print('--- SORTEIO DA ORDEM DE APRESENTAÇÃO ---')
print('Este programa irá sortear a ordem de apresentação de trabalhos.')
print('=' * 60)

# Define o número de alunos como uma constante para facilitar mudanças futuras
NUMERO_DE_ALUNOS = 4
alunos = []

# Coleta os nomes dos alunos em um loop, com validação
for i in range(1, NUMERO_DE_ALUNOS + 1):
    nome_aluno = get_texto_nao_vazio(f'Digite o nome do {i}º aluno: ')
    alunos.append(nome_aluno)

print('\nSorteando a ordem...')
time.sleep(2) # Pequena pausa para efeito de suspense

# Embaralha a lista de alunos
random.shuffle(alunos)

print('\n--- ORDEM DE APRESENTAÇÃO SORTEADA ---')
# Exibe a lista de alunos na nova ordem.
# Podemos usar enumerate para mostrar a posição na apresentação.
for i, aluno in enumerate(alunos):
    print(f'{i+1}º - {aluno}')
print('---------------------------------------\n')

print('--- FIM DO PROGRAMA ---')
time.sleep(1)