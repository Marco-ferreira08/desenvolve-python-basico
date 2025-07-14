import random

def embaralhar_palavras(phrase):
    letter_list = []
    broken_phrase = phrase.split()
    word_list = [list(i) for i in broken_phrase]
    for word in word_list:
        letter_list.append(list(word))
    
    ordened_frags = [[i[0], "".join(sorted(i[1:-1], key=lambda x: random.random())), i[-1]] if len(i) 
                                    > 3 else i for i in word_list]
    
    ordened_words = ["".join(i) for i in ordened_frags]
    ordened_phrase = " ".join(ordened_words)
    return ordened_phrase

print("Digite uma frase: ")
frase = input("")
result = embaralhar_palavras(frase)
print("Frase embaralhada: ")
print(result)
                     
