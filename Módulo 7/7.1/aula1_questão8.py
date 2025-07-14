def funcMultiplica(mult):
    for n in numeros:
        multiplicados.append(n * mult)
        mult -= 1

def funcSomaDiv(lista_m):
    x = 0
    for i in lista_m:
        x += i
    return x % 11

multiplicados = []
cpf = input("Digite o CPF: ")

numeros = [int(i) for i in cpf[:-3:1] if (i != '.' and i !='-')]


funcMultiplica(10)
resultado = funcSomaDiv(multiplicados)

if resultado < 2:
    digito1 = 0
elif resultado >= 2:
    digito1 = 11 - resultado
numeros.append(digito1)

multiplicados.clear()
funcMultiplica(11)
resultado = funcSomaDiv(multiplicados)

if resultado < 2:
    digito2 = 0
elif resultado >= 2:
    digito2 = 11 - resultado
numeros.append(digito2)

numeros = [str(i) for i in numeros]
numeros_str = "".join(numeros)
cpf_teste = numeros_str[:3] + "." + numeros_str[3:6] + "." + \
    numeros_str[6:9] + "-" + numeros_str[-2::]

if cpf == cpf_teste:
    print("CPF Válido! Acesso permitido.")
else:
    print("CPF Inválido! Acesso negado! ")