# section_06_04_04_cubic_spline.py
# (6.4.4) Cubic Spline Interpolation Example

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

# 데이터 포인트 (점 4개)
x_points = np.array([0.0, 1.0, 2.0, 3.0])
y_points = np.array([1.0, 2.0, 0.0, 5.0])

# 새 x 좌표 생성 (보간용)
x_new = np.linspace(
    min(x_points),
    max(x_points),
    200
)

# Cubic Spline Interpolation
cubic_spline = CubicSpline(x_points, y_points)
y_spline = cubic_spline(x_new)

# 결과 그래프 시각화
plt.figure(figsize=(10, 6))

# 데이터 포인트
plt.scatter(
    x_points, y_points,
    color='red', label='Data Points', zorder=5
)

# Cubic Spline 곡선
plt.plot(
    x_new, y_spline,
    label='Cubic Spline',
    color='orange', linewidth=2
)

# 그래프 설정
plt.title('Cubic Spline Interpolation Method')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
plt.axvline(0, color='black', linewidth=0.5, linestyle='--')
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend()

plt.show()
