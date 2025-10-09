import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('netflix_titles.csv')
df = df.drop_duplicates()
df = df[['type', 'title', 'director', 'cast', 'country', 'date_added', 'release_year', 'rating', 'duration', 'listed_in']]

trends = df.groupby('release_year')['type'].value_counts().unstack().fillna(0)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
ax1.plot(trends.index, trends['Movie'], color='blue')
ax1.set_title('Movies Released Per Year')
ax1.set_xlabel('Year')
ax1.set_ylabel('Number of Movies')

ax2.plot(trends.index, trends['TV Show'], color='orange')
ax2.set_title('TV Shows Released Per Year')
ax2.set_xlabel('Year')
ax2.set_ylabel('Number of TV Shows')

plt.suptitle('Comparison of Movies & TV Shows Released Over Years')
plt.tight_layout()
plt.savefig('movies_tv_shows_comparison.png')
plt.show()
