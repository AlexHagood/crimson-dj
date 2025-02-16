import requests
import spotipy
import time
from spotipy.oauth2 import SpotifyClientCredentials

class SpotifyHandler():

    def __init__(self, clientId, clientSecret):
        self.clientId = clientId
        self.clientSecret = clientSecret
        self.authenticationToken = None
        self.getAuthenticationToken()
        self.sp = spotipy.Spotify(auth=self.authenticationToken)
    """
        Refreshes The Authentication Token
    """
    def getAuthenticationToken(self):

        TOKEN_URL = "https://accounts.spotify.com/api/token"

        payload = {
            "grant_type": "client_credentials",
            "client_id": self.clientId,
            "client_secret": self.clientSecret
        }

        # Headers
        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }

        response = requests.post(TOKEN_URL, data=payload, headers=headers)

        if response.status_code == 200:
            access_token = response.json().get("access_token")

        self.authenticationToken=access_token
        self.tokenDie = time.time() + response.json().get("expires_in")

    """
        Refreshes The Authentication Token if beyond expire time
    """
    def refreshAuthenticationToken(self):
        
        if self.tokenDie >= time.time():
            self.getAuthenticationToken()

    """
        Gets The Recommended Song from genre
    """
    def getRecommendedSongSeed(self, genreList):

        self.refreshAuthenticationToken()

        print(self.authenticationToken)

        # print(self.sp.me())

        # print(self.sp.recommendations(seed_genres=genreList, limit=10))

        # # Parse and print results
        # if response.status_code == 200:

        #     recommendations = response.json()
        #     for i, track in enumerate(recommendations["tracks"], 1):
        #         print(f"{i}. {track['name']} by {', '.join(artist['name'] for artist in track['artists'])}")

        # else:
        #     print("Error:", response.json())

CLIENT_ID = "406941e40d6a47be81bc631cef061c37"
CLIENT_SECRET = "bb36fc6a8b404925a4e3379a5cc6be70"

# REDIRECT_URI = "http://localhost:8080"

# # Set the required scopes for user authentication
# scope = "user-read-private user-read-email"

# from spotipy.oauth2 import SpotifyOAuth

# # Use SpotifyOAuth for user authentication
# auth_manager = SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=REDIRECT_URI, scope=scope)

# # Create the Spotify client with user authentication
# spotify = spotipy.Spotify(auth_manager=auth_manager)

# # Fetch user information
# print(spotify.me())

# handler.getRecommendedSongSeed(["Pop"])

# import spotipy
# import spotipy.util as util
# import random


# token = spotipy.oauth2.SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET).get_access_token()

# token = util.oauth2.SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)

# cache_token = token.get_access_token()