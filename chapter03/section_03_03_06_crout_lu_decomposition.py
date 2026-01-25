"""
(3.3.6) Crout LU 분해법
Numerical Analysis with Python
"""

import numpy as np

def crout_lu_decomposition(A):
    """
    Crout LU 분해 함수
    (L은 하삼각, U는 대각 원소가 1인 상삼각 행렬)

    Parameters:
        A: 계수 행렬 (numpy array)

    Returns:
        L: 하삼각 행렬
        U: 상삼각 행렬 (대각선 = 1)
    """
    n = len(A)
    L = np.zeros_like(A, dtype=float)
    U = np.eye(n, dtype=float)

    for j in range(n):
        # L 계산
        for i in range(j, n):
            L[i][j] = A[i][j] - sum(L[i][k] * U[k][j] for k in range(j))

        # U 계산
        for i in range(j + 1, n):
            U[j][i] = (A[j][i] - sum(L[j][k] * U[k][i] for k in range(j))) / L[j][j]

    return L, U


# 문제 정의
A = np.array([[4, 12, -16],
              [12, 37, -43],
              [-16, -43, 98]], dtype=float)

# Crout LU 분해 수행
L, U = crout_lu_decomposition(A)

# 결과 출력
print("L:")
print(L)
print("U:")
print(U)
