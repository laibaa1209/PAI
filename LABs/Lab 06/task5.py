import pandas as pd

df = pd.read_csv("movie_metadata.csv")
print("The dimensons or shape of Movie Data set is(rows, columns): ", df.shape)

print("The extracted columns are: \n", df.columns)