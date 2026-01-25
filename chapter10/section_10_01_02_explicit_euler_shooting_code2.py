# section_10_01_02_explicit_euler_shooting_case2.py
# (10.1) 선형 Shooting Method
# (10.1.2) Explicit Euler Method 예제
# Explicit Euler Method 코드 2

import numpy as np
import matplotlib.pyplot as plt

# ------------------------------------------------------------------
# 계수 정의
# y'' + B y' + A y = 0
# ------------------------------------------------------------------
A = 3.0
B = 1.0

# 상태방정식 행렬
A_ = np.array([[0.0, 1.0],
               [-A, -B]])

# ------------------------------------------------------------------
# 수치해석 설정
# ------------------------------------------------------------------
dx = 0.0005
x_end = 3.0

# 초기 조건
# y(0) = 3, dy/dx(0) = 0
y0 = np.array([3.0, 0.0])

# ------------------------------------------------------------------
# Explicit Forward Euler Method
# ------------------------------------------------------------------
n_steps = int(x_end / dx) + 1
x = np.zeros(n_steps)
y = np.zeros((2, n_steps))

y[:, 0] = y0

for n in range(n_steps - 1):
    x[n + 1] = x[n] + dx
    y[:, n + 1] = (np.eye(2) + dx * A_) @ y[:, n]

# ------------------------------------------------------------------
# 결과 시각화
# ------------------------------------------------------------------
# y(x)
plt.figure()
plt.plot(x, y[0, :], label='y(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Explicit Euler Method: y(x)')
plt.grid()
plt.legend()

# dy/dx
plt.figure()
plt.plot(x, y[1, :], label='dy/dx', color='orange')
plt.xlabel('x')
plt.ylabel('dy/dx')
plt.title('Explicit Euler Method: dy/dx(x)')
plt.grid()
plt.legend()

plt.show()
