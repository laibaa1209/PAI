import pandas as pd

df = pd.read_csv(r'C:\Users\k230006\Desktop\pai lab6\movie_metadata.csv')
result = df[(df["title_year"] == 1987) | (df['title_year'] == 1989)]

print(result['movie_title'])
