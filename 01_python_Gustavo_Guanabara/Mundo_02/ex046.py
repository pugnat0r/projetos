# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício,
# indo de 10 até 0, com uma pausa de 1 segundo entre eles.
# importando a biblioteca time para usar a função sleep

import time
from click import clear
from art import tprint

for c in range(10, 0, -1):
    clear()
    txt = str(c)
    tprint(txt)
    time.sleep(1)

tprint("FOGOS", font="block", chr_ignore=True)
time.sleep(2)
clear()
clear()
tprint("FO", font="block", chr_ignore=True)
time.sleep(2)
clear()
tprint("FOGOSSSS", font="block", chr_ignore=True)
tprint("FOGOSSSS", font="block", chr_ignore=True)
tprint("FOGOSSSS", font="block", chr_ignore=True)
tprint("FOGOSSSS", font="block", chr_ignore=True)
tprint("FOGOSSSS", font="block", chr_ignore=True)
time.sleep(2)
clear()
