import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr']
sales = [1000, 1500, 1200, 1800]

plt.plot(months, sales, color='blue', linestyle='--', linewidth=2, marker='o', label='2025 Sales Data')
plt.xlabel('Months')
plt.ylabel('Sales per Month')
plt.title('Monthly Sales Data')
plt.legend()
plt.grid(color='grey', linestyle=':', linewidth=1)
plt.xlim(0, 4)
plt.ylim(0, 2000)
plt.xticks([0, 1, 2, 3], ['Month 1', 'Month 2', 'Month 3', 'Month 4'])
plt.yticks([0, 500, 1000, 1500, 2000])
plt.show()
