import pygame
import time
import os # Importa o módulo os para verificar a existência do arquivo

# --- Função para carregar e reproduzir áudio ---
def reproduzir_audio(caminho_arquivo):
    try:
        # Inicializa o mixer do pygame
        pygame.mixer.init()
        pygame.mixer.music.load(caminho_arquivo)
        print(f"🎵 Reproduzindo '{os.path.basename(caminho_arquivo)}'...")
        pygame.mixer.music.play()

        # Espera a música terminar de tocar
        # Adiciona um loop para verificar se a música ainda está tocando
        while pygame.mixer.music.get_busy():
            time.sleep(1) # Espera 1 segundo antes de verificar novamente

        print("🎧 Reprodução concluída.")

    except FileNotFoundError:
        print(f"❌ ERRO: O arquivo '{caminho_arquivo}' não foi encontrado.")
        print("Certifique-se de que o arquivo MP3 está no mesmo diretório do script ou que o caminho está correto.")
    except pygame.error as e:
        print(f"❌ ERRO ao reproduzir áudio: {e}")
        print("Verifique se o arquivo MP3 é válido e se as bibliotecas de áudio estão configuradas corretamente.")
    finally:
        # Garante que o mixer seja encerrado corretamente
        if pygame.mixer.get_init():
            pygame.mixer.music.stop()
            pygame.mixer.quit()
            pygame.quit()


# --- Corpo Principal do Programa ---
print('--- TOCADOR DE MP3 SIMPLES ---')
print('Este programa irá reproduzir um arquivo MP3. Certifique-se de que o arquivo esteja no mesmo diretório.')
print('=' * 60)

# Nome do arquivo MP3 (certifique-se de que este arquivo existe no mesmo diretório)
nome_do_arquivo_mp3 = 'asd.mp3' # Mantenha o nome que você usou

# Tenta reproduzir o áudio
reproduzir_audio(nome_do_arquivo_mp3)

print('\n--- FIM DO PROGRAMA ---')
time.sleep(1)