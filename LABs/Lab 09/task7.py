import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("epa-sea-level.csv")
filtered_df = df[df['Year'] > 1923]

plt.scatter(filtered_df['Year'], filtered_df['CSIRO Adjusted Sea Level'], color='teal', label="Sea Level", edgecolor='black')

plt.xlabel("Year")
plt.ylabel("Sea Level (inches)")
plt.title("Sea Level Rise in the Past 100 Years")
plt.legend()

plt.show()
