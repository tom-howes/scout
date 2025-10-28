from backend.lastfm_client import LastFmClient

def test_similar_artists():
    client = LastFmClient()

    test_artists = ["Radiohead", "Queen", "Red Axes", "SASDASFSAsadas"]

    for artist in test_artists:
        print(f"\n{'_'*30}")
        print(f"Testing: {artist}")
        print("_"*30)

        similar = client.get_similar_artists(artist, limit=10)

        for i, similar_artist in enumerate(similar, 1):
            print(f"{i}. {similar_artist}")

if __name__ == "__main__":
    test_similar_artists()