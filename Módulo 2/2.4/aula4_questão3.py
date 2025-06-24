# Solicita o nome do primeiro produto
produto1 = input("Digite o nome do produto 1:")

# Solicita o preço unitário do primeiro produto (valor float)
preco1 = float(input("Digite o preço unitário do produto 1:"))

# Solicita a quantidade do primeiro produto (valor inteiro)
quant1 = int(input("Digite a quantidade do produto 1:"))

# Solicita o nome do segundo produto
produto2 = input("Digite o nome do produto 2:")

# Solicita o preço unitário do segundo produto
preco2 = float(input("Digite o preço unitário do produto 2:"))

# Solicita a quantidade do segundo produto
quant2 = int(input("Digite a quantidade do produto 2:"))

# Solicita o nome do terceiro produto
produto3 = input("Digite o nome do produto 3:")

# Solicita o preço unitário do terceiro produto
preco3 = float(input("Digite o preço unitário do produto 3:"))

# Solicita a quantidade do terceiro produto
quant3 = int(input("Digite a quantidade do produto 3:"))

# Calcula o total da compra: preço x quantidade de cada produto
total = (preco1 * quant1) + (preco2 * quant2) + (preco3 * quant3)

# Formata o total para o padrão brasileiro: vírgula como decimal, ponto como milhar
total_formatado = f"{total:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

# Exibe o total no formato correto
print(f"Total: R${total_formatado}")