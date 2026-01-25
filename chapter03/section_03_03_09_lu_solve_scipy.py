"""
(3.3.9) SciPy LU 분해를 이용한 선형 연립방정식 풀이
Numerical Analysis with Python
"""

import numpy as np
from scipy.linalg import lu_factor, lu_solve

# 계수 행렬과 상수 벡터 정의
A = np.array([[2, 1, -1],
              [-3, -1, 2],
              [-2, 1, 2]], dtype=float)

b = np.array([8, -11, -3], dtype=float)

# LU 분해 수행 (부분 피벗팅 포함)
lu_piv = lu_factor(A)

# LU 분해를 이용한 선형 방정식 풀이
x = lu_solve(lu_piv, b)

# 결과 출력
print("계수 행렬 A:")
print(A)

print("\n상수 벡터 b:")
print(b)

print("\n해 벡터 x:")
print(x)

# 검증
print("\n검증: A @ x")
print(A @ x)
