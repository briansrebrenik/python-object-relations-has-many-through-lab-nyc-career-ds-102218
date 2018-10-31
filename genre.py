# remeber to import the Song class here
from song import Song

class Genre:

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        self._name = name

    def songs(self):
        return[song.name for song in Song._all if song.genre == self]

    def artists(self):
        return[artist.name for song in Song._all if song.artist == self]
