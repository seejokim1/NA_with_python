# section_08_01_01_nonlinear_system_newton_raphson.py
# (8.1.1) 비선형 연립방정식의 뉴톤-랩슨법(Newton-Raphson Method)

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# ------------------------------------------------------------------
# 비선형 연립방정식 정의
# ------------------------------------------------------------------
# 첫 번째 함수: 원 (circle)
# f(x, y) = x^2 + y^2 - 4
def myCirc(x, y):
    return x**2 + y**2 - 4

# 두 번째 함수: 직선 (hyperbolic로 명명된 함수)
# g(x, y) = y - 2x - 1
def myHyp(x, y):
    return y - 2*x - 1

# ------------------------------------------------------------------
# 계산 영역 설정
# ------------------------------------------------------------------
x = np.linspace(-3, 3, 200)
y = np.linspace(-3, 3, 200)
X, Y = np.meshgrid(x, y)

Z1 = myCirc(X, Y)
Z2 = myHyp(X, Y)

# ------------------------------------------------------------------
# 그래프 시각화
# ------------------------------------------------------------------
fig = plt.figure(figsize=(12, 6))

# 3D 곡면 플롯
ax1 = fig.add_subplot(121, projection='3d')
ax1.plot_surface(
    X, Y, Z1,
    cmap='viridis', alpha=0.7, edgecolor='none'
)
ax1.plot_surface(
    X, Y, Z2,
    cmap='plasma', alpha=0.7, edgecolor='none'
)
ax1.set_title("3D Plot of Nonlinear Surfaces")
ax1.set_xlabel("X")
ax1.set_ylabel("Y")
ax1.set_zlabel("Z")

# 2D 암묵적 함수 플롯 (해의 위치 시각화)
ax2 = fig.add_subplot(122)
ax2.contour(
    X, Y, Z1,
    levels=[0], colors='blue',
    linewidths=2, linestyles='dashed'
)
ax2.contour(
    X, Y, Z2,
    levels=[0], colors='red',
    linewidths=2, linestyles='solid'
)

ax2.set_title("2D Implicit Plot (Solution = Intersection)")
ax2.set_xlabel("X")
ax2.set_ylabel("Y")
ax2.grid(True)

plt.tight_layout()
plt.show()
