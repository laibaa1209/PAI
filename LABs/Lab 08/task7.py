import numpy as np

arr = np.random.rand(1000)
print("Random Array: ", arr)

avg = np.mean(arr)
variance = np.var(arr)
std_deviation = np.std(arr)

f = open("numeric analysis.txt", "w")
f.write(f"Average: {avg}\n")
f.write(f"Variance: {variance}\n")
f.write(f"Standard Deviation: {std_deviation}\n")