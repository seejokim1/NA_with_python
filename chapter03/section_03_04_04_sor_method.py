"""
(3.4.4) SOR 반복법 (Successive Over-Relaxation)
Numerical Analysis with Python
"""

import numpy as np

def sor_method(A, b, omega, x0=None, tol=1e-10, max_iter=1000):
    """
    SOR(Successive Over-Relaxation) 반복법으로 Ax = b 풀이

    Parameters:
        A: 계수 행렬 (numpy array)
        b: 상수 벡터 (numpy array)
        omega: 완화 계수 (ω), 0 < ω < 2
        x0: 초기 추정값 (None이면 0 벡터)
        tol: 수렴 허용 오차 (무한 노름)
        max_iter: 최대 반복 횟수

    Returns:
        x: 해 벡터
        iterations: 반복 횟수
    """
    n = len(b)
    x = np.zeros(n) if x0 is None else x0.copy()

    for iteration in range(max_iter):
        x_old = x.copy()

        for i in range(n):
            sigma = sum(A[i, j] * x[j] for j in range(n) if j != i)
            x[i] = (1 - omega) * x_old[i] + omega * (b[i] - sigma) / A[i, i]

        # 수렴 조건
        if np.linalg.norm(x - x_old, ord=np.inf) < tol:
            return x, iteration + 1

    raise ValueError("SOR method did not converge")

# -------------------------
# 예제 문제
# -------------------------
A = np.array([[4, 1, 2],
              [1, 3, -1],
              [2, -1, 3]], dtype=float)

b = np.array([7, 4, 5], dtype=float)

# Gauss–Seidel (ω = 1)
solution_gs, iter_gs = sor_method(A, b, omega=1.0)

# SOR (ω = 1.25)
solution_sor, iter_sor = sor_method(A, b, omega=1.25)

# 결과 출력
print("Gauss–Seidel (ω = 1)")
print("해:", solution_gs)
print("반복 횟수:", iter_gs)
print()

print("SOR (ω = 1.25)")
print("해:", solution_sor)
print("반복 횟수:", iter_sor)
