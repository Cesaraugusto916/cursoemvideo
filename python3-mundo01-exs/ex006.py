import time
import math # Importa o módulo math para usar math.sqrt() para raiz quadrada, embora **0.5 funcione

# --- Função de Validação de Entrada ---
def get_numero_para_calculo(prompt):
    """
    Solicita um número real ao usuário, validando a entrada.
    Permite números negativos, mas avisa sobre a raiz quadrada para eles.
    """
    while True:
        try:
            # Aceita tanto ponto quanto vírgula como separador decimal
            valor_str = input(prompt).replace(',', '.')
            numero = float(valor_str)
            return numero
        except ValueError:
            print('Entrada inválida. Por favor, digite um NÚMERO (ex: 7.5 ou 25).')
            time.sleep(0.5)

# --- Corpo Principal do Programa ---
print('--- CALCULADORA DE OPERAÇÕES BÁSICAS ---')
print('Este programa calcula o dobro, triplo e a raiz quadrada de um número.')
print('=' * 60)

# Coletando o número com validação
numero_digitado = get_numero_para_calculo('Digite um número para ver suas propriedades: ')

print(f'\nCalculando dobro, triplo e raiz quadrada de {numero_digitado}...')
time.sleep(1.5)

# Realizando os cálculos
dobro = numero_digitado * 2
triplo = numero_digitado * 3

# Verificação para a raiz quadrada de números negativos
if numero_digitado >= 0:
    raiz_quadrada = numero_digitado ** 0.5 # Ou math.sqrt(numero_digitado)
else:
    # Para números negativos, a raiz quadrada é um número complexo.
    # Podemos avisar o usuário ou tratar como erro. Aqui, vamos avisar.
    raiz_quadrada = "Não pode ser calculada com números reais"


# Exibindo os resultados detalhados
print('\n--- RESULTADOS ---')
print(f'Você digitou: {numero_digitado}')
print(f'O dobro desse número é: {dobro}')
print(f'O triplo desse número é: {triplo}')

if isinstance(raiz_quadrada, float): # Verifica se a raiz foi calculada como float
    print(f'A raiz quadrada desse número é: {raiz_quadrada:.2f}')
else:
    print(f'A raiz quadrada desse número ({numero_digitado}) é: {raiz_quadrada}.')

print('------------------\n')

print('--- FIM DO PROGRAMA ---')
time.sleep(0.5)