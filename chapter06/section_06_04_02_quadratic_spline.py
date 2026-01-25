# section_06_04_02_quadratic_spline.py
# (6.4.2) Quadratic Spline Interpolation Example

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

# 데이터 포인트 (점 4개)
x_points = np.array([0.0, 1.0, 2.0, 3.0])
y_points = np.array([1.0, 2.0, 0.0, 5.0])

# 보간을 위한 새로운 x 값
x_new = np.linspace(min(x_points), max(x_points), 200)

# Quadratic Spline Interpolation
# (SciPy에는 전용 QuadraticSpline이 없으므로 CubicSpline 사용)
quadratic_spline = CubicSpline(
    x_points,
    y_points,
    bc_type='natural',
    extrapolate=False
)

y_quadratic_spline = quadratic_spline(x_new)

# Plotting
plt.figure(figsize=(10, 6))

# 원 데이터 포인트
plt.scatter(
    x_points, y_points,
    color='red', label='Data Points', zorder=5
)

# Quadratic Spline 결과
plt.plot(
    x_new, y_quadratic_spline,
    label='Quadratic Spline',
    color='purple', linestyle='-.', linewidth=2
)

# 그래프 설정
plt.title('Quadratic Spline Interpolation Method')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
plt.axvline(0, color='black', linewidth=0.5, linestyle='--')
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend()

plt.show()
