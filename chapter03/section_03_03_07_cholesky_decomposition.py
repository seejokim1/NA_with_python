"""
(3.3.7) Cholesky LU 분해 Python 코드
Numerical Analysis with Python
"""

import numpy as np


def cholesky_decomposition(A):
    """
    Cholesky 분해 함수
    (A = L L^T)

    Parameters:
        A : 대칭 양의 정부호 행렬 (numpy array)

    Returns:
        L : 하삼각 행렬
    """

    n = len(A)
    L = np.zeros_like(A, dtype=float)

    for i in range(n):
        for j in range(i + 1):

            # 대각 원소 계산
            if i == j:
                L[i][j] = np.sqrt(
                    A[i][i] - sum(L[i][k] ** 2 for k in range(j))
                )

            # 비대각 원소 계산
            else:
                L[i][j] = (
                    A[i][j]
                    - sum(L[i][k] * L[j][k] for k in range(j))
                ) / L[j][j]

    return L


# ==========================================
# 문제 정의 (대칭 양의 정부호 행렬)
# ==========================================
A = np.array([[4, 12, -16],
              [12, 37, -43],
              [-16, -43, 98]], dtype=float)

# Cholesky 분해 수행
L = cholesky_decomposition(A)

# 결과 출력
print("L:")
print(L)

print("\nL^T:")
print(L.T)

print("\nA (재구성 확인):")
print(np.dot(L, L.T))
