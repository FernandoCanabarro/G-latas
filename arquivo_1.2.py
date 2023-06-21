import time
import random
import tkinter as tk
from tkinter import messagebox

# Cores personalizadas
COR_BACKGROUND = "#FDF6E3"  # Cor de fundo da janela
COR_TEXTO = "#073642"  # Cor do texto
COR_VERMELHO = "#DC322F"  # Cor vermelha
COR_VERDE = "#859900"  # Cor verde
COR_AZUL = "#268BD2"  # Cor azul
COR_AMARELO = "#B58900"  # Cor amarela

# Função para iniciar o simulador de reação de tempo
def iniciar_simulador():
    cores = ['vermelho', 'verde', 'azul', 'amarelo']
    cor_aleatoria = random.choice(cores)

    label_mensagem.config(text="Prepare-se...", fg=COR_TEXTO)
    label_mensagem.update()

    # Aguarda um tempo aleatório antes de exibir a cor
    tempo_aleatorio = random.uniform(1, 3)
    time.sleep(tempo_aleatorio)

    label_mensagem.config(text=cor_aleatoria.upper(), fg=obter_cor(cor_aleatoria))
    label_mensagem.update()

    global tempo_inicial
    tempo_inicial = time.time()

# Função para registrar a reação do usuário
def reagir(event):
    if event.keysym == "Return":
        tempo_final = time.time()
        tempo_reacao = tempo_final #
        label_mensagem.config(text=f"Seu tempo de reação foi de {tempo_reacao:.3f} segundos.", fg=COR_TEXTO)
        label_mensagem.update()

# Função para obter a cor correspondente
def obter_cor(cor):
    if cor == 'vermelho':
        return COR_VERMELHO
    elif cor == 'verde':
        return COR_VERDE
    elif cor == 'azul':
        return COR_AZUL
    elif cor == 'amarelo':
        return COR_AMARELO
    else:
        return COR_TEXTO

# Criar a janela principal
janela = tk.Tk()
janela.title("Simulador de Reação de Tempo")
janela.configure(bg=COR_BACKGROUND)

# Criar rótulo para exibir as mensagens
label_mensagem = tk.Label(janela, text="Clique em 'Iniciar' para começar o simulador.", font=("Arial", 16),
                          fg=COR_TEXTO, bg=COR_BACKGROUND)
label_mensagem.pack(pady=20)

# Criar botão para iniciar o simulador
botao_iniciar = tk.Button(janela, text="Iniciar", command=iniciar_simulador, font=("Arial", 14),
                          fg=COR_TEXTO, bg=COR_BACKGROUND, relief=tk.RAISED)
botao_iniciar.pack(pady=10)

# Registrar a função de reação ao pressionar a tecla "Enter"
janela.bind("<Key>", reagir)

# Iniciar a interface gráfica
janela.mainloop()
