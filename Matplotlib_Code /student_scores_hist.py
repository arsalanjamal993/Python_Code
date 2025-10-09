import matplotlib.pyplot as plt

scores = [45, 67, 89, 54, 76, 82, 91, 63, 78, 85, 92, 49, 71, 88, 60]

plt.figure(figsize=(6, 4))
plt.hist(scores, bins=5, color='purple', edgecolor='black')
plt.xlabel('Score Range')
plt.ylabel('Number of Students')
plt.title('Score Distribution of Students')
plt.show()
