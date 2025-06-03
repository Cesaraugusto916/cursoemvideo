import time

# --- Função de Validação de Entrada para Texto Não Vazio ---
def get_texto_nao_vazio(prompt):
    while True:
        texto = input(prompt).strip() # Remove espaços extras no início/fim
        if not texto: # Verifica se a string está vazia após o strip
            print('Entrada inválida! Por favor, digite um nome de cidade válido.')
            time.sleep(1)
        else:
            return texto

# --- Corpo Principal do Programa ---
print('--- VERIFICADOR DE NOME DE CIDADE ---')
print('Este programa verifica se o nome de uma cidade começa com a palavra "SANTO".')
print('=' * 50)

# Define a palavra a ser buscada como uma constante
PALAVRA_BUSCADA = 'SANTO'

# Solicita o nome da cidade com validação
nome_cidade = get_texto_nao_vazio('Digite o nome de uma cidade: ')

print(f'\nAnalisando a cidade: "{nome_cidade}"...')
time.sleep(1.5)

# --- Verificação e Saída ---
# Converte a cidade para maiúsculas e verifica o prefixo
# É importante verificar se a cidade tem comprimento suficiente para o fatiamento [:(len(PALAVRA_BUSCADA))]
# ou usar startswith(), que é mais robusto
if nome_cidade.upper().startswith(PALAVRA_BUSCADA):
    print(f'Sua cidade ({nome_cidade}) COMEÇA com a palavra "{PALAVRA_BUSCADA.upper()}".')
else:
    print(f'Sua cidade ({nome_cidade}) NÃO COMEÇA com a palavra "{PALAVRA_BUSCADA.upper()}".')

print('\n--- FIM DO PROGRAMA ---')
time.sleep(1)