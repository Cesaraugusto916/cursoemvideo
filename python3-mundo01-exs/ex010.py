import requests
from bs4 import BeautifulSoup
import time


# --- Função de Validação de Entrada (reutilizada) ---
def get_float_nao_negativo(prompt):
    """Solicita um número real não negativo ao usuário, validando a entrada."""
    while True:
        try:
            valor_str = input(prompt).replace(',', '.')
            valor = float(valor_str)
            if valor >= 0:
                return valor
            else:
                print('Entrada inválida! Por favor, digite um valor não negativo.')
                time.sleep(0.5)
        except ValueError:
            print('Entrada inválida. Por favor, digite um NÚMERO (ex: 50.00 ou 100).')
            time.sleep(0.5)


# --- Função para Obter a Cotação via Web Scraping ---
def obter_cotacao_via_scraping():
    """
      Tenta raspar a cotação do dólar de um site.
      (ATENÇÃO: Este código é um exemplo conceitual.
      Ele precisa ser adaptado a um site específico e seus seletores HTML.)
      """
    site_alvo = 'https://www.google.com/finance/quote/USD-BRL'  # Exemplo de URL de um site de cotação
    # Geralmente, é bom simular um navegador para evitar bloqueios
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

    try:
        print(f"Buscando cotação de dólar via web scraping em {site_alvo}...")
        response = requests.get(site_alvo, headers=headers, timeout=10)
        response.raise_for_status()  # Levanta erro para status 4xx/5xx

        soup = BeautifulSoup(response.text, 'html.parser')

        # --- AQUI É ONDE O TRABALHO DE INSPEÇÃO ENTRA ---
        # Você precisaria inspecionar o site_alvo para encontrar o seletor exato.
        # Por exemplo, pode ser uma div com uma classe específica:
        # cotacao_elemento = soup.find('div', class_='YMlKec fxKbKc') # Exemplo para Google Finance

        # Este é um exemplo hipotético. O seletor real pode variar e MUDAR ao longo do tempo.
        cotacao_texto = soup.find('div', class_='YMlKec fxKbKc').text  # Exemplo: "5,18 BRL"

        # Processar o texto para obter o número
        cotacao_valor = float(cotacao_texto.replace(',', '.').replace(' BRL', '').strip())

        print(f"Cotação encontrada via scraping: R$ {cotacao_valor:.4f} por U$ 1.00")
        return cotacao_valor

    except requests.exceptions.RequestException as e:
        print(f"Erro de conexão ou requisição ao site: {e}")
        print("Usando uma taxa de câmbio padrão de R$ 5.00 por U$ 1.00 para continuar.")
        return 5.00  # Fallback
    except AttributeError:
        print(
            "Não foi possível encontrar o elemento da cotação no HTML. O seletor pode estar incorreto ou o site mudou.")
        print("Usando uma taxa de câmbio padrão de R$ 5.00 por U$ 1.00 para continuar.")
        return 5.00  # Fallback
    except ValueError:
        print("Erro ao converter a cotação para número. Formato inesperado.")
        print("Usando uma taxa de câmbio padrão de R$ 5.00 por U$ 1.00 para continuar.")
        return 5.00  # Fallback
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
        print("Usando uma taxa de câmbio padrão de R$ 5.00 por U$ 1.00 para continuar.")
        return 5.00  # Fallback


# --- Corpo Principal do Programa ---
print('--- CONVERSOR DE MOEDAS (REAL para DÓLAR - Cotação via Web Scraping) ---')
print('Este programa converte um valor em Reais para Dólares, buscando a cotação em um site.')
print('=' * 60)

# Obtendo a cotação atual via web scraping
taxa_cambio_dolar = obter_cotacao_via_scraping()

if taxa_cambio_dolar is None:  # Se a função de scraping retornar None em caso de falha grave
    print("Não foi possível obter a cotação. Encerrando o programa.")
    exit()

print(f'\nTaxa de Câmbio Atual (U$ 1.00 = R$): R$ {taxa_cambio_dolar:.4f}')
print('-' * 60)

# Coletando a quantia em Reais com validação
quantia_reais = get_float_nao_negativo('Quanto dinheiro você tem na carteira? R$ ')

print(f'\nConvertendo R$ {quantia_reais:.2f} para Dólares com a cotação atual...')
time.sleep(1.5)

# Calculando a quantidade de Dólares
# Se a taxa é 1 USD = X BRL, então BRL / X = USD
quantia_dolares = quantia_reais / taxa_cambio_dolar

# Exibindo o resultado
print('\n--- RESULTADO DA CONVERSÃO ---')
print(f'Com R$ {quantia_reais:.2f} na carteira e a cotação atual,')
print(f'você conseguiria comprar U$ {quantia_dolares:.2f} Dólares.')
print('------------------------------\n')

print('--- FIM DO PROGRAMA ---')
time.sleep(0.5)