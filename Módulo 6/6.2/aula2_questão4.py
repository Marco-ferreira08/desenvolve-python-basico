lista1 = list()
lista2 = list()
inter = list()

def lista(tamanho, lista):
    for i in range(tamanho):
        (lista).append(int(input("")))

x = int(input("Digite a quantidade de elementos da lista 1: "))
print(f"Digite os {x} elementos da lista 1:")
lista(x, lista1)

y = int(input("Digite a quantidade de elementos da lista 2: "))
print(f"Digite os {y} elementos da lista 2:")
lista(y, lista2)

for item in range(min(len(lista1), len(lista2))):
    inter.append(lista1[item])
    inter.append(lista2[item])

if len(lista1) > len(lista2):
    inter.extend(lista1[len(lista2):])
else:
    inter.extend(lista2[len(lista1):])

print(inter)