# AND = Retorna TRUE se todas as condições forem TRUE
# OR = Retorna TRUE se pelo menos uma condição for TRUE
# NOT = Inverte o resultado da condição

saldo = 1000
saque = 200
limite = 100

saldo >= saque and saque <= limite
# >>> False

saldo >= saque or saque <= limite
# >>> True

not 1000 > 1500
# >>> True
