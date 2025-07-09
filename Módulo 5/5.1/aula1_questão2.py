#Escreva um código que gere n valores inteiros aleatórios entre 0 e 100 e calcule a raíz quadrada da soma dos valores. Peça ao usuário o valor de n

import math as mt, random as rd

n = int(input("Digite o valor de n: "))
soma = 0
for _ in range(n):
    valor = rd.randint(0, 100)
    soma += valor
resultado = mt.sqrt(soma)
print(f"A raiz quadrada da soma dos {n} valores aleatórios é: {resultado}")
