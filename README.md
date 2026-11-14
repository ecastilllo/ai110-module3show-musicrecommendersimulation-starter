# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

Streaming platforms use listening behavior and track attributes to predict what people may enjoy. Collaborative filtering looks for patterns across listeners, such as which tracks are often played by people with similar listening habits. Content-based filtering compares track attributes with a listener's preferences. For example, Spotify describes using listening history, relationships between tracks, and audio attributes to personalize playlists at scale. [Spotify Engineering](https://engineering.atspotify.com/2023/04/humans-machines-a-look-behind-spotifys-algotorial-playlists)

The simulation uses content-based filtering to match songs to a listener's preferences.

### Catalog and taste profile

The catalog in `data/songs.csv` contains 18 tracks, including eight fictional tracks that add new genres and moods. Each `Song` uses `id`, `title`, and `artist` for identification and display. Scoring uses `genre`, `mood`, and `energy`. The CSV also records tempo, valence, danceability, and acousticness for future experiments.

The example `UserProfile` is a dictionary for a listener who wants chill lofi near 0.40 energy:

```python
{
    "favorite_genre": "lofi",
    "favorite_mood": "chill",
    "target_energy": 0.40,
}
```

This profile distinguishes chill lofi from intense rock because the tracks differ in all three scoring features. With these settings, Midnight Coding scores 99.4 and Storm Runner scores 14.7. For a profile targeting intense rock at 0.90 energy, Storm Runner leads the catalog with 99.7. A single genre, mood, and energy target describes one listening context. A profile with multiple preferences could represent someone who likes both styles.

### Algorithm recipe

1. Load the song records and read the listener's profile and the requested number of recommendations, `k`.
2. For each song, award 40 points for an exact mood match and 30 for an exact genre match. Each mismatch earns zero points for that feature.
3. Add up to 30 energy points using `30 × (1 − abs(song_energy − target_energy))`. Song energy and the target both use a 0–1 scale. Equally close values earn the same points.
4. Sort by total score from highest to lowest. Break exact score ties by ascending song ID and return the first `k` songs.

**Weight choice.** The genre-first recipe from the assignment (2 for genre, 1 for mood, and up to 1 for energy) ranks Focus Flow (3.00) above Spacewalk Thoughts (1.88) for the chill lofi profile. The chosen mood-first recipe gives Spacewalk Thoughts 66.4 and Focus Flow 60.0. For this example, the requested chill mood matters most.

### Data flow

1. **Input** — Read the taste profile, the song catalog, and `k`.
2. **Processing** — Compare each song with the profile and record its total score.
3. **Output** — Sort the scored tracks and return the top `k`. For the example profile and `k = 3`, the expected order is 1. Midnight Coding (99.4), 2. Library Rain (98.5), 3. Spacewalk Thoughts (66.4).

**Potential bias.** Exact labels can split tracks that feel similar, such as `chill` and `relaxed`. Giving mood the most weight can favor tracks labeled `chill` even when tracks with other labels match the listener's genre and energy more closely. Genres with more tracks in this small catalog also have more opportunities to appear in the top results.

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows
   ```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

Run `python -m src.main` from the project directory to see the default pop/happy profile's recommendations.

```text
Loaded songs: 18
Profile: pop / happy / target energy 0.80

Top recommendations:
1. Sunrise City - Score: 99.40
   Because: Mood match (happy, +40.00); Genre match (pop, +30.00); Energy similarity (0.82 vs target 0.80, +29.40)
2. Rooftop Lights - Score: 68.80
   Because: Mood match (happy, +40.00); Energy similarity (0.76 vs target 0.80, +28.80)
3. Gym Hero - Score: 56.10
   Because: Genre match (pop, +30.00); Energy similarity (0.93 vs target 0.80, +26.10)
4. Night Drive Loop - Score: 28.50
   Because: Energy similarity (0.75 vs target 0.80, +28.50)
5. City in Motion - Score: 27.90
   Because: Energy similarity (0.73 vs target 0.80, +27.90)
```

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this



