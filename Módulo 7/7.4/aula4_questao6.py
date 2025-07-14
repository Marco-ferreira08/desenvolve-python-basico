# Você deve criar um script Python para processar esse arquivo e gerar 
# uma lista com 10 elementos, cada qual representando a música mais tocada 
# de cada ano no intervalo de 2012 a 2022. Considere somente músicas dentro 
# do intervalo solicitado. Cada elemento da lista produzida deve conter as 
# seguintes informações:

    # - [track_name, artist(s)_name, released_year, streams]

# Essa atividade tem alguns desafios. Assim como as colunas da tabela são 
# separadas por vírgulas, músicas com mais de um artista (artist_count>1) 
# terá o campo artist(s)_name entre aspas com o nome dos artistas separado por 
# vírgulas. 

# Há também nomes de músicas entre aspas por conter caracteres especiais como 
# vírgulas ou aspas. 

# Você deve ignorar essas linhas, e terá portanto que propor uma verificação 
# para identificá-las.

# Ao final imprima a lista produzida. Ex:
    # [ ['When I Was Your Man', 'Bruno Mars', 2012, 1661187319],
    #  ['I Wanna Be Yours', 'Arctic Monkeys', 2013, 1297026226], 


import csv

def verify_most_popular(popular, current_music):



    if popular is None:
        return current_music
    elif int(current_music[8]) > int(popular[8]):
        return current_music
    else:
        return popular


with open("spotify-2023.csv", "r", encoding='latin-1') as f:
    reader = csv.reader(f)
    header = next(reader)


    safe_list = []

    for line in reader:

        if '"' in line[0] or '"' in line[1] or '"' in line[3]:
            continue


        safe_list.append(line)


most_popular_songs = []

for year in range(2012, 2023):
    most_popular = None
    for music in safe_list:
        if music[3] == str(year):
            most_popular = verify_most_popular(most_popular, music)

    if most_popular:
        most_popular_songs.append([most_popular[0], most_popular[1], int(most_popular[3]), int(most_popular[8])])

print("Música, Autor, Ano de Lançamento, Número de vezes tocada")
for song in most_popular_songs:

    print(song)


