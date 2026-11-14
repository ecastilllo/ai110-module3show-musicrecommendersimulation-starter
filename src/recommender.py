import csv
from dataclasses import dataclass
from typing import Dict, List, Tuple

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool


class Recommender:
    """Rank Song objects using the same rules as the command-line recommender."""

    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        """Return the top k Song objects for the user's preferences."""
        songs_by_id = {song.id: song for song in self.songs}
        ranked = recommend_songs(vars(user), [vars(song) for song in self.songs], k)
        return [songs_by_id[song["id"]] for song, _, _ in ranked]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        """Explain the points a song earned for this user."""
        _, reasons = score_song(vars(user), vars(song))
        return "; ".join(reasons)


def load_songs(csv_path: str) -> List[Dict]:
    """Load song dictionaries from a CSV and convert numeric fields."""
    with open(csv_path, newline="", encoding="utf-8-sig") as catalog:
        songs = list(csv.DictReader(catalog))

    for song in songs:
        song["id"] = int(song["id"])
        for field in ("energy", "tempo_bpm", "valence", "danceability", "acousticness"):
            song[field] = float(song[field])
    return songs


def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Return a song's weighted score and the reasons for its points."""
    favorite_genre = user_prefs.get("favorite_genre", user_prefs.get("genre"))
    favorite_mood = user_prefs.get("favorite_mood", user_prefs.get("mood"))
    target_energy = user_prefs["target_energy"] if "target_energy" in user_prefs else user_prefs["energy"]

    score = 0.0
    reasons = []
    if song["mood"] == favorite_mood:
        score += 40
        reasons.append(f"Mood match ({favorite_mood}, +40.00)")
    if song["genre"] == favorite_genre:
        score += 30
        reasons.append(f"Genre match ({favorite_genre}, +30.00)")

    song_energy = song["energy"]
    energy_points = round(30 * (1 - abs(song_energy - target_energy)), 12)
    score += energy_points
    reasons.append(
        f"Energy similarity ({song_energy:.2f} vs target {target_energy:.2f}, "
        f"+{energy_points:.2f})"
    )
    return score, reasons


def recommend_songs(
    user_prefs: Dict, songs: List[Dict], k: int = 5
) -> List[Tuple[Dict, float, str]]:
    """Return the top k songs with scores and explanations."""
    scored = []
    for song in songs:
        score, reasons = score_song(user_prefs, song)
        scored.append((song, score, "; ".join(reasons)))

    scored.sort(key=lambda result: (-result[1], result[0]["id"]))
    return scored[:max(0, k)]
