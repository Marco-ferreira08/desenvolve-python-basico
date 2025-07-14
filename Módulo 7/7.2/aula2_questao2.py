vogais =  ["A", "E","I", "O", "U", "a", "e", "i", "o", "u"]
frase = input("Digite uma frase: ")

for i in vogais:
    if i in frase:
        frase = frase.replace(i, "*")

print(f"Frase modificada: {frase}")