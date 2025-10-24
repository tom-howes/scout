import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
import os

load_dotenv()

# Retrieve env variables for API keys
CLIENT_ID = os.environ.get("SPOTIFY_CLIENT_ID")
CLIENT_SECRET = os.environ.get("SPOTIFY_CLIENT_SECRET")

# Initialize spotipy instance
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET
))

# Testing search results
results = sp.search(q="Radiohead", type='artist', limit=1)
radiohead = results['artists']['items'][0]
print(radiohead)
print(f"Artist: {radiohead['name']}")
print(f"ID: ", {radiohead['id']})
print(f"Followers: {radiohead['followers']['total']}")

tracks = sp.artist_top_tracks(radiohead['id'])
print("Top Tracks:\n______")
for track in tracks['tracks']:
    print(track['name'])