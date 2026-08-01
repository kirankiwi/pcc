def album_generator(album_title, artist, number_of_songs):
    album = {}
    album["album name"] = album_title.title()
    album["artist"] = artist.title()
    if number_of_songs:
        album["number of songs"] = number_of_songs
    return album
print(album_generator("Random Access Memories", "Daft Punk", ""))
while True:
    album_title = input("What is the name of the album?\n(enter q to quit.) ")
    if album_title == "q":
        break
    artist = input("What is the name of the artist?\n(enter q to quit.) ")
    if artist == "q":
        break
    number_of_songs = input("How many songs are in the album?\n(enter q to quit. This question is optional, so if you do not know, skip by pressing enter.) ")
    if number_of_songs == "q":
        break
    print(album_generator(album_title, artist, number_of_songs))