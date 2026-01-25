# section_11_02_07_1d_steady_heat_fdm.py
# (11.2) 유한차분법의 수치해석
# (11.2.7) 1차원 정상 열전달 FDM 수치해석

import numpy as np
import matplotlib.pyplot as plt

# ------------------------------------------------------------------
# 문제 정의
# u''(x) = f(x),  0 <= x <= 1
# u(0) = 1, u(1) = e
# ------------------------------------------------------------------
def function_f(x):
    return np.exp(x)

def exact_solution(x):
    return np.exp(x)

# ------------------------------------------------------------------
# FDM Solver (2차 중앙 차분)
# ------------------------------------------------------------------
def fdm_solver(n, a, b):
    h = (b - a) / (n - 1)           # 격자 간격
    x = np.linspace(a, b, n)        # 격자점

    # 계수 행렬 및 우변 벡터
    A = np.zeros((n, n))
    F = np.zeros(n)

    # 내부 격자점 (중앙 차분)
    for i in range(1, n - 1):
        A[i, i - 1] = 1.0 / h**2
        A[i, i]     = -2.0 / h**2
        A[i, i + 1] = 1.0 / h**2
        F[i] = function_f(x[i])

    # 경계 조건 (Dirichlet)
    A[0, 0] = 1.0
    F[0] = 1.0                # u(0) = 1

    A[-1, -1] = 1.0
    F[-1] = np.exp(1.0)       # u(1) = e

    # 선형 시스템 해
    U = np.linalg.solve(A, F)

    return x, U

# ------------------------------------------------------------------
# 입력 데이터
# ------------------------------------------------------------------
n = 50          # 격자 수
a, b = 0.0, 1.0 # 계산 구간

# FDM 해
x_fdm, u_fdm = fdm_solver(n, a, b)

# 정확해
x_exact = np.linspace(a, b, 1000)
u_exact = exact_solution(x_exact)

# ------------------------------------------------------------------
# 결과 시각화
# ------------------------------------------------------------------
plt.figure(figsize=(10, 6))
plt.plot(x_fdm, u_fdm, 'o--', label='FDM Solution', markersize=6)
plt.plot(x_exact, u_exact, '-', label='Exact Solution', linewidth=2)

plt.title('1차원 정상 열전달: FDM 해와 정확해 비교')
plt.xlabel('x')
plt.ylabel('u(x)')
plt.grid(True)
plt.legend()
plt.show()
