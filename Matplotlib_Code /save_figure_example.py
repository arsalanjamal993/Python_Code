import matplotlib.pyplot as plt

x = [1, 2, 3]
y = [10, 20, 30]

plt.plot(x, y)
plt.title('Simple Line Plot')
plt.savefig('simple_plot.png', dpi=300, bbox_inches='tight')
plt.show()
