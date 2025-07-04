# Entrada: Número de Experiências
n = int(input("Digite o número de experiências realizadas durante o ano: "))
cont = 0
frogs, rats, rabbits, total = 0, 0, 0, 0

# Processamento: Interações com o usário
while cont < n: 
    quantity = int(input(f"Digite o número de cobaias usadas na experiência {cont +1}: "))
    type = input("Digite o tipo de cobaia: ")
    total += quantity

    if type == "S":
        frogs += quantity
    
    elif type == "R":
        rats += quantity

    elif type == "C":
        rabbits += quantity

    else:
        print("Tipo inválido! Repetindo operação...")
        cont -= 1  

    cont += 1

# Saída: Total de Cobaias, total e porcentagem de coelhos, de ratos e de sapos
print(f"Total: {total}")
print(f"Total de coelhos: {rabbits}")
print(f"Total de ratos: {rats}")
print(f"Total de sapos: {frogs}")
print(f"Percentual de coelhos: {(rabbits / total) * 100: .2f}%")
print(f"Percentual de ratos: {(rats / total) * 100: .2f}%")
print(f"Percentual de sapos: {(frogs / total) * 100: .2f}%")