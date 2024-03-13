# 05. Crie um programa para verificar se um número é primo ou não. Utilize o comando for.

n = int(input('Digite um número: '))
contador = 0

for a in range(1, n + 1):
    if a % n == 0:
        contador += 1
   

if contador == 2 :
    print("Seu número é primo")
else:
    print("Seu número não é primo")

