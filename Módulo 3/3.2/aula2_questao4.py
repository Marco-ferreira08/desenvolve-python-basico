print("Escolha a classe (guerreiro, mago ou arquiro)")
classe = input("Digite o nome com todas as letras em caixa baixa: ")
forca = int(input("Digite os pontos de força (de 1 a 20): "))
magia = int(input("Digite os pontos de magia (de 1 a 20): "))

# Processamento: Verifica se os pontos de atributo são consistentes com a classe escolhida
guerreiro = classe == "guerreiro" and forca >= 15 and magia <= 10
mago = classe == "mago" and forca <= 10 and magia >= 15
arqueiro = "arqueiro" and (5 <= forca <= 15) and (5 <= magia <= 15)

print (f"Pontos de atributo consistentes com a classe escolhida: {(guerreiro or mago or arqueiro)}")