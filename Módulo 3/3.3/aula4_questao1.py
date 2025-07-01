print("Me entregue dois números e eu irei dizer se a soma deles é par ou ímpar.")
x = int(input("Digite um número: "))
y = int(input("Agora digite outro número: "))

soma = x + y

if (x + y) % 2 == 0:
    print(f"A soma de {x} com {y} é {x + y}, que é par.")
else:
    print(f"A soma de {x} com {y} é {x + y}, que é ímpar.")