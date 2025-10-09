import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('netflix_titles.csv')
df = df.drop_duplicates()
df = df[['type', 'title', 'director', 'cast', 'country', 'date_added', 'release_year', 'rating', 'duration', 'listed_in']]

movie_data = df[df['type'] == 'Movie']
durations = movie_data['duration'].str.replace(' min', '').astype(int)

plt.figure(figsize=(8, 6))
plt.hist(durations, bins=30, color='purple', edgecolor='black')
plt.xlabel('Duration in Minutes')
plt.ylabel('Number of Movies')
plt.title('Distribution of Movie Duration')
plt.tight_layout()
plt.savefig('movie_duration_histogram.png')
plt.show()
