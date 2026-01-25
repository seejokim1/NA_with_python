import numpy as np
import matplotlib.pyplot as plt

# 데이터 포인트 (점 4개)
x_points = np.array([0, 1, 2, 3])
y_points = np.array([1, 2, 0, 5])

# Newton의 차분(divided difference) 계수 계산
def divided_diff(x, y):
    n = len(y)
    coef = np.zeros((n, n))
    coef[:, 0] = y
    for j in range(1, n):
        for i in range(n - j):
            coef[i, j] = (coef[i + 1, j - 1] - coef[i, j - 1]) / (x[i + j] - x[i])
    return coef[0, :]

# Newton 다항식 계산
def newton_poly(coef, x_data, x):
    n = len(coef) - 1
    p = coef[n]
    for k in range(1, n + 1):
        p = coef[n - k] + (x - x_data[n - k]) * p
    return p

# 계수 계산
newton_coef = divided_diff(x_points, y_points)

# 보간 곡선 계산
x_new = np.linspace(0, 3, 100)
y_newton = newton_poly(newton_coef, x_points, x_new)

# 결과 시각화
plt.figure(figsize=(10, 6))
plt.scatter(x_points, y_points, color='red', label='Data Points', zorder=5)
plt.plot(x_new, y_newton, label='Newton Divided Difference', color='blue', linewidth=2)

plt.title('Newton Divided Difference Interpolation')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()
plt.show()
