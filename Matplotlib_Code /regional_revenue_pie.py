import matplotlib.pyplot as plt

regions = ['North', 'South', 'East', 'West']
revenue = [3000, 2000, 1500, 1000]
colors = ['gold', 'skyblue', 'lightgreen', 'coral']

plt.figure(figsize=(6, 6))
plt.pie(revenue, labels=regions, colors=colors, autopct='%.1f%%', startangle=90)
plt.title('Revenue Contribution by Region')
plt.show()
