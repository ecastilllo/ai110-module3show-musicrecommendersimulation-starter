# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name

**MoodMix 1.0**

## 2. Goal and Intended Use

MoodMix suggests up to five songs from the catalog based on a listener's preferred genre, mood, and target energy. It explains the points each recommendation earns.

**Intended use.** Classroom demonstrations and experiments with recommendation rules.

**Non-intended use.** Production music recommendations, where the catalog and evaluation would need to represent real listeners and a wider range of music.

## 3. How the Model Works

A matching mood earns 40 points, a matching genre earns 30, and a track earns up to 30 more points based on how close its energy is to the listener's target. The recommender sorts tracks by total score and uses song ID to break ties.

## 4. Data

The catalog contains 18 fictional songs, including eight additions to the starter catalog. Genres include lofi, pop, rock, folk, funk, and house. Moods include chill, happy, intense, and melancholic. The CSV also records tempo, valence, danceability, and acousticness. Scoring uses genre, mood, and energy. Each track has one mood label, and the small catalog has limited coverage of genre and mood combinations.

## 5. Strengths

The strongest results occur when a track matches both the requested mood and genre. The chill lofi profile starts with two such tracks, ordered by energy similarity. The explanations also show which preferences each partial match satisfies.

## 6. Limitations and Bias

The recommender requires an exact mood label and still returns five tracks when that mood is absent. For High-Energy Sad Pop, none of the 18 tracks had the `sad` label, so Gym Hero, an intense pop song, ranked first. Low Lantern is labeled `melancholic`, so it earns zero mood points and falls outside the top five. This can narrow discovery for listeners who describe a similar mood with different words.

## 7. Evaluation

I ran `python -m src.main --evaluate` and compared the top five titles, scores, and explanations for four profiles. The first three cover distinct tastes. High-Energy Sad Pop is an edge case because it requests a mood absent from the catalog.

### Baseline terminal output

#### High-Energy Pop

```text
=== High-Energy Pop ===
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

#### Chill Lofi

```text
=== Chill Lofi ===
Profile: lofi / chill / target energy 0.40

Top recommendations:
1. Midnight Coding - Score: 99.40
   Because: Mood match (chill, +40.00); Genre match (lofi, +30.00); Energy similarity (0.42 vs target 0.40, +29.40)
2. Library Rain - Score: 98.50
   Because: Mood match (chill, +40.00); Genre match (lofi, +30.00); Energy similarity (0.35 vs target 0.40, +28.50)
3. Spacewalk Thoughts - Score: 66.40
   Because: Mood match (chill, +40.00); Energy similarity (0.28 vs target 0.40, +26.40)
4. Focus Flow - Score: 60.00
   Because: Genre match (lofi, +30.00); Energy similarity (0.40 vs target 0.40, +30.00)
5. Coffee Shop Stories - Score: 29.10
   Because: Energy similarity (0.37 vs target 0.40, +29.10)
```

#### Intense Rock

```text
=== Intense Rock ===
Profile: rock / intense / target energy 0.90

Top recommendations:
1. Storm Runner - Score: 99.70
   Because: Mood match (intense, +40.00); Genre match (rock, +30.00); Energy similarity (0.91 vs target 0.90, +29.70)
2. Gym Hero - Score: 69.10
   Because: Mood match (intense, +40.00); Energy similarity (0.93 vs target 0.90, +29.10)
3. Glass Horizon - Score: 29.10
   Because: Energy similarity (0.87 vs target 0.90, +29.10)
4. Sunrise City - Score: 27.60
   Because: Energy similarity (0.82 vs target 0.90, +27.60)
5. Rooftop Lights - Score: 25.80
   Because: Energy similarity (0.76 vs target 0.90, +25.80)
```

#### High-Energy Sad Pop

```text
=== High-Energy Sad Pop ===
Profile: pop / sad / target energy 0.90

Top recommendations:
1. Gym Hero - Score: 59.10
   Because: Genre match (pop, +30.00); Energy similarity (0.93 vs target 0.90, +29.10)
2. Sunrise City - Score: 57.60
   Because: Genre match (pop, +30.00); Energy similarity (0.82 vs target 0.90, +27.60)
3. Storm Runner - Score: 29.70
   Because: Energy similarity (0.91 vs target 0.90, +29.70)
4. Glass Horizon - Score: 29.10
   Because: Energy similarity (0.87 vs target 0.90, +29.10)
5. Rooftop Lights - Score: 25.80
   Because: Energy similarity (0.76 vs target 0.90, +25.80)
```

### Accuracy and surprises

The chill lofi list looks coherent based on the catalog labels. Midnight Coding and Library Rain are both chill lofi with energy close to 0.40. Spacewalk Thoughts is ambient and still fits the requested chill mood. Focus Flow has the requested genre and exact energy, but ranks fourth because it is labeled `focused`.

Sunrise City ranks first for High-Energy Pop. It earns 40 points for happy, 30 for pop, and 29.40 for energy of 0.82 against a target of 0.80, totaling 99.40. Gym Hero still comes third because its pop match and nearby energy give it 56.10 points despite its intense mood. It rises to first for High-Energy Sad Pop because the requested mood is absent and Gym Hero matches pop with energy close to 0.90.

### Pairwise profile comparisons

| Profiles | What changed and why |
| --- | --- |
| High-Energy Pop and Chill Lofi | Sunrise City gives way to Midnight Coding. Each matches the requested genre and mood, and the lofi list favors tracks closer to 0.40 energy. |
| High-Energy Pop and Intense Rock | Storm Runner takes first for Intense Rock. Gym Hero moves from third to second because it matches the requested intense mood. |
| High-Energy Pop and High-Energy Sad Pop | Gym Hero moves from third to first. Rooftop Lights falls from second to fifth when it loses the happy-mood bonus. |
| Chill Lofi and Intense Rock | The top fives share zero tracks. Chill Lofi favors chill tracks around 0.40 energy. Intense Rock favors intense tracks and alternatives near 0.90. |
| Chill Lofi and High-Energy Sad Pop | The top fives share zero tracks. Chill Lofi has strong mood and genre matches. Sad Pop relies on pop and high energy because its mood is absent. |
| Intense Rock and High-Energy Sad Pop | Four tracks overlap because both target 0.90 energy. Storm Runner leads on rock and intense matches, while Gym Hero leads on pop and energy. |

### Weight-shift experiment

I temporarily halved the genre bonus from 30 to 15 and doubled the maximum energy points from 30 to 60. The mood bonus stayed at 40. With song and target energy on the 0–1 scale, the energy award remains between 0 and 60 and the score has a maximum of 115.

| Profile | First track | Baseline score | Shifted score |
| --- | --- | ---: | ---: |
| High-Energy Pop | Sunrise City | 99.40 | 113.80 |
| Chill Lofi | Midnight Coding | 99.40 | 113.80 |
| Intense Rock | Storm Runner | 99.70 | 114.40 |
| High-Energy Sad Pop | Gym Hero | 59.10 | 73.20 |

The top five stayed in the same order for all four profiles. For High-Energy Pop, the score gap between Gym Hero and Night Drive Loop shrank from 27.60 to 10.20 points. The change affected score gaps without improving the recommendations in these runs. The default CLI retains the original weights.

## 8. Ideas for Improvement

- Give partial credit to related moods, such as `sad` and `melancholic`, and check whether the new matches fit the requested mood.
- Tell listeners when a requested mood is missing and label the results as partial matches.
- Add tracks that cover more combinations of genre, mood, and energy, then rerun the same four profiles.

## 9. Personal Reflection

My biggest learning moment was seeing how much the song labels shaped the results. The chill lofi list felt believable with just genre, mood, and energy. Midnight Coding matched all three, and the ambient track Spacewalk Thoughts still made sense in the same playlist because it matched the chill mood. The sad pop test showed the other side of that rule. Gym Hero came first because the catalog had no track labeled sad, even though Gym Hero is labeled intense.

I used an AI assistant to expand the catalog, turn the scoring plan into Python, and suggest an edge case. The weight experiment was where I needed to check the output. Doubling energy and halving genre sounded like a change that would reorder the songs, but all four top-five rankings stayed the same. Next I would test partial credit for related moods, such as sad and melancholic, on a larger catalog. I would compare the same profiles before and after to see whether the resulting playlists fit the requests better.
