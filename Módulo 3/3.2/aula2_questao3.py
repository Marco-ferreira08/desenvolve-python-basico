idade = int(input("Digite sua idade: "))

    # - Se já jogou pelo menos 3 jogos de tabuleiro;
print("Você já jogou, pelo menos, três jogos de tabuleiro? ")
experiencia = bool(input("Responda 'True' caso sim, ou 'False' caso não: "))

    # - Número de jogos que venceu.
vitorias = int(input("Quantos jogos você já venceu? "))

# Saída de dados: Se o usuário é apto ou não para ingressar no clube
print(f"Apto para ingressar no clube de jogos de tabuleiro: {15 < idade < 19 and experiencia == True and vitorias >= 1}")