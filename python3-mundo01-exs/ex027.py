import time

# --- Função de Validação de Entrada (simplificada para texto) ---
def get_texto_nao_vazio(prompt):
    while True:
        texto = input(prompt).strip() # Remove espaços extras no início/fim
        if not texto: # Verifica se a string está vazia após o strip
            print('Entrada inválida! Por favor, digite seu nome completo.')
            time.sleep(1)
        else:
            return texto

# --- Corpo Principal do Programa ---
print('--- ANALISADOR DE NOME ---')
print('Este programa irá separar o primeiro e o último nome de uma pessoa.')
print('=' * 50)

nome_completo = get_texto_nao_vazio('Digite seu nome completo: ')

print('\nAnalisando seu nome...')
time.sleep(1.5)

# --- Usando o método split() (MAIS RECOMENDADO) ---
# Divide o nome completo em uma lista de palavras.
# split() sozinho já lida com múltiplos espaços e remove vazios.
palavras_do_nome = nome_completo.split()

primeiro_nome = ""
ultimo_nome = ""

if len(palavras_do_nome) >= 2: # Se há pelo menos duas palavras, temos primeiro e último nome
    primeiro_nome = palavras_do_nome[0]
    ultimo_nome = palavras_do_nome[-1]
elif len(palavras_do_nome) == 1: # Se há apenas uma palavra, ela é o primeiro nome
    primeiro_nome = palavras_do_nome[0]
    ultimo_nome = "(Não há sobrenome aparente)" # Mensagem para indicar ausência de sobrenome
else: # Caso a entrada, por algum motivo, resulte em lista vazia (já evitado pelo get_texto_nao_vazio)
    print("Erro: Não foi possível processar o nome.")


print('\n--- RESULTADO ---')
print(f'Seu primeiro nome é: {primeiro_nome}')
print(f'Seu último nome é: {ultimo_nome}')
print('-------------------\n')

print('--- FIM DO PROGRAMA ---')
time.sleep(1)