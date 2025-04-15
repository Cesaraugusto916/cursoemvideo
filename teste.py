import tkinter as tk
from tkinter import messagebox
import time

# Tempo total: 108 minutos em segundos e o limite de aviso: 5 minutos.
TOTAL_TIME = 6 * 60  # 6480 segundos
WARNING_THRESHOLD = 5 * 60  # 300 segundos

# Variáveis globais para o timer e controle dos alarmes
countdown_seconds = TOTAL_TIME
warning_alarm_playing = False
emergency_alarm_playing = False
warning_alarm_id = None
emergency_alarm_id = None


def reset_timer():
    """Reinicia o timer e para os alarmes."""
    global countdown_seconds, warning_alarm_playing, emergency_alarm_playing, warning_alarm_id, emergency_alarm_id
    countdown_seconds = TOTAL_TIME
    timer_label.config(text=format_time(countdown_seconds))
    stop_warning_alarm()
    stop_emergency_alarm()
    log_message("Código aceito. Timer reiniciado.")


def format_time(seconds):
    """Formata os segundos para exibição no formato MM:SS."""
    minutes, sec = divmod(seconds, 60)
    return f"{int(minutes):02d}:{int(sec):02d}"


def update_timer():
    """Atualiza o timer a cada segundo e verifica os estados dos alarmes."""
    global countdown_seconds, warning_alarm_playing, emergency_alarm_playing
    timer_label.config(text=format_time(countdown_seconds))

    # Inicia o alarme de aviso ao chegar a 5 minutos
    if countdown_seconds == WARNING_THRESHOLD and not warning_alarm_playing:
        start_warning_alarm()

    # Ao atingir 0, dispara o alarme de emergência
    if countdown_seconds <= 0:
        if not emergency_alarm_playing:
            start_emergency_alarm()
        timer_label.config(text="00:00")
    else:
        countdown_seconds -= 1
        root.after(1000, update_timer)


def beep_warning():
    """Emite um beep (alarme de aviso) a cada 1 segundo enquanto estiver ativo."""
    global warning_alarm_playing, warning_alarm_id
    if warning_alarm_playing:
        root.bell()
        warning_alarm_id = root.after(1000, beep_warning)


def beep_emergency():
    """Emite um beep (alarme de emergência) a cada 500ms enquanto estiver ativo."""
    global emergency_alarm_playing, emergency_alarm_id
    if emergency_alarm_playing:
        root.bell()
        emergency_alarm_id = root.after(500, beep_emergency)


def start_warning_alarm():
    """Inicia o alarme de aviso repetitivo."""
    global warning_alarm_playing
    warning_alarm_playing = True
    beep_warning()
    log_message("Aviso: Restam 5 minutos para reinicialização!")


def stop_warning_alarm():
    """Para o alarme de aviso."""
    global warning_alarm_playing, warning_alarm_id
    warning_alarm_playing = False
    if warning_alarm_id is not None:
        root.after_cancel(warning_alarm_id)
        warning_alarm_id = None


def start_emergency_alarm():
    """Inicia o alarme de emergência repetitivo."""
    global emergency_alarm_playing
    emergency_alarm_playing = True
    beep_emergency()
    log_message("Emergência: Tempo esgotado! Acionando alarme!")


def stop_emergency_alarm():
    """Para o alarme de emergência."""
    global emergency_alarm_playing, emergency_alarm_id
    emergency_alarm_playing = False
    if emergency_alarm_id is not None:
        root.after_cancel(emergency_alarm_id)
        emergency_alarm_id = None


def check_code(event=None):
    """Verifica o código inserido. Se o código correto for digitado durante os últimos 5 minutos, o timer reinicia."""
    user_code = code_entry.get().strip()
    if user_code == "4 8 15 16 23 42":
        if 0 < countdown_seconds <= WARNING_THRESHOLD:
            reset_timer()
        else:
            log_message("Código inserido fora do período válido. Nada acontece.")
    else:
        log_message("Código incorreto.")
    code_entry.delete(0, tk.END)


def log_message(message):
    """Adiciona mensagens no terminal simulado."""
    log_text.config(state=tk.NORMAL)
    log_text.insert(tk.END, f"{time.strftime('%H:%M:%S')} - {message}\n")
    log_text.see(tk.END)
    log_text.config(state=tk.DISABLED)


# Criação da interface gráfica simulando um terminal retrô.
root = tk.Tk()
root.title("Computador da Escotilha - Simulação Lost")
root.configure(bg="black")

top_frame = tk.Frame(root, bg="black")
top_frame.pack(pady=10)

# Label do timer com visual de terminal
timer_label = tk.Label(top_frame, text=format_time(countdown_seconds),
                       font=("Courier", 32), fg="lime", bg="black")
timer_label.pack()

# Campo de entrada para o código
code_entry = tk.Entry(top_frame, font=("Courier", 16), fg="lime", bg="black", insertbackground="lime", width=25)
code_entry.pack(pady=10)
code_entry.bind("<Return>", check_code)

# Widget de texto para simular o monitor do sistema com logs
log_text = tk.Text(root, height=10, width=50, bg="black", fg="lime", font=("Courier", 10))
log_text.pack(pady=10)
log_text.insert(tk.END, "Iniciando simulação do computador da escotilha...\n")
log_text.config(state=tk.DISABLED)

# Inicia a contagem regressiva após 1 segundo
root.after(1000, update_timer)

# Loop principal da interface
root.mainloop()
