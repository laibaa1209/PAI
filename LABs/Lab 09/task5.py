import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv("StudentsPerformance.csv")

grouped_data = df.groupby(["gender"]).size() #size function tells num of occurrence for each gender
color = plt.cm.Pastel2(np.linspace(0, 1, len(grouped_data)))
plt.pie(grouped_data, labels=grouped_data.index, autopct='%1.1f%%', startangle=140, colors=color)
plt.title("Gender Distribution")
plt.show()


