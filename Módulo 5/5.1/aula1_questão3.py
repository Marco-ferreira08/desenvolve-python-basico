import random as rd 

valor = rd.randint(1, 10)
palpite = ()
chute = 1

while palpite != valor:
    palpite = int(input("Adivinhe o número entre 1 e 10: "))
    if palpite < valor:
        print("Muito baixo!")
    elif palpite > valor:
        print("Muito alto!")
    else:
        print("Correto!")
        break
    chute += 1
print ("Você acertou o número com", chute, "chutes.")