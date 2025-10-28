import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os
from dotenv import load_dotenv

load_dotenv()

class SpotifyClient:
    def __init__(self):
        self.sp = spotipy.Spotify(
            auth_manager=SpotifyClientCredentials(
                client_id=os.getenv("SPOTIFY_CLIENT_ID"),
                client_secret=os.getenv("SPOTIFY_CLIENT_SECRET")
            )
        )
    
    def search_artist(self, artist_name):
        """
        Search for a Dict with artist data (None if not found)
        TODO: Handle cases where multiple artists have same name (currently returns most popular)
        """

        try:
            results = self.sp.search(q=f"artist:{artist_name}", type='artist', limit=1)

            if not results['artists']['items']:
                print(f"Artist not found on spotify: {artist_name}")
                return None

            artist = results['artists']['items'][0]

            artist_data = {
                'spotify_id': artist['id'],
                'name' : artist['name'],
                'followers' : artist['followers']['total'],
                'popularity' : artist['popularity'],
                'genres' : artist['genres'],
                'image_url' : artist['images'][0]['url'] if artist['images'] else None,
                'spotify_url' : artist['external_urls']['spotify']
            }

            return artist_data
        
        except Exception as e:
            print(f"Error searching Spotify for {artist_name}: {e}")
            return None
    
    # def get_artist_by_id(self, spotify_id):
        
    #     try:
    #         artist = self.sp.artist(spotify_id)
    #         return self.search_artist(artist['name'])
    #     except Exception as e:
    #         print(f"Error fetching artist {spotify_id}: {e}")
    #         return None