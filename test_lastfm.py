from backend.lastfm_client import LastFmClient

def test_similar_artists():
    client = LastFmClient()

    test_artists = ["Radiohead", "Queen", "Red Axes", "SASDASFSAsadas"]

    for artist in test_artists:
        print(f"\n_____")
        print(f"Testing: {artist}")
        print(f"_____")

        similar = client.get_similar_artists(artist, limit=10)

        for i, similar_artist in enumerate(similar, 1):
            print(f"{i}. {similar_artist}")

if __name__ == "__main__":
    test_similar_artists()