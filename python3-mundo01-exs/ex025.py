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
print('--- VERIFICADOR DE SOBRENOME ---')
print('Este programa verifica se o sobrenome "SILVA" está presente no nome digitado.')
print('=' * 50)

# Define o sobrenome a ser buscado como uma constante
SOBRENOME_BUSCADO = 'SILVA'

# Solicita o nome completo ao usuário com validação
nome_completo = get_texto_nao_vazio('Digite seu nome completo: ')

print(f'\nAnalisando o nome: "{nome_completo}"...')
time.sleep(1.5)

# --- Verificação e Saída ---
# Converte o nome para maiúsculas para uma busca case-insensitive
if SOBRENOME_BUSCADO in nome_completo.upper():
    print(f'Parabéns! Seu nome contém "{SOBRENOME_BUSCADO.upper()}".')
else:
    print(f'Seu nome não contém "{SOBRENOME_BUSCADO.upper()}".')

print('\n--- FIM DO PROGRAMA ---')
time.sleep(1)