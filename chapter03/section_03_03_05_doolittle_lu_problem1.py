"""
(3.3.5) Doolittle LU 분해 Python 코드
문제 1
Numerical Analysis with Python
"""

import numpy as np

def doolittle_lu_decomposition(A):
    n = len(A)
    L = np.zeros_like(A, dtype=float)
    U = np.zeros_like(A, dtype=float)

    for i in range(n):
        L[i][i] = 1  # L의 대각선은 1로 고정

        # U 행렬 계산
        for j in range(i, n):
            U[i][j] = A[i][j] - sum(L[i][k] * U[k][j] for k in range(i))

        # L 행렬 계산
        for j in range(i + 1, n):
            L[j][i] = (A[j][i] - sum(L[j][k] * U[k][i] for k in range(i))) / U[i][i]

    return L, U


# 문제 정의
A = np.array([[2, 1, -1],
              [-3, -1, 2],
              [-2, 1, 2]], dtype=float)

# Doolittle LU 분해 수행
L, U = doolittle_lu_decomposition(A)

# 결과 출력
print("L:")
print(L)
print("U:")
print(U)
