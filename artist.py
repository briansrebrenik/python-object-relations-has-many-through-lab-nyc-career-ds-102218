# remeber to import the Song class here
from song import Song

class Artist:

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        self._name = name

    def songs(self):
        return [song.name for song in Song._all if song.artist == self]

    def genres(self):
        return [song.genre for song in Song._all if song.artist == self]
