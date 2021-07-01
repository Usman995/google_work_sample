"""A video player class."""
import random

from .video_library import VideoLibrary
from .video_playlist import Playlist


class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self.is_playing = False
        self.playing_title = "None"
        self.is_paused = False
        self.current_video_id = "None"

    def video_name(self, video_id):
        video = self._video_library.get_video(video_id)
        return video.title

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        list_names_videos = self._video_library.get_all_videos()
        temp_list = []
        print("Here's a list of all available videos:")
        for elem in list_names_videos:
            tags = "["
            for tag in elem.tags:
                tags = tags + tag + " "
            tags = tags + "]"
            if tags != "[]":
                tags = tags[0:len(tags) - 2] + "]"
            temp_list += [f"{elem.title} ({elem.video_id}) {tags}"]

        sorted_list = sorted(temp_list)
        for x in sorted_list:
            print(x)

    def play_video(self, video_id):

        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """
        currently_playing = self._video_library.get_video(video_id)
        try:
            temp = currently_playing.title
            if self.is_playing is not True:
                print(f"Playing video: {temp}")
                self.is_playing = True
                self.is_paused = False
                self.current_video_id = video_id
            else:
                print(f"Stopping video: {self.video_name(self.current_video_id)}")
                print(f"Playing video: {temp}")
                self.current_video_id = video_id
                self.is_paused = False
        except:
            print("Cannot play video: Video does not exist")

    def stop_video(self):
        """Stops the current video."""
        if self.is_playing is True:
            print("Stopping video: " + self.video_name(self.current_video_id))
            self.is_playing = False
        else:
            print(f"Cannot stop video: No video is currently playing")

    def play_random_video(self):

        """Plays a random video from the video library."""
        currently_playing = random.choice(self._video_library.get_all_videos())

        if self.is_playing is False:
            print("Playing video: " + currently_playing.title)
            self.current_video_id = currently_playing.video_id
            self.is_playing = True
        elif self.is_playing is True:
            print(f"Stopping video: " + self.video_name(self.current_video_id))
            print("Playing video: " + currently_playing.title)
            self.playing_title = currently_playing.title

    def pause_video(self):
        """Pauses the current video."""

        if self.is_playing is True:

            if self.is_paused is True:
                print(f"Video already paused: " + self.video_name(self.current_video_id))
            else:
                print("Pausing video: " + self.video_name(self.current_video_id))
                self.is_paused = True
        else:
            print(f"Cannot pause video: No video is currently playing")

    def continue_video(self):
        """Resumes playing the current video."""

        if self.is_playing is True:
            if self.is_paused is False:
                print(f"Cannot continue video: Video is not paused")
            else:
                print(f"Continuing video: {self.video_name(self.current_video_id)}")
        else:
            print("Cannot continue video: No video is currently playing")

    def show_playing(self):
        """Displays video currently playing."""
        temp_list = []
        if self.is_playing:
            currently_playing = self._video_library.get_video(self.current_video_id)
            tags = "["
            for tag in currently_playing.tags:
                tags = tags + tag + " "
            tags = tags
            if tags != "[]":
                tags = tags[0:len(tags) - 1] + "]"
            if self.is_paused:
                print(f"Currently playing: {currently_playing.title} ({currently_playing.video_id}) {tags} - PAUSED")
            else:
                print(f"Currently playing: {currently_playing.title} ({currently_playing.video_id}) {tags}")
        else:
            print(f"No video is currently playing")

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        playlist = Playlist(playlist_name)
        name = playlist.playlist_name()
        if playlist.search_playlist(name) is True:
            print(f"Successfully created new playlist: {name}")
        else:
            print(f"Cannot create playlist: A playlist with the same name already exists")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        print("add_to_playlist needs implementation")

    def show_all_playlists(self):
        """Display all playlists."""

        print("show_all_playlists needs implementation")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
