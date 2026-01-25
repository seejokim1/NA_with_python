"""
(3.3.10) LU 분해 vs numpy.linalg.solve 성능·구조 비교
Numerical Analysis with Python
"""

import numpy as np
from scipy.linalg import lu_factor, lu_solve

# 계수 행렬과 상수 벡터 정의
A = np.array([[2, 1, -1],
              [-3, -1, 2],
              [-2, 1, 2]], dtype=float)

b = np.array([8, -11, -3], dtype=float)

print("계수 행렬 A:")
print(A)
print("\n상수 벡터 b:")
print(b)

# -------------------------------
# 1. numpy.linalg.solve 사용
# -------------------------------
x_numpy = np.linalg.solve(A, b)

print("\n[numpy.linalg.solve 결과]")
print("x =", x_numpy)
print("검증 A @ x =", A @ x_numpy)

# -------------------------------
# 2. SciPy LU 분해 + 풀이
# -------------------------------
lu_piv = lu_factor(A)
x_lu = lu_solve(lu_piv, b)

print("\n[SciPy LU 분해 결과]")
print("x =", x_lu)
print("검증 A @ x =", A @ x_lu)

# -------------------------------
# 결과 비교
# -------------------------------
print("\n해의 차이 (numpy - LU):")
print(x_numpy - x_lu)
