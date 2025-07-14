import re

with open('frase.txt', 'r') as file:
    phrase = file.read()
    words = re.findall(r'[a-zA-Z]+', phrase)

with open('palavras.txt', 'w') as f1:
    for i in words:
        f1.write(str(i) + "\n")

with open('palavras.txt', 'r') as f2:
    text = f2.read()
    print(text)