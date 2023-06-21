import tkinter as tk
from tkinter import messagebox
from tkinter import font as tkfont

# Cores personalizadas
COR_BACKGROUND = "#FDF6E3"  # Cor de fundo da janela
COR_BOTAO = "#EEE8AA"  # Cor dos botões
COR_TEXTO_BOTAO = "#586E75"  # Cor do texto dos botões
COR_PLACAR = "#073642"  # Cor do rótulo do placar
COR_TEXTO_PLACAR = "#FFFFFF"  # Cor do texto do rótulo do placar


# Função para verificar se um jogador venceu
def verificar_vitoria(tabuleiro, jogador):
    # Verificar linhas
    for linha in tabuleiro:
        if linha.count(jogador = 3:
            return True

    # Verificar colunas
    for coluna in range(3:
        if tabuleiro[0][coluna] == tabuleiro[1][coluna] == tabuleiro[2][coluna] == jogador:
            return True

    # Verificar diagonais
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == jogador:
        return True
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == jogador:
        return True

    return False

# Função para realizar uma jogada
def fazer_jogada(linha, coluna):
    global jogador_atual, tabuleiro, placar

    if tabuleiro[linha][coluna] == " ":
        tabuleiro[linha][coluna] = jogador_atual
        if verificar_vitoria(tabuleiro, jogador_atual):
            messagebox.showinfo("Fim de jogo", f"Jogador {jogador_atual} venceu!")
            placar[jogador_atual] += 1
            reiniciar_jogo()
        elif " " not in tabuleiro[0] and " " not in tabuleiro[1] and " " not in tabuleiro[2]:
            messagebox.showinfo("Fim de jogo", "Empate!")
            reiniciar_jogo()
        else:
            jogador_atual = "O" if jogador_atual == "X" else "X"
            atualizar_interface()

# Função para reiniciar o jogo
def reiniciar_jogo():
    global jogador_atual, tabuleiro

    jogador_atual = "X"
    tabuleiro = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    atualizar_interface()

# Função para atualizar a interface gráfica
def atualizar_interface():
    for linha in range(3):
        for coluna in range(3):
            if tabuleiro[linha][coluna] != " ":
                b = tk.Button(janela, text=tabuleiro[linha][coluna], state="disabled",
                              bg=COR_BOTAO, fg=COR_TEXTO_BOTAO, disabledforeground=COR_TEXTO_BOTAO,
                              font=("Arial", 30), width=4, height=2)
            else:
                b = tk.Button(janela, text=" ", command=lambda l=linha, c=coluna: fazer_jogada(l, c),
                              bg=COR_BOTAO, fg=COR_TEXTO_BOTAO, font=("Arial", 30), width=4, height=2)
            b.grid(row=linha, column=coluna)

    placar_label.config(text=f"Placar - X: {placar['X']}  O: {placar['O']}", bg=COR_PLACAR, fg=COR_TEXTO_PLACAR)

# Criar a janela principal
janela = tk.Tk()
janela.title("Jogo da Velha")
janela.configure(bg=COR_BACKGROUND)

# Variáveis globais
jogador_atual = "X"
tabuleiro = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
placar = {"X": 0, "O": 0}

# Criar os botões da interface
for linha in range(3):
    for coluna in range(3):
        b = tk.Button(janela, text=" ", command=lambda l=linha, c=coluna: fazer_jogada(l, c),
                      bg=COR_BOTAO, fg=COR_TEXTO_BOTAO, font=("Arial", 30), width=4, height=2)
        b.grid(row=linha, column=coluna)

# Criar rótulo para o placar
placar_font = tkfont.Font(family="Arial", size=12, weight="bold")
placar_label = tk.Label(janela, text="Placar - X: 0  O: 0", font=placar_font, bg=COR_PLACAR, fg=COR_TEXTO_PLACAR)
placar_label.grid(row=3, column=0, columnspan=3

# Iniciar a interface gráfica
janela.mainloop(


#Em algumas partes do meu código, a inteligência parece que esqueceu ou deu algum bug e não fechou os parênteses