"""
(3.4.2) Jacobi 반복법
Numerical Analysis with Python
"""

import numpy as np

def jacobi(A, b, x0, tol=1e-10, max_iterations=100):
    """
    Jacobi 반복법으로 Ax = b 풀이

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
    n = len(A)
    x = x0.copy()
    x_new = np.zeros_like(x)

    for iteration in range(max_iterations):
        for i in range(n):
            sigma = sum(A[i, j] * x[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - sigma) / A[i, i]

        # 수렴 조건 확인 (무한 노름)
        if np.linalg.norm(x_new - x, ord=np.inf) < tol:
            return x_new, iteration + 1

        x = x_new.copy()

    raise ValueError("Jacobi method did not converge within the maximum iterations")

# -------------------------
# 예제 문제
# -------------------------
A = np.array([[4, 1, -1],
              [2, 7, 1],
              [1, -3, 12]], dtype=float)

b = np.array([3, 19, 31], dtype=float)
x0 = np.zeros_like(b)

# Jacobi 반복법 실행
solution, iterations = jacobi(A, b, x0)

# 결과 출력
print("Jacobi 반복법 해:")
print(solution)
print("반복 횟수:", iterations)
