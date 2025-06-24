# area_m2 = comprimento * largura
# preco_total = preco_m2 * area_m2

# Solicita ao usuário que digite o comprimento do terreno em metros (valor inteiro)
comprimento = int(input("Digite o comprimento do terreno (em metros): "))

# Solicita ao usuário que digite a largura do terreno em metros (valor inteiro)
largura = int(input("Digite a largura do terreno (em metros): "))

# Solicita ao usuário que digite o preço do metro quadrado da região (valor com ponto flutuante)
preco_m2 = float(input("Digite o preço do metro quadrado (em R$): "))

# Calcula a área total do terreno
area_m2 = comprimento * largura

# Calcula o preço total do terreno
preco_total = preco_m2 * area_m2

# Formata o valor do preço total para o padrão brasileiro (vírgula como separador decimal)
preco_formatado = f"{preco_total:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

# Exibe a área e o custo total do terreno no formato desejado
print(f"O terreno possui {area_m2}m2 e custa R${preco_formatado}")
