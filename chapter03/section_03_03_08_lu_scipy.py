"""
(3.3.8) SciPy에서의 LU 분해
Numerical Analysis with Python
"""

import numpy as np
from scipy.linalg import lu

# 계수 행렬 정의
A = np.array([[2, 1, -1],
              [-3, -1, 2],
              [-2, 1, 2]], dtype=float)

# LU 분해 수행
P, L, U = lu(A)

# 결과 출력
print("계수 행렬 A:")
print(A)

print("\n행 교환 행렬 P:")
print(P)

print("\n하삼각 행렬 L:")
print(L)

print("\n상삼각 행렬 U:")
print(U)

# 검증: PA = LU
print("\n검증: P @ A")
print(P @ A)

print("\n검증: L @ U")
print(L @ U)
