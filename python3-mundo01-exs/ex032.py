import time
import datetime # Importa o módulo datetime para obter o ano atual

# --- Função de Validação de Entrada para Números Inteiros Positivos ---
def get_inteiro_positivo(prompt):
    while True:
        try:
            valor_str = input(prompt)
            numero = int(valor_str)
            if numero <= 0:
                print('Valor inválido! Por favor, digite um número inteiro positivo.')
                time.sleep(1)
            else:
                return numero
        except ValueError:
            print('Entrada inválida. Por favor, digite um NÚMERO INTEIRO.')
            time.sleep(1)

# --- Função para verificar se o ano é bissexto ---
def verificar_bissexto(ano):
    # Regra: Anos divisíveis por 4 E (não divisíveis por 100 OU divisíveis por 400)
    return (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)

# --- Corpo Principal do Programa ---
print('--- VERIFICADOR DE ANO BISSEXTO ---')
print('Descubra se um ano é bissexto e sua relação com o ano atual.')
print('=' * 60)

# Obtém o ano atual
ano_atual = datetime.date.today().year

# Solicita o ano ao usuário com validação
ano_para_verificar = get_inteiro_positivo('Digite o ano que deseja verificar: ')

print(f'\nAnalisando o ano {ano_para_verificar}...')
time.sleep(1.5)

# --- Determina se o ano é bissexto ---
e_bissexto = verificar_bissexto(ano_para_verificar)

# --- Determina a relação com o ano atual (passado, presente, futuro) ---
verbo_temporal = ""
if ano_para_verificar < ano_atual:
    verbo_temporal = "foi"
elif ano_para_verificar == ano_atual:
    verbo_temporal = "é"
else:
    verbo_temporal = "será"

# --- Constrói a mensagem final completa ---
if e_bissexto:
    print(f'O ano {ano_para_verificar} {verbo_temporal} BISSEXTO.')
else:
    print(f'O ano {ano_para_verificar} {verbo_temporal} NÃO é bissexto.') # Ajustado para incluir o verbo temporal

print('\n--- FIM DO PROGRAMA ---')
time.sleep(1)