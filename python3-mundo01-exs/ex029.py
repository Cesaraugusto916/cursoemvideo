import time

# --- Função de Validação de Entrada para Números Inteiros Não Negativos ---
# Adaptei a função de inteiro positivo para aceitar 0, já que velocidade pode ser 0
def get_inteiro_nao_negativo(prompt):
    while True:
        try:
            valor_str = input(prompt)
            numero = int(valor_str)
            if numero < 0: # Agora aceita 0, mas não negativos
                print('Valor inválido! Por favor, digite uma velocidade não negativa.')
                time.sleep(1)
            else:
                return numero
        except ValueError:
            print('Entrada inválida. Por favor, digite um NÚMERO INTEIRO.')
            time.sleep(1)

# --- Corpo Principal do Programa ---
print('--- RADAR ELETRÔNICO ---')
print('Verificador de velocidade e calculador de multa.')
print('=' * 50)

# Define as constantes para as regras do radar
LIMITE_VELOCIDADE = 80 # Km/h
VALOR_MULTA_POR_KM = 7.00 # R$ por cada Km/h acima do limite

# Solicita a velocidade do carro com validação
velocidade_carro = get_inteiro_nao_negativo(f'Digite a velocidade atual do carro em Km/h (limite: {LIMITE_VELOCIDADE} Km/h): ')

print(f'\nAnalisando velocidade de {velocidade_carro} Km/h...')
time.sleep(1.5)

# --- Lógica de Multa e Saída ---
if velocidade_carro <= LIMITE_VELOCIDADE:
    print('===================================================')
    print('Parabéns! Você está dentro do limite de velocidade.')
    print('O carro NÃO foi multado.')
    print('===================================================')
else:
    velocidade_excedida = velocidade_carro - LIMITE_VELOCIDADE
    valor_multa = velocidade_excedida * VALOR_MULTA_POR_KM
    print('===================================================')
    print('ATENÇÃO! O carro foi multado!')
    print(f'Ele excedeu o limite em {velocidade_excedida} Km/h.')
    print(f'O valor da multa será de R${valor_multa:.2f}.')
    print('===================================================')

print('\n--- FIM DO PROGRAMA ---')
time.sleep(1)