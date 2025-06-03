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
print('--- SORTEADOR DE ALUNOS ---')
print('Este programa irá sortear um aluno entre os nomes fornecidos.')
print('=' * 50)

# Define o número de alunos a serem coletados como uma constante
NUMERO_DE_ALUNOS = 4
alunos = []

# Coleta os nomes dos alunos em um loop, com validação
for i in range(1, NUMERO_DE_ALUNOS + 1):
    nome_aluno = get_texto_nao_vazio(f'Digite o nome do {i}º aluno: ')
    alunos.append(nome_aluno)

print('\nRealizando o sorteio...')
time.sleep(2) # Pequena pausa para efeito de suspense

# Sorteia um aluno da lista
aluno_sorteado = random.choice(alunos)

print('\n--- RESULTADO DO SORTEIO ---')
print(f'O aluno escolhido para apagar o quadro foi: {aluno_sorteado}!')
print('---------------------------\n')

print('--- FIM DO PROGRAMA ---')
time.sleep(1)