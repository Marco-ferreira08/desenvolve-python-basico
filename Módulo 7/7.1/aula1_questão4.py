number = input("Digite o número: ")

if len(number) == 8:
    number = "9" + number
    fone_number = number[:5] + '-' + number[5:]
    print(f"Número completo do celular: {fone_number}")
elif len(number) == 9:
    if number[1] == "9": 
        fone_number = number[:5] + '-' + number[5:]
        print(f"Número completo do celular: {fone_number}")
    else:
        fone_number = number[:5] + '-' + number[5:]
        print(f"Número completo do telephone-fixo: {fone_number}")