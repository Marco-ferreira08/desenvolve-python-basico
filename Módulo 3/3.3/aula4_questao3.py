# Entrada de Dados:
    # É solicitado um ano para ser testado
year = int(input("Digite um ano e saiba de ele é bissexto ou não: "))

if ( (year % 4 == 0) and (year % 100 != 0) ) or (year % 400 == 0):
    print(f"O ano {year} é bissexto.")
else:
    print(f"O ano {year} não é bissexto.")