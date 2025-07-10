lista = []

a = int(input("Escreva o tamanho da lista (mínimo = 4): "))
if a < 4:
    a = 4


for i in range(a):
    lista.append(int(input("")))

print(lista)
print(lista[:2:])
print(lista[(a - 2)::])
print(lista[::-1])
print(lista[::2])
print(lista[1::2])