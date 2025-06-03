import time

# --- Função de Validação de Entrada para Números Flutuantes Positivos ---
def get_float_positivo(prompt):
    while True:
        try:
            valor_str = input(prompt).replace(',', '.') # Aceita vírgula como decimal
            valor = float(valor_str)
            if valor <= 0:
                print('Valor inválido! Por favor, digite um comprimento positivo e maior que zero.')
                time.sleep(1)
            else:
                return valor
        except ValueError:
            print('Entrada inválida. Por favor, digite um NÚMERO (ex: 5.5).')
            time.sleep(1)

# --- Corpo Principal do Programa ---
print('--- ANALISADOR DE TRIÂNGULOS ---')
print('Verificaremos se três segmentos de reta podem formar um triângulo.')
print('=' * 50)

# Solicita os comprimentos das retas com validação
r1 = get_float_positivo('Digite o comprimento da primeira reta: ')
r2 = get_float_positivo('Digite o comprimento da segunda reta: ')
r3 = get_float_positivo('Digite o comprimento da terceira reta: ')

print('\nAnalisando os segmentos...')
time.sleep(1.5)

# --- Lógica de verificação de triângulo (Método comum) ---
# Um triângulo pode ser formado se a soma de quaisquer dois lados for maior que o terceiro.
if (r1 + r2 > r3) and \
   (r1 + r3 > r2) and \
   (r2 + r3 > r1):
    print(f'Os segmentos {r1}, {r2} e {r3} PODEM FORMAR um triângulo!')
else:
    print(f'Os segmentos {r1}, {r2} e {r3} NÃO PODEM FORMAR um triângulo.')

# --- Exemplo da sua lógica adaptada com min/max (alternativa, não precisa das duas) ---
# Você também poderia fazer, se preferir seu método original, mas de forma mais Pythônica:
# menor_lado = min(r1, r2, r3)
# maior_lado = max(r1, r2, r3)
# meio_lado = (r1 + r2 + r3) - menor_lado - maior_lado

# if menor_lado + meio_lado > maior_lado:
#     print(f'Os segmentos {r1}, {r2} e {r3} PODEM FORMAR um triângulo! (Verificado com menor+meio > maior)')
# else:
#     print(f'Os segmentos {r1}, {r2} e {r3} NÃO PODEM FORMAR um triângulo! (Verificado com menor+meio > maior)')

print('\n--- FIM DO PROGRAMA ---')
time.sleep(1)