import pandas as pd
df = pd.read_csv(r'C:\Users\k230006\Downloads\Analyzing-the-IMDB-Movie-Dataset-master\movie_metadata.csv')

result = df[(df["gross"] > 2000000 ) & (df["budget"] < 1000000)] 
print(result)