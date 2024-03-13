# 02. Escreva um código em Python que utilize um laço for para imprimir os números de 1 a 15 (inclusive), mas pulando os números 5, 8 e 12.

for a in range(1, 16):
    if not(a == 5 or a == 8 or a == 12):
        print(a)