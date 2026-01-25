# section_06_05_02_cubic_spline_comparison.py
# (6.5.2) Cubic Spline이 다른 보간법과 다른 이유

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange, CubicSpline

# 데이터 포인트 (점 4개)
x_points = np.array([0.0, 1.0, 2.0, 3.0])
y_points = np.array([1.0, 2.0, 0.0, 5.0])

# 보간용 x 좌표
x_new = np.linspace(0.0, 3.0, 200)

# ------------------------------------------------------------------
# 1. Newton의 분할차분 보간법
# ------------------------------------------------------------------
def divided_diff(x, y):
    n = len(y)
    coef = np.zeros((n, n))
    coef[:, 0] = y
    for j in range(1, n):
        for i in range(n - j):
            coef[i, j] = (coef[i + 1, j - 1] - coef[i, j - 1]) / (x[i + j] - x[i])
    return coef[0, :]

def newton_poly(coef, x_data, x):
    n = len(coef) - 1
    p = coef[n]
    for k in range(1, n + 1):
        p = coef[n - k] + (x - x_data[n - k]) * p
    return p

newton_coef = divided_diff(x_points, y_points)
y_newton = newton_poly(newton_coef, x_points, x_new)

# ------------------------------------------------------------------
# 2. Cubic Spline 보간법
# ------------------------------------------------------------------
cubic_spline = CubicSpline(x_points, y_points)
y_spline = cubic_spline(x_new)

# ------------------------------------------------------------------
# 3. Lagrange 보간법
# ------------------------------------------------------------------
lagrange_poly = lagrange(x_points, y_points)
y_lagrange = lagrange_poly(x_new)

# ------------------------------------------------------------------
# 4. Quadratic Spline 보간법
#    (CubicSpline을 이용한 구현)
# ------------------------------------------------------------------
quadratic_spline = CubicSpline(
    x_points,
    y_points,
    bc_type='natural',
    extrapolate=False
)
y_quadratic_spline = quadratic_spline(x_new)

# ------------------------------------------------------------------
# 결과 비교 그래프
# ------------------------------------------------------------------
plt.figure(figsize=(10, 6))

# 데이터 포인트
plt.scatter(
    x_points, y_points,
    color='red', label='Data Points', zorder=5
)

# Newton 보간
plt.plot(
    x_new, y_newton,
    label="Newton's Divided Difference",
    color='blue', linewidth=2
)

# Cubic Spline
plt.plot(
    x_new, y_spline,
    label="Cubic Spline",
    color='orange', linewidth=2
)

# Lagrange 보간
plt.plot(
    x_new, y_lagrange,
    label="Lagrange Interpolation",
    color='green', linestyle='--', linewidth=2
)

# Quadratic Spline
plt.plot(
    x_new, y_quadratic_spline,
    label="Quadratic Spline",
    color='purple', linestyle='-.', linewidth=2
)

# 그래프 설정
plt.title('Cubic Spline이 다른 보간법과 다른 이유')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
plt.axvline(0, color='black', linewidth=0.5, linestyle='--')
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend()

plt.show()
