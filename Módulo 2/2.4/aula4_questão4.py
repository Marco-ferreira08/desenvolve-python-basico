# Lê o valor inteiro a ser convertido em notas
valor = int(input())

# Calcula a quantidade de notas de 100
nota100 = valor // 100
valor = valor % 100

# Calcula a quantidade de notas de 50
nota50 = valor // 50
valor = valor % 50

# Calcula a quantidade de notas de 20
nota20 = valor // 20
valor = valor % 20

# Calcula a quantidade de notas de 10
nota10 = valor // 10
valor = valor % 10

# Calcula a quantidade de notas de 5
nota5 = valor // 5
valor = valor % 5

# Calcula a quantidade de notas de 2
nota2 = valor // 2
valor = valor % 2

# O que restar agora só pode ser nota de 1 real
nota1 = valor

# Exibe o resultado no formato especificado
print(f"{nota100} nota(s) de R$100,00")
print(f"{nota50} nota(s) de R$50,00")
print(f"{nota20} nota(s) de R$20,00")
print(f"{nota10} nota(s) de R$10,00")
print(f"{nota5} nota(s) de R$5,00")
print(f"{nota2} nota(s) de R$2,00")
print(f"{nota1} nota(s) de R$1,00")