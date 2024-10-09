import numpy as np

A = np.random.choice([2, 5, 9, 10], size=(4, 4))
print("\nMatrix A: \n", A)

B = np.eye(4)
print("\nMatrix B: \n", B)

odd_matrix = np.arange(1, 32, 2).reshape(4, 4)
print("\nOdd Matrix: \n", odd_matrix)

mul_arr_iden = np.dot(A, B)
print("\nA x B:\n", mul_arr_iden)

summ = np.add(odd_matrix, mul_arr_iden)
print("\nmul_arr_identity + odd_array:\n", summ)