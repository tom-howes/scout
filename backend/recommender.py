from backend.lastfm_client import LastFmClient
from backend.spotify_client import SpotifyClient
import time

class ArtistRecommender:

    def __init__(self):
        self.lastfm = LastFmClient()
        self.spotify = SpotifyClient()

    def get_similar_artists_with_data(self, artist_name, limit=20):
        """
        Get similar artists through Last.fm with their Spotify data
        Returns: List of artist data Dicts
        """

        print(f"\nFinding Artists similar to {artist_name}...")
        similar_names = self.lastfm.get_similar_artists(artist_name, limit=limit)

        if not similar_names:
            print("No similar artists found")
            return []
        
        print(f"Fetching spotify data for {len(similar_names)} artists...")
        artists_data = []
        for i, name in enumerate(similar_names, 1):
            print(f" [{i}/{len(similar_names)}] {name}...", end=" ")
            spotify_data = self.spotify.search_artist(name)
            if spotify_data:
                artists_data.append(spotify_data)
                print(f" {spotify_data['followers']:,} followers") # :, makes larger numbers readable e.g. 2500000 = 2,500,000
            else:
                print("Not found")
            
            # Don't overload API
            time.sleep(0.3)
            
        
        print(f"\n Successfully fetched data for {len(artists_data)} artists")
        return artists_data
