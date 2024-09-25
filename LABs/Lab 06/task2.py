import pandas as pd

df = pd.read_csv(r'C:\Users\k230006\Downloads\Analyzing-the-IMDB-Movie-Dataset-master\movie_metadata.csv')
df = df.dropna()
sorted_df = df.sort_values(by='title_year', ascending=False)

sorted_df.to_csv(r'C:\Users\k230006\Downloads\sorted_movies_by_year.csv', index=False)

print(sorted_df)

