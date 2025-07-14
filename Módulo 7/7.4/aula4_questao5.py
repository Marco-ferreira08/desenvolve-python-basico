# Lista com os dados dos livros: [Título, Autor, Ano de publicação, Número de páginas]
livros = [
    ["Prólogo, Ato e Epílogo", "Fernanda Montenegro", 2019, 312],
    ["Harry Potter e a Pedra Filosofal", "J.K. Rowling", 1997, 223],
    ["1984", "George Orwell", 1949, 328],
    ["Dom Casmurro", "Machado de Assis", 1899, 256],
    ["O Pequeno Príncipe", "Antoine de Saint-Exupéry", 1943, 96],
    ["A Revolução dos Bichos", "George Orwell", 1945, 112],
    ["A Menina que Roubava Livros", "Markus Zusak", 2005, 480],
    ["O Senhor dos Anéis: A Sociedade do Anel", "J.R.R. Tolkien", 1954, 576],
    ["Capitães da Areia", "Jorge Amado", 1937, 272],
    ["Grande Sertão: Veredas", "João Guimarães Rosa", 1956, 624]
]

# Criação do arquivo CSV
with open("meus_livros.csv", "w", encoding="utf-8") as arquivo:
    # Escreve o cabeçalho
    arquivo.write("Título,Autor,Ano de publicação,Número de páginas\n")
    
    # Escreve os dados dos livros
    for livro in livros:
        linha = f"{livro[0]},{livro[1]},{livro[2]},{livro[3]}\n"
        arquivo.write(linha)

print("Arquivo 'meus_livros.csv' criado com sucesso!")