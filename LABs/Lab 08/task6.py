import numpy as np

A = np.arange(1, 16).reshape(5, 3)
B = np.arange(2, 32, 2).reshape(3, 5)

multiplication = np.dot(A, B)

print("Matrix A:", A)
print("\nMatrix B:", B)

print("\nAxB: \n", multiplication)