# section_08_02_02_circle_line_nonlinear_system.py
# (8.2.2) 원과 직선이 만나는 점을 찾는 연립 비선형방정식

import matplotlib.pyplot as plt
from numpy import (
    array, dot, zeros, linspace, meshgrid, set_printoptions
)
from numpy.linalg import inv

# ------------------------------------------------------------------
# 비선형 연립방정식의 Newton-Raphson 방법
# ------------------------------------------------------------------
def newton_nonlinear(f1, f2, x10, x20, n, omega):
    x1 = zeros(n)
    x2 = zeros(n)
    x1[0] = x10
    x2[0] = x20

    for k in range(n - 1):
        f = array([f1(x1[k], x2[k]), f2(x1[k], x2[k])])
        dx1, dx2 = -omega * dot(inv(j(x1[k], x2[k])), f)
        x1[k + 1] = x1[k] + dx1
        x2[k + 1] = x2[k] + dx2

    return x1, x2

# ------------------------------------------------------------------
# 야코비안 행렬 (Jacobian matrix)
# ------------------------------------------------------------------
def j(x1, x2):
    j11 = 2.0 * x1
    j12 = 2.0 * x2
    j21 = -2.0
    j22 = 1.0
    return array([[j11, j12],
                  [j21, j22]])

# ------------------------------------------------------------------
# 비선형 연립방정식 정의
# ------------------------------------------------------------------
def f1(x1, x2):
    return x1**2 + x2**2 - 1.0     # 원 방정식

def f2(x1, x2):
    return -2.0 * x1 + x2 - 1.0    # 직선 방정식

# ------------------------------------------------------------------
# 초기값 및 매개변수 설정
# ------------------------------------------------------------------
try:
    x10 = float(input("x1의 초기 추정값을 입력하세요: "))
    x20 = float(input("x2의 초기 추정값을 입력하세요: "))
except ValueError:
    print("잘못된 입력! 기본값 x1 = 0.0, x2 = 2.0을 사용합니다.")
    x10 = 0.0
    x20 = 2.0

omega = 1.0   # 과보정 계수
n = 10        # 반복 횟수

# ------------------------------------------------------------------
# Newton-Raphson 방법 적용
# ------------------------------------------------------------------
x1, x2 = newton_nonlinear(f1, f2, x10, x20, n, omega)

set_printoptions(precision=4)

print("x1 =", x1)
print("x2 =", x2)
print(f"수렴 해: x1 = {x1[-1]:.4f}, x2 = {x2[-1]:.4f}")

# ------------------------------------------------------------------
# 해의 기하학적 의미 시각화
# ------------------------------------------------------------------
x_vals = linspace(-1.5, 1.5, 300)
y_vals = linspace(-1.5, 1.5, 300)
X, Y = meshgrid(x_vals, y_vals)

F1 = f1(X, Y)   # 원
F2 = f2(X, Y)   # 직선

plt.figure(figsize=(6, 6))

# 암묵 곡선
plt.contour(X, Y, F1, levels=[0], colors='blue', linewidths=2)
plt.contour(X, Y, F2, levels=[0], colors='green', linewidths=2)

# 수렴 경로
plt.plot(
    x1, x2,
    marker='o', linestyle='-',
    color='red', label='수렴 경로'
)

# 최종 해
plt.scatter(
    x1[-1], x2[-1],
    color='orange', s=100,
    label=f"해 ({x1[-1]:.4f}, {x2[-1]:.4f})"
)

plt.title("Newton-Raphson 방법에 의한 연립 비선형방정식 해", fontsize=14)
plt.xlabel("x1")
plt.ylabel("x2")
plt.axhline(0, color='black', linestyle='--', linewidth=0.5)
plt.axvline(0, color='black', linestyle='--', linewidth=0.5)
plt.grid(alpha=0.5)
plt.legend()
plt.show()
