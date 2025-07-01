print("Bem-vindo ao Sistema de Entrega Expressa!")

try:
    # Solicita os dados ao usuário
    distancia = float(input("Digite a distância da entrega (em km): "))
    peso = float(input("Digite o peso do pacote (em kg): "))

    # Define o valor base por kg de acordo com a distância
    if distancia <= 100:
        valor_por_kg = 1.00
    elif distancia <= 300:
        valor_por_kg = 1.50
    else:
        valor_por_kg = 2.00

    # Calcula o valor base do frete
    frete = peso * valor_por_kg

    # Aplica taxa adicional se o peso for superior a 10 kg
    if peso > 10:
        frete += 10.00

    # Exibe o valor final do frete
    print(f"O valor do frete é: R${frete:.2f}")

except ValueError:
    print("Entrada inválida. Por favor, digite números válidos para distância e peso.")