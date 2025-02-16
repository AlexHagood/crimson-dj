import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
from dotenv import load_dotenv
from os import getenv


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
    
    
c = player()
print(c.getSongName())