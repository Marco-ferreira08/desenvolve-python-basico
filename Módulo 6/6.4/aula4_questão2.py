vogais = ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u"]

frase = input("Digite uma frase: ")

# Criação da lista de caracteres
frase_lista = list(frase)

# Lista de vogais ordenada
frase_vogais = sorted([i for i in frase_lista if i in vogais])

# Lista de consoantes, removendo espaços
frase_consoantes = [i for i in frase_lista if i not in vogais and i != ' ']

# Impressão com interpolação correta
print(f"Vogais: {frase_vogais}")
print(f"Consoantes: {frase_consoantes}")