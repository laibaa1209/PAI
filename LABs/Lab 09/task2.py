import matplotlib.pyplot as plt
import numpy as np

cities = [f"City {i+1}" for i in range(10)]
population = np.random.randint(200000, 500000, 10)

plt.figure(figsize=(12, 6))
bar_colors = plt.cm.Pastel1(np.linspace(0, 1, len(cities)))
plt.barh(cities, population, color=bar_colors)
plt.title("Population Of Cities")
plt.xlabel("Population")
plt.ylabel("Cities")

plt.show()