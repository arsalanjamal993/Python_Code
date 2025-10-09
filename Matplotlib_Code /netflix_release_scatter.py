import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('netflix_titles.csv')
df = df.drop_duplicates()
df = df[['type', 'title', 'director', 'cast', 'country', 'date_added', 'release_year', 'rating', 'duration', 'listed_in']]

release_counts = df['release_year'].value_counts().sort_index()
plt.figure(figsize=(10, 6))
plt.scatter(release_counts.index, release_counts.values, color='red')
plt.xlabel('Release Year')
plt.ylabel('Number of Shows')
plt.title('Release Year vs Number of Shows')
plt.tight_layout()
plt.savefig('release_year_scatter.png')
plt.show()
