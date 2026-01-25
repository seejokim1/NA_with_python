"""
(5.1.3) 리만 합 구현 및 가시화
Numerical Analysis with Python

교재 본문 예제 코드
"""


import numpy as np
import matplotlib.pyplot as plt

# 함수 정의
def f(x):
    return x**2  # 예제 함수: f(x) = x^2

# 리만 합 계산 함수
def riemann_sum(f, a, b, n, method="left"):
    dx = (b - a) / n
    x = np.linspace(a, b, n + 1)
    
    if method == "left":
        x_points = x[:-1]  # 좌측 리만 합
    elif method == "right":
        x_points = x[1:]  # 우측 리만 합
    elif method == "midpoint":
        x_points = (x[:-1] + x[1:]) / 2  # 중앙 리만 합
    else:
        raise ValueError("method must be 'left', 'right', or 'midpoint'")
    
    return np.sum(f(x_points) * dx)

# 적분 구간 및 함수 정의
a, b = 0, 2  # 적분 구간
n = 10  # 구간 개수

# 리만 합 계산
left_sum = riemann_sum(f, a, b, n, method="left")
right_sum = riemann_sum(f, a, b, n, method="right")
midpoint_sum = riemann_sum(f, a, b, n, method="midpoint")

# 결과 출력
print(f"Left Riemann Sum: {left_sum}")
print(f"Right Riemann Sum: {right_sum}")
print(f"Midpoint Riemann Sum: {midpoint_sum}")

# 가시화
x = np.linspace(a, b, 100)
y = f(x)

x_rect = np.linspace(a, b, n + 1)
dx = (b - a) / n

# 리만 합 그림 그리기
plt.figure(figsize=(8, 6))
plt.plot(x, y, 'b-', label='f(x) = x^2')

# 좌측 리만 합 시각화
for i in range(n):
    x_rect_left = [x_rect[i], x_rect[i], x_rect[i+1], x_rect[i+1]]
    y_rect_left = [0, f(x_rect[i]), f(x_rect[i]), 0]
    plt.fill(x_rect_left, y_rect_left, 'r', edgecolor='k', alpha=0.3, label='Left Riemann' if i == 0 else "")

# 중앙 리만 합 시각화
for i in range(n):
    mid_x = (x_rect[i] + x_rect[i + 1]) / 2
    x_rect_mid = [x_rect[i], x_rect[i], x_rect[i+1], x_rect[i+1]]
    y_rect_mid = [0, f(mid_x), f(mid_x), 0]
    plt.fill(x_rect_mid, y_rect_mid, 'g', edgecolor='k', alpha=0.3, label='Midpoint Riemann' if i == 0 else "")

# 우측 리만 합 시각화
for i in range(n):
    x_rect_right = [x_rect[i], x_rect[i], x_rect[i+1], x_rect[i+1]]
    y_rect_right = [0, f(x_rect[i+1]), f(x_rect[i+1]), 0]
    plt.fill(x_rect_right, y_rect_right, 'b', edgecolor='k', alpha=0.3, label='Right Riemann' if i == 0 else "")

# 그래프 설정
plt.legend(loc='upper left', fontsize=10)
plt.title('Riemann Sums Visualization')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid()
plt.show()
