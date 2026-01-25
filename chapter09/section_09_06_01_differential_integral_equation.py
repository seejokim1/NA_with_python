# section_09_06_01_differential_integral_equation.py
# (9.6.1) Differential-Integral Equation Solution (Euler, RK2, RK4)
# (9.6) 1.1. 미분-적분 방정식 수치기법


import numpy as np
import matplotlib.pyplot as plt

# 시간 설정
t0, tf = 0, 5  # 초기 및 종료 시간
dt = 0.5  # 시간 간격
t = np.arange(t0, tf + dt, dt)  # 시간 배열

# 초기 조건
y_euler = np.zeros(len(t))
y_rk2 = np.zeros(len(t))
y_rk4 = np.zeros(len(t))
y_euler[0] = 1  # Euler 초기 조건
y_rk2[0] = 1  # RK2 초기 조건
y_rk4[0] = 1  # RK4 초기 조건

# 적분항 초기화
integral = np.zeros(len(t))

# 방정식 정의
def f(t, y, integral):
    return -y + integral

# Euler, RK2 및 RK4 선택적으로 사용
def solve_differential_integral(param):
    global y_euler, y_rk2, y_rk4

    for i in range(1, len(t)):
        # 적분항 계산 (누적합)
        integral[i] = integral[i-1] + np.exp(-t[i-1]) * dt

        if param == 4 or param == 1:  # Euler 방법
            y_euler[i] = y_euler[i-1] + dt * f(t[i-1], y_euler[i-1], integral[i-1])

        if param == 4 or param == 2:  # RK2 사용
            k1_rk2 = f(t[i-1], y_rk2[i-1], integral[i-1])
            k2_rk2 = f(t[i-1] + dt, y_rk2[i-1] + dt * k1_rk2, integral[i-1])
            y_rk2[i] = y_rk2[i-1] + (dt / 2) * (k1_rk2 + k2_rk2)

        if param == 4 or param == 3:  # RK4 사용
            k1_rk4 = f(t[i-1], y_rk4[i-1], integral[i-1])
            k2_rk4 = f(t[i-1] + dt / 2, y_rk4[i-1] + dt / 2 * k1_rk4, integral[i-1])
            k3_rk4 = f(t[i-1] + dt / 2, y_rk4[i-1] + dt / 2 * k2_rk4, integral[i-1])
            k4_rk4 = f(t[i-1] + dt, y_rk4[i-1] + dt * k3_rk4, integral[i-1])
            y_rk4[i] = y_rk4[i-1] + (dt / 6) * (k1_rk4 + 2 * k2_rk4 + 2 * k3_rk4 + k4_rk4)

    if param not in [1, 2, 3, 4]:
        raise ValueError("Invalid parameter: Use param=1 for Euler, param=2 for RK2, param=3 for RK4, param=4 for all methods")

# 사용자 입력에 따라 Euler, RK2, RK4, 또는 모두 실행
param = int(input("Enter 1 for Euler, 2 for RK2, 3 for RK4, or 4 for all: "))
solve_differential_integral(param)

# 결과 시각화
if param == 1:
    plt.plot(t, y_euler, label="Euler")
elif param == 2:
    plt.plot(t, y_rk2, label="RK2")
elif param == 3:
    plt.plot(t, y_rk4, label="RK4")
elif param == 4:
    plt.plot(t, y_euler, label="Euler")
    plt.plot(t, y_rk2, label="RK2")
    plt.plot(t, y_rk4, label="RK4")

plt.xlabel("Time (t)")
plt.ylabel("y(t)")
plt.title("Differential-Integral Equation Solution (Euler, RK2, RK4)")
plt.legend()
plt.grid()
plt.show()

