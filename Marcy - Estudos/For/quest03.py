# Crie um programa em Python que imprima a soma dos números pares de 0 até um número inteiro dado pelo usuário. 
# Utilize o comando for para percorrer os números e realizar a soma.

n = int(input('Digite um número: '))
soma = 0

for a in range(0, n + 1, 2):
    soma += a
print(soma)