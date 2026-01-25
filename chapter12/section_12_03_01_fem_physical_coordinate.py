# section_12_03_01_fem_physical_coordinate.py
# (12.3) 실제좌표계에서의 유한요소법(FEM)
# (12.3.1) 실제좌표계에서의 유한요소법(FEM) 예제

import numpy as np
import matplotlib.pyplot as plt

# ------------------------------------------------------------------
# 미분방정식 정의
# -u''(x) = exp(x),   0 <= x <= 1
# u(0) = 1,  u(1) = e
# ------------------------------------------------------------------
class ode:
    @staticmethod
    def function_f(x):
        return -np.exp(x)

    @staticmethod
    def function_g(x):
        if x == 0:
            return 1.0
        elif x == 1:
            return np.exp(1.0)

# ------------------------------------------------------------------
# FEM 강성 행렬 (1D, 선형 요소)
# ------------------------------------------------------------------
def stiffness_matrix(n, h, k):
    K = np.zeros((n, n))
    for i in range(n):
        if i > 0:
            K[i, i - 1] = -k / h
        K[i, i] = 2 * k / h
        if i < n - 1:
            K[i, i + 1] = -k / h
    return K

# ------------------------------------------------------------------
# FEM 외력 벡터
# ------------------------------------------------------------------
def force_vector(n, h):
    F = np.zeros(n)
    for i in range(n):
        x_i = i * h
        F[i] = ode.function_f(x_i) * h
    return F

# ------------------------------------------------------------------
# 이론해
# ------------------------------------------------------------------
def analytical_solution(x):
    return np.exp(x)

# ------------------------------------------------------------------
# 입력 데이터
# ------------------------------------------------------------------
n = 5                  # 노드 수
h = 1.0 / (n - 1)      # 요소 길이
k = 1.0                # 계수

# ------------------------------------------------------------------
# FEM 계산
# ------------------------------------------------------------------
K = stiffness_matrix(n, h, k)
F = force_vector(n, h)

# Dirichlet 경계 조건 적용
K[0, :] = 0.0
K[0, 0] = 1.0
F[0] = ode.function_g(0)

K[-1, :] = 0.0
K[-1, -1] = 1.0
F[-1] = ode.function_g(1)

# 선형 시스템 풀이
U_fem = np.linalg.solve(K, F)

# ------------------------------------------------------------------
# 좌표 생성
# ------------------------------------------------------------------
x_fem = np.linspace(0.0, 1.0, n)
x_exact = np.linspace(0.0, 1.0, 1000)
U_exact = analytical_solution(x_exact)

# ------------------------------------------------------------------
# 결과 시각화
# ------------------------------------------------------------------
plt.figure(figsize=(10, 6))
plt.plot(x_fem, U_fem, 'o--', label='FEM Solution', markersize=8)
plt.plot(x_exact, U_exact, '-', label='Analytical Solution', linewidth=2)

plt.title('실제좌표계 FEM 해와 이론해 비교')
plt.xlabel('x')
plt.ylabel('u(x)')
plt.grid(True)
plt.legend()
plt.show()
