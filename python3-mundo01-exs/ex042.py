import time

print('--- ANALISADOR DE TRIÂNGULOS V2.0 ---')

# --- Funções de Validação de Entrada ---
# Criamos uma função para evitar repetição de código na validação de cada reta
def get_lado_triangulo(prompt):
    while True:
        try:
            valor_str = input(prompt).replace(',', '.')
            lado = float(valor_str)
            if lado <= 0:
                print('Valor inválido! O comprimento de uma reta deve ser um número positivo e maior que zero.')
                time.sleep(1)
            else:
                return lado # Retorna o valor válido e sai do loop
        except ValueError:
            print('Entrada inválida. Por favor, digite um NÚMERO para o comprimento da reta (ex: 5.5).')
            time.sleep(1)

# --- Solicitação de Entradas com Validação ---
r1 = get_lado_triangulo('Digite o valor da primeira reta: ')
r2 = get_lado_triangulo('Digite o valor da segunda reta: ')
r3 = get_lado_triangulo('Digite o valor da última reta: ')

# --- Organização dos Lados para Verificação da Condição de Existência ---
# Usamos sorted() para obter os lados em ordem crescente.
# Isso simplifica muito a lógica de verificar a condição do triângulo.
lados_ordenados = sorted([r1, r2, r3])
menor = lados_ordenados[0]
meio = lados_ordenados[1]
maior = lados_ordenados[2]

# --- Verificação da Condição de Existência do Triângulo ---
# Um triângulo pode ser formado se a soma de quaisquer dois lados for maior que o terceiro lado.
# Ao ordenar os lados, basta verificar se a soma dos dois menores é maior que o maior.
if menor + meio > maior:
    print(f'\nOs segmentos {menor}, {meio} e {maior} PODEM formar um triângulo!')

    # --- Classificação do Tipo de Triângulo ---
    # A ordem das verificações é importante para a especificidade.
    if r1 == r2 and r2 == r3: # Equilátero (todos os lados iguais)
        print('Seu triângulo será: EQUILÁTERO!')
    elif r1 == r2 or r1 == r3 or r2 == r3: # Isósceles (dois lados iguais)
        print('Seu triângulo será: ISÓSCELES!')
    else: # Escaleno (todos os lados diferentes)
        print('Seu triângulo será: ESCALENO!')
else:
    print(f'\nOs segmentos {menor}, {meio} e {maior} NÃO podem formar um triângulo.')
    print('Condição de existência de triângulo não satisfeita.')

print('\n--- FIM DA ANÁLISE ---')
time.sleep(2)