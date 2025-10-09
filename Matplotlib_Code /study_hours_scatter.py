import matplotlib.pyplot as plt

hours = [1, 2, 3, 4, 5, 6, 7, 8]
scores = [50, 55, 60, 65, 70, 75, 80, 85]

plt.figure(figsize=(6, 4))
plt.scatter(hours, scores, color='green', marker='o', label='Class A')
plt.xlabel('Hours Studied')
plt.ylabel('Exam Scores')
plt.title('Relationship between Study Time and Exam Scores')
plt.grid(True)
plt.legend()
plt.show()
