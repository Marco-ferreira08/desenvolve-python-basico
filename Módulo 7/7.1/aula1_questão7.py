import random

def encrypt(names):
    n = random.randint(1, 10)
    encrypted_names = []

    for name in names:
        encrypted_name = ''
        for char in name:
            code = ord(char)
            if 33 <= code <= 126:
                new_code = 33 + ((code - 33 + n) % 94)
                encrypted_name += chr(new_code)
            else:
                encrypted_name += char
        encrypted_names.append(encrypted_name)

    return encrypted_names, n

def main():
    print("Digite os nomes para criptografar (pressione Enter em branco para finalizar):")
    names = []
    while True:
        name = input("Nome: ")
        if name.strip() == "":
            break
        names.append(name)

    if not names:
        print("Nenhum nome foi informado.")
        return

    encrypted_names, key = encrypt(names)

    print("\n🔐 Nomes criptografados:")
    for original, encrypted in zip(names, encrypted_names):
        print(f"{original} → {encrypted}")

    print(f"\n🗝️  Chave de criptografia usada: {key}")

if __name__ == "__main__":
    main()