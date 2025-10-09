import matplotlib.pyplot as plt

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
sales = [10, 15, 7, 20, 12]

plt.plot(days, sales)
plt.title('Bakery Sales This Week')
plt.xlabel('Day of the Week')
plt.ylabel('Number of Cakes Sold')
plt.show()
