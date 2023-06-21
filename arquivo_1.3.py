import time
import tkinter as tk

# Cores personalizadas
COR_BACKGROUND = "#FDF6E3"  # Cor de fundo da janela
COR_TEXTO = "#073642"  # Cor do texto
COR_VERMELHO = "#DC322F"  # Cor vermelha
COR_VERDE = "#859900"  # Cor verde
COR_AZUL = "#268BD2"  # Cor azul

def iniciar_cronometro():
    global inicio
    inicio = time.time()
    atualizar_cronometro()

def parar_cronometro():
    janela.after_cancel(contagem)

def reiniciar_cronometro():
    parar_cronometro()
    label_cronometro.config(text="00:00:00", fg=COR_TEXTO)

def atualizar_cronometro():
    tempo_passado = int(time.time() - inicio)
    minutos = tempo_passado // 60
    segundos = tempo_passado % 60
    horas = minutos // 60
    minutos = minutos % 60
    tempo_formatado = f"{horas:02d}:{minutos:02d}:{segundos:02d}"
    label_cronometro.config(text=tempo_formatado, fg=COR_VERDE)
    global contagem
    contagem = janela.after(1000, atualizar_cronometro)

# Criar a janela principal
janela = tk.Tk()
janela.title("Cronômetro")
janela.configure(bg=COR_BACKGROUND)

# Criar rótulo para exibir o cronômetro
label_cronometro = tk.Label(janela, text="00:00:00", font=("Arial", 32), fg=COR_TEXTO, bg=COR_BACKGROUND, width=8)
label_cronometro.pack(pady=20)

# Criar botões
frame_botoes = tk.Frame(janela, bg=COR_BACKGROUND)
frame_botoes.pack()

botao_iniciar = tk.Button(frame_botoes, text="Iniciar", command=iniciar_cronometro, font=("Arial", 14), fg=COR_TEXTO, bg=COR_AZUL, relief=tk.RAISED)
botao_iniciar.grid(row=0, column=0, padx=10)

botao_parar = tk.Button(frame_botoes, text="Parar", command=parar_cronometro, font=("Arial", 14), fg=COR_TEXTO, bg=COR_AZUL, relief=tk.RAISED)
botao_parar.grid(row=0, column=1, padx=10)

botao_reiniciar = tk.Button(frame_botoes, text="Reiniciar", command=reiniciar_cronometro, font=("Arial", 14), fg=COR_TEXTO, bg=COR_AZUL, relief=tk.RAISED)
botao_reiniciar.grid(row=0, column=2, padx=10)

# Iniciar a interface gráfica
janela.mainloop()
