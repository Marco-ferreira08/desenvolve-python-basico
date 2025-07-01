print("Bem-vindo ao Sistema de Classificação de Filmes!")

# Solicita a avaliação do usuário
try:
    classificacao = int(input("Digite a avaliação do filme (1 a 5): "))

    # Dicionário com as mensagens correspondentes
    mensagens = {
        1: "Ruim.",
        2: "Regular.",
        3: "Bom!",
        4: "Muito Bom!",
        5: "Excelente!"
    }

    # Verifica se a classificação está entre 1 e 5
    if 1 <= classificacao <= 5:
        print(mensagens[classificacao])
    else:
        print("Por favor, insira um número entre 1 e 5.")

except ValueError:
    print("Entrada inválida. Por favor, digite um número inteiro.")