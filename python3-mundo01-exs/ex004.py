import time

# --- Corpo Principal do Programa ---
print('--- ANÁLISE DE ENTRADA ---')
print('Este programa lê o que você digita e mostra suas características.')
print('=' * 50)

# Coletando a entrada do usuário
dado_digitado = input('Digite algo: ')

print(f'\nVocê digitou: "{dado_digitado}"')
print('Analisando as características do que foi digitado...')
time.sleep(1.5)

# Exibindo as informações sobre a entrada
print('\n--- INFORMAÇÕES DETALHADAS ---')

# 1. Tipo primitivo
print(f'1. O tipo primitivo do que você digitou é: {type(dado_digitado)}')
time.sleep(0.3)

# 2. Verificações de conteúdo (com Sim/Não)
print(f'2. Contém apenas espaços?                 : {"Sim" if dado_digitado.isspace() else "Não"}')
time.sleep(0.3)
print(f'3. É um número?                          : {"Sim" if dado_digitado.isnumeric() else "Não"}')
time.sleep(0.3)
print(f'4. É alfabético (somente letras)?        : {"Sim" if dado_digitado.isalpha() else "Não"}')
time.sleep(0.3)
print(f'5. É alfanumérico (letras e/ou números)?: {"Sim" if dado_digitado.isalnum() else "Não"}')
time.sleep(0.3)
print(f'6. Está em letras maiúsculas?            : {"Sim" if dado_digitado.isupper() else "Não"}')
time.sleep(0.3)
print(f'7. Está em letras minúsculas?            : {"Sim" if dado_digitado.islower() else "Não"}')
time.sleep(0.3)
print(f'8. Está capitalizada (Título)?           : {"Sim" if dado_digitado.istitle() else "Não"}')
time.sleep(0.3)
print(f'9. Contém apenas dígitos (0-9)?          : {"Sim" if dado_digitado.isdigit() else "Não"}')
time.sleep(0.3)
print(f'10. É um identificador válido (Python)?  : {"Sim" if dado_digitado.isidentifier() else "Não"}')
time.sleep(0.3)
print(f'11. É imprimível (não é um caracter de controle)?: {"Sim" if dado_digitado.isprintable() else "Não"}')
time.sleep(0.3)

print('-----------------------------\n')

print('--- FIM DA ANÁLISE ---')
time.sleep(0.5)1