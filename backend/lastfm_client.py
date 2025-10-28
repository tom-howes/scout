import requests
import os
from dotenv import load_dotenv

load_dotenv()

class LastFmClient:
    def __init__(self):
        self.api_key = os.getenv("LASTFM_API_KEY")
        self.base_url = "http://ws.audioscrobbler.com/2.0/"
    
    def get_similar_artists(self, artist_name, limit=20):
        """
        Get a list of similar artists from Last.fm

        limit: max # of similar artists to return
        """

        params = {
            'method' : 'artist.getsimilar',
            'artist' : artist_name,
            'api_key' : self.api_key,
            'format' : 'json',
            'limit' : limit
        }

        try:
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()

            data = response.json()

            if 'similarartists' not in data:
                print(f"No similar artists found for {artist_name}")
                return []
            
            similar_artists = data['similarartists']['artist']

            artist_names = [artist['name'] for artist in similar_artists]

            print(f"Found {len(artist_names)} similar artists to {artist_name}")
            return artist_names
        
        except requests.exceptions.RequestException as e:
            print(f"Error fetching from Last.fm: {e}")
            return []
        except KeyError as e:
            print(f"Unexpected response format: {e}")
            return []
