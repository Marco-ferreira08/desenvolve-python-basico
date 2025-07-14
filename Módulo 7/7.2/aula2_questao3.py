while True:
    frase_original = input("Digite uma frase (digite 'fim' para encerrar): ")
    if frase_original.lower() == "fim":
        break

    frase_modificada = ''.join([i for i in frase_original if i.isalpha()])
    frase_modificada = frase_modificada.lower()

    if frase_modificada == frase_modificada[::-1]:
        print(f"'{frase_original}' é um palíndromo!")
    else:
        print(f"'{frase_original}' não é um palíndromo!")