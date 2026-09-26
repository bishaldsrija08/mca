import matplotlib.pyplot as plt
import numpy as np

# Point Plot
x = [1, 2, 3, 4, 5]
y = [2, 5, 3, 7, 6]

plt.scatter(x, y)
plt.title("Point Plot")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

# Line Plot
plt.plot(x, y, marker="o")
plt.title("Line Plot")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

# Bar Graph
subjects = ["Python", "DBMS", "OS", "Math"]
marks = [80, 75, 85, 70]

plt.bar(subjects, marks)
plt.title("Bar Graph")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.show()

# Histogram
data = [12, 15, 18, 20, 22, 22, 25, 27, 28, 30,
        31, 32, 35, 35, 38, 40, 42, 45, 45, 48]

plt.hist(data, bins=5)
plt.title("Histogram")
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.show()

# Boxplot
marks = [55, 60, 65, 70, 72, 75, 78, 80, 85, 90]

plt.boxplot(marks)
plt.title("Boxplot")
plt.ylabel("Marks")
plt.show()

# 3D Plot
from mpl_toolkits.mplot3d import Axes3D

x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 8, 10])
z = np.array([5, 10, 15, 20, 25])

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

ax.scatter(x, y, z)
ax.set_title("3D Plot")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

plt.show()