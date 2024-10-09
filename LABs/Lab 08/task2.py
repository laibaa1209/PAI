#dimensions = columns
#sample size = num of rows
import numpy as np

odd_arr = np.arange(1,19, 2).reshape(3, 3)
count = 1
for i in odd_arr:
    print(f"element {count}: ", i)
    count = count+1