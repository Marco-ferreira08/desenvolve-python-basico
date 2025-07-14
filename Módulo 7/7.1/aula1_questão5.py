vogais = []
n_vogais = 0
frase = input("Digite uma frase: ")

for i in range(len(frase)):
    if frase[i] in "AEIOUaeiou":
        n_vogais += 1
        vogais.append(i)
print(f"A frase tem {n_vogais} vogais")
print(f"Índices: {vogais}")