import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('netflix_titles.csv')
df = df.drop_duplicates()
df = df[['type', 'title', 'director', 'cast', 'country', 'date_added', 'release_year', 'rating', 'duration', 'listed_in']]

country_counts = df['country'].value_counts().head(10)
plt.figure(figsize=(8, 6))
plt.barh(country_counts.index, country_counts.values, color='teal')
plt.xlabel('Number of Shows')
plt.ylabel('Country')
plt.title('Top 10 Countries by Number of Shows')
plt.tight_layout()
plt.savefig('top_10_countries.png')
plt.show()
