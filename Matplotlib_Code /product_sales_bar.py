import matplotlib.pyplot as plt

products = ['A', 'B', 'C', 'D']
sales = [1000, 1500, 800, 1200]

plt.figure(figsize=(6, 4))
plt.bar(products, sales, color='skyblue', width=0.6, label='Sales')
plt.xlabel('Product')
plt.ylabel('Sales')
plt.title('Product Sales Comparison')
plt.legend()
plt.show()
