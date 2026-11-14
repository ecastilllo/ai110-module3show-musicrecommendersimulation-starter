"""Run the music recommender from the command line."""

import argparse
from pathlib import Path

from .recommender import load_songs, recommend_songs


PROFILES = {
    "High-Energy Pop": {
        "favorite_genre": "pop",
        "favorite_mood": "happy",
        "target_energy": 0.80,
    },
    "Chill Lofi": {
        "favorite_genre": "lofi",
        "favorite_mood": "chill",
        "target_energy": 0.40,
    },
    "Intense Rock": {
        "favorite_genre": "rock",
        "favorite_mood": "intense",
        "target_energy": 0.90,
    },
    "High-Energy Sad Pop": {
        "favorite_genre": "pop",
        "favorite_mood": "sad",
        "target_energy": 0.90,
    },
}


def print_recommendations(user_prefs: dict, songs: list) -> None:
    """Print the profile and its five highest-scoring tracks."""
    recommendations = recommend_songs(user_prefs, songs, k=5)

    print(
        f"Profile: {user_prefs['favorite_genre']} / {user_prefs['favorite_mood']} / "
        f"target energy {user_prefs['target_energy']:.2f}"
    )
    print("\nTop recommendations:")
    for rank, (song, score, explanation) in enumerate(recommendations, start=1):
        print(f"{rank}. {song['title']} - Score: {score:.2f}")
        print(f"   Because: {explanation}")


def main(evaluate: bool = False) -> None:
    catalog_path = Path(__file__).resolve().parents[1] / "data" / "songs.csv"
    songs = load_songs(catalog_path)
    print(f"Loaded songs: {len(songs)}")

    if evaluate:
        for name, user_prefs in PROFILES.items():
            print(f"\n=== {name} ===")
            print_recommendations(user_prefs, songs)
    else:
        print_recommendations(PROFILES["High-Energy Pop"], songs)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--evaluate", action="store_true", help="Run all four evaluation profiles."
    )
    main(evaluate=parser.parse_args().evaluate)
