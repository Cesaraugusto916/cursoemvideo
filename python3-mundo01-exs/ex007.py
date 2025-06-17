import time

# --- Função de Validação de Entrada ---
def get_nota_valida(prompt, min_val=0.0, max_val=10.0):
    """
    Solicita uma nota ao usuário, validando se é um número float
    e se está dentro do intervalo permitido (padrão de 0.0 a 10.0).
    """
    while True:
        try:
            # Aceita tanto ponto quanto vírgula como separador decimal
            valor_str = input(prompt).replace(',', '.')
            nota = float(valor_str)
            if min_val <= nota <= max_val: # Verifica se a nota está no intervalo válido
                return nota
            else:
                print(f'Nota inválida! Por favor, digite um valor entre {min_val:.1f} e {max_val:.1f}.')
                time.sleep(0.5)
        except ValueError:
            print('Entrada inválida. Por favor, digite um NÚMERO (ex: 7.5 ou 9).')
            time.sleep(0.5)

# --- Corpo Principal do Programa ---
print('--- CALCULADORA DE MÉDIA ARITMÉTICA ---')
print('Este programa calcula a média de duas notas de um aluno.')
print('=' * 50)

# Coletando as notas do aluno com validação
# Podemos especificar o intervalo, se necessário, por exemplo: max_val=100.0 para notas de 0 a 100.
nota1 = get_nota_valida('Insira a primeira nota do aluno (0-10): ')
nota2 = get_nota_valida('Insira a segunda nota do aluno (0-10): ')

print(f'\nCalculando a média para as notas {nota1:.2f} e {nota2:.2f}...')
time.sleep(1.5)

# Calculando a média
media_aluno = (nota1 + nota2) / 2

# Exibindo o resultado
print('\n--- RESULTADO DA MÉDIA ---')
print(f'A primeira nota foi: {nota1:.2f}')
print(f'A segunda nota foi: {nota2:.2f}')
print(f'A média aritmética desse aluno é: {media_aluno:.2f}')

# Adicionando um feedback simples com base na média (opcional, para aprimorar a UX)
if media_aluno >= 7.0:
    print('Parabéns! O aluno foi APROVADO!')
elif media_aluno >= 5.0:
    print('O aluno está de RECUPERAÇÃO.')
else:
    print('Que pena! O aluno foi REPROVADO.')

print('---------------------------\n')

print('--- FIM DO PROGRAMA ---')
time.sleep(0.5)