import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
x = np.random.randint(1, 50, 10)
y1 = np.random.randint(1, 50, 10)
y2 = np.random.randint(1, 50, 10)

x.sort()
y1 = y1[np.argsort(x)] 
y2 = y2[np.argsort(x)] 

plt.plot(x, y1, color="pink", marker='o', label='Metric 1')
plt.plot(x, y2, color="grey", marker='o',  label='Metric 2')

plt.title("Two Lines On One Graphs")
plt.xlabel("Amazing x Axis")
plt.ylabel("Incredible y Axis")
plt.legend(loc='lower right')

plt.show()

