from tkinter import *
from PIL import ImageTk
import time
import backend

# 🖥️ JANELA
root = Tk()
root.title("Vending Machine PIX")
root.state("zoomed")

# =========================
# 🧠 TELAS
# =========================

frame_main = Frame(root)
frame_pagamento = Frame(root)

frame_main.pack(fill="both", expand=True)

# =========================
# 🧱 LAYOUT PRINCIPAL (3 COLUNAS)
# =========================

# 🛒 ESQUERDA = CARRINHO
frame_left = Frame(frame_main, width=300, bg="#f0f0f0")
frame_left.pack(side=LEFT, fill=Y)

# 📦 CENTRO = PRODUTOS
frame_center = Frame(frame_main)
frame_center.pack(side=LEFT, expand=True, fill="both")

# 💰 DIREITA = TOTAL
frame_right = Frame(frame_main, width=250, bg="#eaeaea")
frame_right.pack(side=RIGHT, fill=Y)

# =========================
# 🛒 CARRINHO
# =========================

carrinho = {}

Label(frame_left, text="CARRINHO", font=(
    "Arial", 16), bg="#f0f0f0").pack(pady=0)

frame_carrinho = Frame(frame_left, bg="#f0f0f0")
frame_carrinho.pack()

# =========================
# 💰 TOTAL (EMBAIXO DIREITA)
# =========================

# espaço empurra pra baixo
Frame(frame_right, bg="#eaeaea").pack(expand=True)

label_total = Label(frame_right, text="Total: R$0.00",
                    font=("Arial", 18), bg="#eaeaea")
label_total.pack(pady=10)

# =========================
# 📦 PRODUTOS
# =========================

produtos = [
    {"codigo": "A1", "nome": "Coca-Cola", "preco": 0.10},
    {"codigo": "A2", "nome": "Guaraná", "preco": 0.10},
    {"codigo": "A3", "nome": "Água", "preco": 0.10},
    {"codigo": "B1", "nome": "Salgadinho", "preco": 0.10},
]

botoes = []

# =========================
# ➕➖❌ CARRINHO
# =========================


def adicionar_carrinho(produto):
    nome = produto["nome"]

    if nome in carrinho:
        carrinho[nome]["qtd"] += 1
    else:
        carrinho[nome] = {"preco": produto["preco"], "qtd": 1}

    atualizar_carrinho()


def aumentar(nome):
    carrinho[nome]["qtd"] += 1
    atualizar_carrinho()


def diminuir(nome):
    carrinho[nome]["qtd"] -= 1
    if carrinho[nome]["qtd"] <= 0:
        del carrinho[nome]
    atualizar_carrinho()


def remover(nome):
    del carrinho[nome]
    atualizar_carrinho()


def atualizar_carrinho():
    for w in frame_carrinho.winfo_children():
        w.destroy()

    total = 0

    if not carrinho:
        Label(frame_carrinho, text="Carrinho vazio", bg="#f0f0f0").pack()
        label_total.config(text="Total: R$0.00")
        return

    for nome, item in carrinho.items():
        preco = item["preco"]
        qtd = item["qtd"]
        total += preco * qtd

        f = Frame(frame_carrinho, bg="#f0f0f0")
        f.pack()

        Button(f, text="+", command=lambda n=nome: aumentar(n)).pack(side=LEFT)
        Button(f, text="-", command=lambda n=nome: diminuir(n)).pack(side=LEFT)
        Button(f, text="❌", command=lambda n=nome: remover(n)).pack(side=LEFT)

        Label(f, text=f"{nome} x{qtd}", bg="#f0f0f0").pack(side=LEFT)

    label_total.config(text=f"Total: R${total:.2f}")

# =========================
# 💳 PAGAMENTO (TELA NOVA)
# =========================


label_status_pag = Label(frame_pagamento, text="", font=("Arial", 20))
label_status_pag.pack(pady=20)

label_timer_pag = Label(frame_pagamento, text="", font=("Arial", 18))
label_timer_pag.pack()

label_qr_pag = Label(frame_pagamento)
label_qr_pag.pack(pady=20)


def mostrar_pagamento():
    frame_main.pack_forget()
    frame_pagamento.pack(fill="both", expand=True)


def voltar_inicio():
    frame_pagamento.pack_forget()
    frame_main.pack(fill="both", expand=True)

    carrinho.clear()
    atualizar_carrinho()

# =========================
# 💳 PAGAR
# =========================


def pagar():
    global payment_id, inicio

    if not carrinho:
        return

    total = sum(item["preco"] * item["qtd"] for item in carrinho.values())

    payment_id, image = backend.criar_pagamento(total, "Compra vending")

    img = ImageTk.PhotoImage(image)
    label_qr_pag.config(image=img)
    label_qr_pag.image = img

    mostrar_pagamento()

    inicio = time.time()
    verificar_pagamento()


btn_pagar = Button(
    frame_right,
    text="PAGAR",
    font=("Arial", 16),
    bg="green",
    fg="white",
    command=lambda: pagar()
)
btn_pagar.pack(pady=10)

# =========================
# 🔁 PAGAMENTO LOOP
# =========================


def verificar_pagamento():
    tempo_limite = 60
    tempo_restante = int(tempo_limite - (time.time() - inicio))

    if tempo_restante <= 0:
        label_status_pag.config(text="⛔ Tempo esgotado")
        root.after(3000, voltar_inicio)
        return

    status = backend.verificar_status(payment_id)

    label_timer_pag.config(text=f"⏳ {tempo_restante}s")
    label_status_pag.config(text=f"Status: {status}")

    if status == "approved":
        label_status_pag.config(text="✅ Pago! Liberando produto...")
        root.after(20000, voltar_inicio)
        return

    root.after(3000, verificar_pagamento)

# =========================
# 🔘 GRID PRODUTOS
# =========================


colunas = 3

for i, produto in enumerate(produtos):
    row = i // colunas
    col = i % colunas

    btn = Button(
        frame_center,
        text=f"{produto['codigo']}\n{produto['nome']}\nR${produto['preco']}",
        font=("Arial", 14),
        width=12,
        height=4,
        command=lambda p=produto: adicionar_carrinho(p)
    )

    btn.grid(row=row, column=col, padx=10, pady=10)
    botoes.append(btn)

root.mainloop()
