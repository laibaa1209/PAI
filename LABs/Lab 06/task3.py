import pandas as pd
import numpy as np

student = {
    "first_name": ["laiba", "Amna", "Layyana", "Ali", "Alisha", "Fasih", "Owais", "Abser"],
    "ids": ["23K-0006", "23K-0066", "23K-0052", "23K-0052", "23K-0025", "23K-0018", "23K-0042","23K-0030"],
    "last_name": ["Zia", "Khali Amna", "Junaid", "stupid", "Zaidi", "Hassan Khan", "the best", "Mansoor"],
    'score': [12.5, 0, np.nan, 9, 20, 14.5, np.nan, 19]
}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

df = pd.DataFrame(data = student, index = labels)

print(df)
