n = int(input("Digite o número de respondentes da pesquisa: "))
cont = 1
idades = 0

while cont <= n:
    idades += int(input(f"Digite a idade do {cont}⁰ respondente: " ))
    cont += 1

print (f"A média de idade dos respondentes é {idades / n:.0f}")