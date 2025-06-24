# Solicita ao usuário que digite a temperatura em graus Fahrenheit (valor inteiro)
fahrenheit = int(input("Digite a temperatura em graus Fahrenheit: "))

# Converte a temperatura de Fahrenheit para Celsius usando a fórmula fornecida
celsius = (fahrenheit - 32) * (5 / 9)

# Converte o valor em Celsius para inteiro, conforme solicitado no enunciado
celsius_inteiro = int(celsius)

# Exibe a temperatura convertida no formato especificado
print(f"{fahrenheit} graus Fahrenheit são {celsius_inteiro} graus Celsius.")