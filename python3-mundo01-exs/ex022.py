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
print('--- ANALISADOR DE TEXTOS (NOMES) ---')
print('Este programa analisará algumas características do nome completo digitado.')
print('=' * 50)

# Solicita o nome completo do usuário com validação
nome_completo = get_texto_nao_vazio('Digite seu nome completo: ')

print(f'\nAnalisando o nome: "{nome_completo}"...')
time.sleep(1.5)

# --- Processamento das informações ---
# 1. Nome em maiúsculas e minúsculas
nome_maiusculas = nome_completo.upper()
nome_minusculas = nome_completo.lower()

# 2. Quantidade de letras ao todo (sem considerar espaços)
# Substitui todos os espaços por nada e então conta o comprimento
total_letras_sem_espacos = len(nome_completo.replace(" ", ""))

# 3. Quantidade de letras do primeiro nome
# Usa split() para obter uma lista de palavras.
# Isso é mais robusto para extrair o primeiro nome.
palavras_do_nome = nome_completo.split()

# Verifica se a lista de palavras não está vazia (caso a validação inicial falhe por algum motivo)
if palavras_do_nome:
    primeiro_nome = palavras_do_nome[0]
    letras_primeiro_nome = len(primeiro_nome)
else:
    primeiro_nome = "N/A" # Caso improvável devido à validação get_texto_nao_vazio
    letras_primeiro_nome = 0


# --- Exibição dos resultados ---
print('\n--- RESULTADOS DA ANÁLISE ---')
print(f'Nome em maiúsculas: {nome_maiusculas}')
print(f'Nome em minúsculas: {nome_minusculas}')
print(f'Total de letras (sem espaços): {total_letras_sem_espacos}')
print(f'Seu primeiro nome é "{primeiro_nome}" e tem {letras_primeiro_nome} letras.')
print('-------------------------------\n')

print('--- FIM DO PROGRAMA ---')
time.sleep(1)