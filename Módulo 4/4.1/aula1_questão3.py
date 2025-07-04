n1 , n2 , n3 = int(input("Digite o primeiro número: ")), int(input("Digite o segundo número: ")), int(input("Digite o terceiro número: "))
m = (n1 + n2 + n3) / 3

if m >= 60 and m < 90:
    print("Aprovado")
elif m >=40 and m < 60:
        print("Recuperação")
else:
    print("Reprovado")