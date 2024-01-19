class Song:
    def __init__(self, title, artist, album, genre, length):
        self.title, self.artist, self.album, self.genre, self.length = title, artist, album, genre, length

class MusicLibrary:
    def __init__(self):
        self.song_list = {}

    def add_song(self, song):
        key = f"{song.title} - {song.artist}"
        if key not in self.song_list:
            self.song_list[key] = song

    def add_songs(self, songs):
        for song in songs:
            self.add_song(song)

    def get_songs_by_artist(self, artist):
        return '\n'.join([f"{song.title} - {song.album}" for song in self.song_list.values() if song.artist == artist])

    def get_songs_by_album(self, album):
        return '\n'.join([f"{song.title} - {song.artist}" for song in self.song_list.values() if song.album == album])

    def get_songs_by_genre(self, genre):
        return '\n'.join([f"{song.title} - {song.artist}" for song in self.song_list.values() if song.genre == genre])

    def get_songs_by_title(self, title):
        return '\n'.join([f"{song.album} - {song.artist}" for song in self.song_list.values() if song.title == title])

    def display_all_songs(self):
        return '\n'.join([f"{song.title} - {song.artist}" for song in self.song_list.values()])

class Playlist:
    def __init__(self, name):
        self.name = name
        self.song_list = []

    def add_song(self, song):
        if song not in self.song_list:
            self.song_list.append(song)

    def add_songs(self, songs):
        for song in songs:
            self.add_song(song)

    def remove_song(self, song):
        if song in self.song_list:
            self.song_list.remove(song)

    def reorder_songs(self, song, index):
        if song in self.song_list:
            self.song_list.remove(song)
            self.song_list.insert(index, song)

    def display_playlist(self):
        return '\n'.join([f"{song.title} - {song.artist}" for song in self.song_list])
