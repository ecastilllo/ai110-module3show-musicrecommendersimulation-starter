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

This simulation will use content-based filtering. A song earns 40 points for matching the preferred mood, 30 for matching the preferred genre, and up to 30 for energy similarity. On a 0–1 scale, the energy points are `30 × (1 − abs(song_energy − target_energy))`. The recommender will add those points for each song and sort the catalog from highest to lowest total score.

- `Song` uses `id`, `title`, and `artist` to identify and display tracks. It uses `genre`, `mood`, and `energy` for scoring.
- `UserProfile` stores a preferred genre, a preferred mood, and a target energy on a 0–1 scale.

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

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

Paste a sample of your recommender's output here as a text block so a reader can see what it produces:

```
# e.g.:
# User profile: genre=indie, mood=chill, energy=low
# Recommendations:
#   1. ...
#   2. ...
#   3. ...
```

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

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



