"""
(3.3.5) Doolittle LU 분해 + 해 구하기
Numerical Analysis with Python
"""

import numpy as np

def lu_decomposition(A):
    """
    LU 분해 함수

    Parameters:
        A: 계수 행렬 (numpy array)

    Returns:
        L: 하삼각 행렬
        U: 상삼각 행렬
    """
    n = len(A)
    L = np.eye(n)
    U = np.zeros_like(A, dtype=float)

    for i in range(n):
        # U 계산
        for j in range(i, n):
            U[i, j] = A[i, j] - np.dot(L[i, :i], U[:i, j])

        # L 계산
        for j in range(i + 1, n):
            L[j, i] = (A[j, i] - np.dot(L[j, :i], U[:i, i])) / U[i, i]

    return L, U


def solve_lu(L, U, b):
    """
    LU 분해를 이용한 선형 방정식 풀이

    Parameters:
        L: 하삼각 행렬
        U: 상삼각 행렬
        b: 상수 벡터

    Returns:
        x: 해 벡터
    """
    n = len(b)

    # 전진 대입: L y = b
    y = np.zeros_like(b, dtype=float)
    for i in range(n):
        y[i] = b[i] - np.dot(L[i, :i], y[:i])

    # 후진 대입: U x = y
    x = np.zeros_like(b, dtype=float)
    for i in range(n - 1, -1, -1):
        x[i] = (y[i] - np.dot(U[i, i + 1:], x[i + 1:])) / U[i, i]

    return x


# 계수 행렬과 상수 벡터 정의
A = np.array([[2, 1, -1],
              [-3, -1, 2],
              [-2, 1, 2]], dtype=float)

b = np.array([8, -11, -3], dtype=float)

# LU 분해 및 해 계산
L, U = lu_decomposition(A)
solution = solve_lu(L, U, b)

# 결과 출력
print("하삼각 행렬 L:\n", L)
print("상삼각 행렬 U:\n", U)
print("해:", solution)
