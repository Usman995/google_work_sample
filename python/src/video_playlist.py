"""A video playlist class."""


class Playlist:
    """A class used to represent a Playlist."""
    def __init__(self, name):

        self.name = name
        self.playlists_names = {}

    def search_playlist(self, x):
        if x not in self.playlists_names.values():
            self.playlists_names = {"Playlist": x}
            return True

        else:
            return False

    def playlist_name(self):
        return self.name
