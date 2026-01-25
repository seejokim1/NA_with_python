"""
(3.4.3) Gauss–Seidel 반복법
Numerical Analysis with Python
"""

import numpy as np

def gauss_seidel(A, b, x0, tol=1e-6, max_iterations=100):
    """
    Gauss–Seidel 반복법으로 Ax = b 풀이

    Parameters:
        A: 계수 행렬 (numpy array)
        b: 상수 벡터 (numpy array)
        x0: 초기 추정값
        tol: 수렴 허용 오차 (무한 노름)
        max_iterations: 최대 반복 횟수

    Returns:
        x: 해 벡터
        iterations: 반복 횟수
    """
    n = len(b)
    x = x0.copy()

    for iteration in range(max_iterations):
        x_old = x.copy()

        for i in range(n):
            sum1 = sum(A[i, j] * x[j] for j in range(i))          # j < i
            sum2 = sum(A[i, j] * x_old[j] for j in range(i+1, n)) # j > i
            x[i] = (b[i] - sum1 - sum2) / A[i, i]

        # 수렴 조건 (무한 노름)
        if np.linalg.norm(x - x_old, ord=np.inf) < tol:
            return x, iteration + 1

    raise ValueError("Gauss–Seidel method did not converge")

# -------------------------
# 예제 문제
# -------------------------
A = np.array([[4, 1, -1],
              [2, 7, 1],
              [1, -3, 12]], dtype=float)

b = np.array([3, 19, 31], dtype=float)
x0 = np.zeros_like(b)

# Gauss–Seidel 반복법 실행
solution, iterations = gauss_seidel(A, b, x0)

# 결과 출력
print("Gauss–Seidel 반복법 해:")
print(solution)
print("반복 횟수:", iterations)
