import tkinter as tk
from tkinter import messagebox
import math


def localizar_fortaleza(x1, z1, angulo1, x2, z2, angulo2):
    theta1 = math.radians(angulo1)
    theta2 = math.radians(angulo2)
    m1 = math.tan(theta1)
    m2 = math.tan(theta2)

    if abs(m1 - m2) < 1e-6:
        return None

    x = (m1 * x1 - m2 * x2 + z2 - z1) / (m1 - m2)
    z = m1 * (x - x1) + z1
    return round(x), round(z)


def calcular():
    try:
        x1 = float(entry_x1.get())
        z1 = float(entry_z1.get())
        ang1 = float(entry_ang1.get())
        x2 = float(entry_x2.get())
        z2 = float(entry_z2.get())
        ang2 = float(entry_ang2.get())

        resultado = localizar_fortaleza(x1, z1, ang1, x2, z2, ang2)

        if resultado:
            output_label.config(
                text=f"Fortaleza estimada:\nX = {resultado[0]}, Z = {resultado[1]}")
        else:
            output_label.config(
                text="As linhas são paralelas.\nNão há interseção.")
    except ValueError:
        messagebox.showerror("Erro", "Digite apenas números válidos.")



# Interface Tkinter

# Criação da janela principal
root = tk.Tk()

# Configurações da janela
root.title("Localizador de Fortaleza - Minecraft")

# Definindo tamanho fixo da janela
root.geometry("350x360")

# Impedindo redimensionamento
root.resizable(False, False)


tk.Label(root, text="Coordenadas do Ponto A").pack() # Rótulo para as coordenadas do Ponto A

entry_x1 = tk.Entry(root) # Campo de entrada para a coordenada X do Ponto A
entry_x1.pack() # Adicionando o campo de entrada à janela

entry_x1.insert(0, "395") # Coordenada X do Ponto A
entry_z1 = tk.Entry(root) # Campo de entrada para a coordenada Z do Ponto A
entry_z1.pack() # Adicionando o campo de entrada à janela

entry_z1.insert(0, "-188") # Coordenada Z do Ponto A
entry_ang1 = tk.Entry(root) # Campo de entrada para o ângulo do Ponto A
entry_ang1.pack() # Adicionando o campo de entrada à janela

entry_ang1.insert(0, "60") # Coordenada do ângulo do Ponto A

# Cria um rótulo (texto) na janela principal (root) com o texto "Coordenadas do Ponto B" e o posiciona
tk.Label(root, text="Coordenadas do Ponto B").pack()

# Cria um campo de entrada (Entry) para digitar o valor de X e o posiciona
entry_x2 = tk.Entry(root)
entry_x2.pack()
# Insere o valor inicial "395" no campo de entrada de X
entry_x2.insert(0, "395")

# Cria um campo de entrada para digitar o valor de Z e o posiciona
entry_z2 = tk.Entry(root)
entry_z2.pack()
# Insere o valor inicial "921" no campo de entrada de Z
entry_z2.insert(0, "921")

# Cria um campo de entrada para digitar o ângulo e o posiciona
entry_ang2 = tk.Entry(root)
entry_ang2.pack()
# Insere o valor inicial "120" no campo de entrada de ângulo
entry_ang2.insert(0, "120")

# Cria um botão com o texto "Calcular Fortaleza" que, quando clicado, chama a função 'calcular'
tk.Button(root, text="Calcular Fortaleza", command=calcular).pack(pady=10)

# Cria um rótulo vazio para exibir a saída (resultado) com fonte Arial tamanho 12 e alinhamento central
output_label = tk.Label(root, text="", font=("Arial", 12), justify="center")
output_label.pack()

# Inicia o loop principal da interface gráfica (mantém a janela aberta)
root.mainloop()
