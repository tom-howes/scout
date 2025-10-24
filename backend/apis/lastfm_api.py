from dotenv import load_dotenv
import os
import requests


load_dotenv()

# Retrieve API key from env variables
API_KEY = os.environ.get("LASTFM_API_KEY")

# Query url
url = f"http://ws.audioscrobbler.com/2.0/?method=artist.getsimilar&artist=Radiohead&api_key={API_KEY}&format=json"

# Get request + jsonify
response = requests.get(url)
data = response.json()

# Print test output
for artist in data['similarartists']['artist'][:5]:
    print(artist['name'])