import pandas as pd
df = pd.read_csv(r'C:\Users\k230006\Downloads\Analyzing-the-IMDB-Movie-Dataset-master\movie_metadata.csv')

last_actor = df["actor_2_name"].str.split().str[-1]
df["a"] = last_actor
print(df["a"])
