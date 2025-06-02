import time

print('--- CALCULADORA DE MÉDIA ESCOLAR ---')

# --- Função de Validação de Entrada para Notas ---
def get_nota(prompt):
    while True:
        try:
            nota_str = input(prompt).replace(',', '.') # Permite vírgula como separador decimal
            nota = float(nota_str)
            # Valida se a nota está dentro de um intervalo razoável (ex: entre 0 e 10)
            if 0 <= nota <= 10:
                return nota # Retorna a nota válida e sai do loop
            else:
                print('Nota inválida! Por favor, digite um valor entre 0 e 10.')
                time.sleep(1)
        except ValueError:
            print('Entrada inválida. Por favor, digite um NÚMERO para a nota (ex: 7.5).')
            time.sleep(1)

# --- Solicitação de Entradas com Validação ---
n1 = get_nota('Digite a primeira nota: ')
n2 = get_nota('Digite a segunda nota: ')

# --- Cálculo da Média ---
m = (n1 + n2) / 2

# --- Exibição do Resultado e Status do Aluno ---
print(f'\nCalculando a média das notas {n1:.1f} e {n2:.1f}...')
time.sleep(1) # Pequena pausa para simular processamento e melhorar a leitura

print(f'Média: {m:.1f}')

# Lógica para determinar o status do aluno (ajustada para o enunciado)
if m < 5.0:
    print('Status: REPROVADO')
elif 5.0 <= m < 7.0: # Média entre 5.0 (inclusive) e 7.0 (exclusivo)
    print('Status: RECUPERAÇÃO')
else: # Média 7.0 ou superior (m >= 7.0)
    print('Status: APROVADO!')

print('\n--- FIM DA AVALIAÇÃO ---')
time.sleep(2)