import os

frase = input("Digite uma frase: ")
f = open('frase.txt', 'w')
f.write(frase)
f.close()
caminho = os.path.abspath('frase.txt')
print(f"Frase salva em {caminho}")

