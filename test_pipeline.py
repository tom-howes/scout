from backend.recommender import ArtistRecommender

def test_recommendation_pipeline():
    recommender = ArtistRecommender()

    test_artist = "Radiohead"
    similar_artists = recommender.get_similar_artists_with_data(test_artist, limit=10)

    print(f"{'_'*30}\n")
    print(f"Artists similar to {test_artist}:")
    print("_"*30)

    for i, artist in enumerate(similar_artists, 1):
        print(f"\n{i}) {artist['name']}")
        print(f"    Followers: {artist['followers']:,}")
        print(f"    Popularity: {artist['popularity']}/100")
        print(f"    Genres: {", ".join(artist['genres'][:3]) if artist['genres'] else 'N/A'}")
        print(f"    Spotify: {artist['spotify_url']}")
    

if __name__ == "__main__":
    test_recommendation_pipeline()