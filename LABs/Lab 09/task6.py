import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("StudentsPerformance.csv")

math_marks = df.loc[0:10, "math score"]
science_score = df.loc[0:10, "reading score"]
plt.scatter(math_marks, science_score, c='purple')
plt.xlabel("Math Score")
plt.ylabel("Science Score")
plt.title("Comparision: Science and Math")

plt.show()