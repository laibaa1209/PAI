import pandas as pd

data = {
    "first_name": ["laiba", "Amna", "Layyana", "Ali", "Alisha"],
    "last_name": ["Zia", "Khali Amna", "Junaid", "stupid", "Zaidi"],
    "score": [12.5, 9, 16.5, 20, 14.5]
}

df = pd.DataFrame(data)
new_index = pd.Index(range(1, 1 + len(df)))
df.index = new_index

print(df)
