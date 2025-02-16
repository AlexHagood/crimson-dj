import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
from dotenv import load_dotenv
from os import getenv
import os

os.environ["SPOTIPY_CLIENT_ID"] = "54c3af9ee0574979847913da5d2bad92"
os.environ["SPOTIPY_CLIENT_SECRET"] = "f7409833b90b45b789936f47b1d39983"
os.environ["SPOTIPY_REDIRECT_URI"] = "http://google.com/callback/"

load_dotenv()

client_id = os.getenv('SPOTIPY_CLIENT_ID')
client_secret = os.getenv('SPOTIPY_CLIENT_SECRET')
redirect = os.getenv('SPOTIPY_REDIRECT_URI')


class player():
    def __init__(self):
        scope = "user-read-private user-read-email user-modify-playback-state user-read-playback-state"
        auth_manager = SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect, scope=scope)
        self.sp = spotipy.Spotify(auth_manager=auth_manager)
    def play(self):
        self.sp.start_playback()
    def pause(self):
        self.sp.pause_playback()
    def getSongName(self):
        return self.sp.current_playback().get("item").get("name")
    def timeToAddSongToQueue(self):
        playback  = self.sp.current_playback()
        track_duration = playback["item"]["duration_ms"]  # Total duration in ms
        progress = playback["progress_ms"]  # Current position in ms
        if (track_duration - progress) > 30000:
            return False
        return True

    def addSongToQueue(self, themes):

        results = self.sp.search(q=themes, limit=1, type='track')
        if results:
            if "tracks" in results.keys():
            
                c = results["tracks"]["items"][0]["id"]
                self.sp.add_to_queue(c)
                print(c)
        
                # album = self.sp.album("42D7ruMnjM6a8FkXkxPDzT") #results["tracks"]["href"]
                # results["tracks"]["href"]
                # print(album)
        # print(results)