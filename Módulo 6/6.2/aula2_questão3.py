import random
lista1 = []
lista2 = []
interseccao = []

for i in range(20):
    lista1.append(random.randint(0, 50))
    lista2.append(random.randint(0, 50))

for i in lista1:
    if i in lista2 and i not in interseccao:
        interseccao.append(i)


print(f"lista1 - {lista1}")
print(f"lista2 - {lista2}")
print(f"Intersecção - {interseccao}")
print("Contagem: ")
for i in interseccao:
    print(f"{i}: (Lista1={lista1.count(i)}, lista2={lista2.count(i)}) ")