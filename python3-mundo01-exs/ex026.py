import time

# --- Função de Validação de Entrada para Texto Não Vazio ---
def get_texto_nao_vazio(prompt):
    while True:
        texto = input(prompt).strip() # Remove espaços extras no início/fim
        if not texto: # Verifica se a string está vazia após o strip
            print('Entrada inválida! Por favor, digite uma frase.')
            time.sleep(1)
        else:
            return texto

# --- Corpo Principal do Programa ---
print('--- ANALISADOR DE LETRAS EM FRASE ---')
print('Este programa contará a ocorrência de uma letra e suas posições.')
print('=' * 50)

# Define a letra a ser buscada como uma constante
LETRA_BUSCADA = 'a'

# Solicita a frase ao usuário e a padroniza
frase = get_texto_nao_vazio(f'Digite uma frase para analisar a letra "{LETRA_BUSCADA}": ').lower() # Já padroniza para minúsculas aqui

print(f'\nAnalisando a frase: "{frase}"...')
time.sleep(1.5)

# --- Contagem e Posições ---
quantidade_a = frase.count(LETRA_BUSCADA)
primeira_posicao_a = frase.find(LETRA_BUSCADA)
ultima_posicao_a = frase.rfind(LETRA_BUSCADA)

print(f'\n--- RESULTADO ---')
print(f'A letra "{LETRA_BUSCADA.upper()}" aparece {quantidade_a} vezes na frase.')

# Condicional para tratar a ausência da letra na frase
if quantidade_a > 0:
    print(f'A primeira vez que ela aparece é na posição: {primeira_posicao_a + 1}')
    print(f'A última vez que ela aparece é na posição: {ultima_posicao_a + 1}')
else:
    print(f'A letra "{LETRA_BUSCADA.upper()}" não foi encontrada na frase.')

print('-------------------\n')
print('--- FIM DO PROGRAMA ---')
time.sleep(1)