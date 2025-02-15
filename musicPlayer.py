
# # Authenticate
# sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="5c346f6ca2124df9ab63bc476a9af418",
#                                                client_secret="ea287964c0cf415ea45bff09135af98c",
#                                                redirect_uri="http://localhost"))

# # SPOTIPY_CLIENT_ID = "5c346f6ca2124df9ab63bc476a9af418"
# # CLIENT_SECRET = "ea287964c0cf415ea45bff09135af98c"
# # REDIRECT_URI = "http://localhost:8080"

import os
import random
import requests
import string
import urllib
from spotipy.oauth2 import SpotifyOAuth

# Spotify API credentials
CLIENT_ID = "your_client_id"
CLIENT_SECRET = "your_client_secret"
REDIRECT_URI = "http://localhost:8080"

# Define the scope (modify as needed)
SCOPE = "user-read-playback-state user-modify-playback-state user-read-currently-playing"

requests.post()

# # Authenticate and get token
# sp_oauth = SpotifyOAuth(client_id=CLIENT_ID,
#                         client_secret=CLIENT_SECRET,
#                         redirect_uri=REDIRECT_URI,
#                         scope=SCOPE)

# token_info = sp_oauth.get_access_token(as_dict=True)
# access_token = token_info['access_token']
# print(access_token)


# class SpotifyClient(object):
# 	def __init__(self, api_token):
# 		self.api_token = api_token

# 	def get_random_tracks(self):
# 		wildcard = f'%{random.choice(string.ascii_lowercase)}%'
# 		query = urllib.parse.quote(wildcard)
# 		offset = random.randint(0, 2000)
# 		url = f"https://api.spotify.com/v1/search?q={query}&offset={offset}&type=track"
# 		response = requests.get(
# 			url,
# 			headers={
# 				"Content-Type": "application/json",
# 				"Authorization": f"Bearer {self.api_token}"
# 			}
# 		)
# 		response_json = response.json()

# 		# tracks = [
# 		# 	track for track in response_json['tracks']['items']
# 		# ]
# 		print(response_json)

# 		# print(f'Found {len(tracks)} tracks to add to your library')

# 		# return tracks


# 	def add_tracks_to_library(self, track_ids):
# 		url = "https://api.spotify.com/v1/me/tracks"
# 		response = requests.put(
# 			url,
# 			json={
# 				"ids": track_ids
# 			},
# 			headers={
# 				"Content-Type": "application/json",
# 				"Authorization": f"Bearer {self.api_token}"
# 			}
# 		)
		
# 		return response.ok

# def run():
	
#     token = os.getenv('SPOTIFY_AUTH_TOKEN')
#     print(token)
	
#     spotify_client = SpotifyClient(os.getenv('SPOTIFY_AUTH_TOKEN'))
#     random_tracks = spotify_client.get_random_tracks()
# 	# track_ids = [track['id'] for track in random_tracks]

# 	# was_added_to_library = spotify_client.add_tracks_to_library(track_ids)
# 	# if was_added_to_library:
# 	# 	for track in random_tracks:
# 	# 		print(f"Added {track['name']} to your library")


# if __name__ == '__main__':
# 	run()

