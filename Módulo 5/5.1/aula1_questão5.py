import emoji

# Dicionário de palavras para emojis (simples e direto)
mapa_emojis = {
    "amor": ":red_heart:",
    "amo": ":red_heart:",
    "chocolate": ":chocolate_bar:",
    "parabéns": ":partying_face:",
    "pensando": ":thinking_face:",
    "legal": ":thumbs_up:"
}

# Solicita a frase do usuário
frase_original = input("Digite uma frase e ela será emojizada automaticamente:\n")

# Substitui palavras por códigos emoji
frase_codificada = frase_original
for palavra, codigo in mapa_emojis.items():
    if palavra in frase_codificada.lower():
        frase_codificada = frase_codificada.replace(palavra, codigo)

# Emojiza a frase codificada
frase_emojizada = emoji.emojize(frase_codificada, language='alias')

print(frase_emojizada)
