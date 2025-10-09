import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y_line = [10, 20, 15, 25]
y_bar = [12, 18, 22, 16]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

ax1.plot(x, y_line, color='blue')
ax1.set_title('Line Plot')

ax2.bar(x, y_bar, color='orange')
ax2.set_title('Bar Plot')

plt.tight_layout()
plt.show()
