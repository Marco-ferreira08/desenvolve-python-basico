import random

def imprime_enforcado(n_erro):
   n_erro += 1
   x = 6 * n_erro
   for i in range(x - 6,x,1):
        print(linhas[i].rstrip())

with open('gabarito_enforcado.txt', 'r') as f:
    linhas = f.readlines()

gabarito = linhas[random.randint(43, 52)].rstrip()
gabarito = list(gabarito)
undercores = ["_" for i in range(len(gabarito))]
tentativas = []
erros = 0
acertos = 0

imprime_enforcado(erros)
print(" ".join(undercores))
print("")

while erros < 6 and acertos < len(gabarito):
    palpite = input("Dê um palpite ").upper() 
    
    if not palpite.isalpha():
        print("Caractere inválido, digite uma letra!")
        print()

    elif len(palpite) > 1:
        print("Digite apenas uma única letra")
        print()

    elif palpite in tentativas:
        print("Você já tentou essa letra, tente novamente.")
        print(f"Tentativas: {', '.join(tentativas)}")

    elif palpite in gabarito:
        n = gabarito.count(palpite)
        for i in range(n):
            posicao = gabarito.index(palpite)
            undercores[posicao] = palpite
            gabarito[posicao] = "#"
            acertos += 1
        tentativas.append(palpite)
        print("Acertou!")
        print(" ".join(undercores))
        print("")

    else: 
        erros += 1
        tentativas.append(palpite)
        imprime_enforcado(erros)
        print("Letra errada")
        print(f"Tentativas: {', '.join(tentativas)}")

print("")
print("Fim de Jogo!")
if acertos == len(gabarito):
    print("Parabéns, você ganhou!")

else:
    print("Acabaram suas tentativas, você perdeu.")

        
