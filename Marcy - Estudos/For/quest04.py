# 04. Crie um código em Python que use o comando for para percorrer de 0 até n (inclusive) números e calcule a média aritmética desses valores.

n = int(input('Digite um número: '))
soma = 0
contador = 0
for a in range(0, n + 1 ):
    soma += a
    contador += 1

media = soma / contador
print(f'Sua média aritmética é igual a : {media}') 
