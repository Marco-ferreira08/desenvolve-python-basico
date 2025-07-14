def encontrar_anagramas(palavra, string):
    from collections import Counter
    
    palavra_counter = Counter(palavra)
    anagramas = []
    
    for i in range(len(string) - len(palavra) + 1):
        substring = string[i:i + len(palavra)]
        if Counter(substring) == palavra_counter:
            anagramas.append(substring)
    
    return anagramas

print ("Digite a palavra objetivo:")
palavra_objetivo = input().strip()
print ("Digite a string para buscar anagramas:")
string_para_busca = input().strip()

anagramas_encontrados = encontrar_anagramas(palavra_objetivo, string_para_busca)
print("Anagramas encontrados:", anagramas_encontrados)