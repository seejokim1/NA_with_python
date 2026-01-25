# =========================================================
# Section (1.11) NumPy 벡터 및 행렬
# =========================================================

import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

dot = np.dot(a, b)
print("Dot product:", dot)

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

C = A @ B
print(C)
