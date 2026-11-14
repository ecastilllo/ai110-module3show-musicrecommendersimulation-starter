"""Run the music recommender from the command line."""

from pathlib import Path

from .recommender import load_songs, recommend_songs


def main() -> None:
    catalog_path = Path(__file__).resolve().parents[1] / "data" / "songs.csv"
    songs = load_songs(catalog_path)
    print(f"Loaded songs: {len(songs)}")

    user_prefs = {
        "favorite_genre": "pop",
        "favorite_mood": "happy",
        "target_energy": 0.80,
    }
    recommendations = recommend_songs(user_prefs, songs, k=5)

    print(
        f"Profile: {user_prefs['favorite_genre']} / {user_prefs['favorite_mood']} / "
        f"target energy {user_prefs['target_energy']:.2f}"
    )
    print("\nTop recommendations:")
    for rank, (song, score, explanation) in enumerate(recommendations, start=1):
        print(f"{rank}. {song['title']} - Score: {score:.2f}")
        print(f"   Because: {explanation}")


if __name__ == "__main__":
    main()
