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
root = tk.Tk()
root.title("Localizador de Fortaleza - Minecraft")
root.geometry("350x360")
root.resizable(False, False)

tk.Label(root, text="Coordenadas do Ponto A").pack()
entry_x1 = tk.Entry(root)
entry_x1.pack()
entry_x1.insert(0, "395")
entry_z1 = tk.Entry(root)
entry_z1.pack()
entry_z1.insert(0, "-188")
entry_ang1 = tk.Entry(root)
entry_ang1.pack()
entry_ang1.insert(0, "60")

tk.Label(root, text="Coordenadas do Ponto B").pack()
entry_x2 = tk.Entry(root)
entry_x2.pack()
entry_x2.insert(0, "395")
entry_z2 = tk.Entry(root)
entry_z2.pack()
entry_z2.insert(0, "921")
entry_ang2 = tk.Entry(root)
entry_ang2.pack()
entry_ang2.insert(0, "120")

tk.Button(root, text="Calcular Fortaleza", command=calcular).pack(pady=10)
output_label = tk.Label(root, text="", font=("Arial", 12), justify="center")
output_label.pack()

root.mainloop()
