from backend.spotify_client import SpotifyClient
def test_get_artist():

    client = SpotifyClient()

    test_artists = ["Stevie Wonder", "Lola Young", "Acid"]

    for artist in test_artists:
        current = client.search_artist(artist)
        print(current)


if __name__ == "__main__":
    test_get_artist()
