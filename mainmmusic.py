from MusicLibrary import Song, Playlist,MusicLibrary

# Songs
songs = [
    Song("Lovin On Me", "Jack Harlow", "Lovin On Me", "Rap", "2:18"),
    Song("redrum", "21 Savage", "american dream", "Rap", "4:31"),
    Song("Dancing with my phone", "HYBS", "Making Steak", "Pop", "3:24"),
    Song("Tip Toe", "HYBS", "Tip Toe", "Pop", "3:45"),
    Song("Too Many Nights", "Metro Boominn", "HEROES & VILLAINS", "Rap", "3:20"),
    Song("Agora Hills", "Doja Cat", "Scarlet", "R&B", "4:25"),
    Song("Superhero", "Metro Boomin", "HEROES & VILLAINS", "Rap", "3:02"),
    Song("Paint The Town Red", "Doja Cat", "Scarlet", "R&B", "3:50"),
    Song("So High", "Doja Cat", "So High", "R&B", "3:22"),
]
# Title, Artist, Album, Genre, Length

library = MusicLibrary()
library.add_songs(songs)

# Songs by Doja Cat
print("Songs by Doja Cat:")
print(library.get_songs_by_artist("Doja Cat"))
print()

# Songs in album
print("Songs in HEROES & VILLAINS album:")
print(library.get_songs_by_album("HEROES & VILLAINS"))
print()

# Rap Songs
print("Songs in Rap:")
print(library.get_songs_by_genre("Rap"))
print()

# Create playlist and add songs in playlist
playlist = Playlist("Beatz")
playlist.add_songs([songs[1], songs[2], songs[4], songs[6], songs[8]])
playlist.add_song(songs[7])
playlist.remove_song(songs[3])
playlist.reorder_songs(songs[7], 1)

# All Songs
print("Songs in the library:")
print(library.display_all_songs())

# All Songs in Playlist
print(f"\nSongs in {playlist.name} playlist:")
print(playlist.display_playlist())