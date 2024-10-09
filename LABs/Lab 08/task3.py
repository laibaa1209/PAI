import numpy as np

even_arr = np.arange(2, 19, 2).reshape(3,3)
print("Even Matrix:\n", even_arr)

mul_arr = np.multiply(even_arr, 4)
print("Even Matrix multiplied by 4: \n", mul_arr)

identity_matrix = np.eye(3)

mul_even_iden = np.dot(mul_arr, identity_matrix)
print("Matrix multipled by identity matrix:\n", mul_even_iden)