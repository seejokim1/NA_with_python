# section_09_06_01_differential_integral_equation.py
# (9.6.1) Differential-Integral Equation Solution (Euler, RK2, RK4)
# (9.6) 1.1. 미분-적분 방정식 수치기법

import numpy as np
import matplotlib.pyplot as plt

# ------------------------------------------------------------------
# 시간 설정
# ------------------------------------------------------------------
t0, tf = 0.0, 5.0        # 초기 및 종료 시간
dt = 0.5                # 시간 간격
t = np.arange(t0, tf + dt, dt)

# ------------------------------------------------------------------
# 초기 조건
# ------------------------------------------------------------------
y_euler = np.zeros(len(t))
y_rk2 = np.zeros(len(t))
y_rk4 = np.zeros(len(t))

y_euler[0] = 1.0
y_rk2[0] = 1.0
y_rk4[0] = 1.0

# ------------------------------------------------------------------
# 적분항 초기화
# I(t) = ∫ exp(-t) dt (수치적으로 누적 계산)
# ------------------------------------------------------------------
integral = np.zeros(len(t))

# ------------------------------------------------------------------
# 미분-적분 방정식 정의
# y'(t) = -y(t) + ∫ exp(-t) dt
# ------------------------------------------------------------------
def f(t, y, integral):
    return -y + integral

# ------------------------------------------------------------------
# 미분-적분 방정식 풀이
# param = 1 (Euler), 2 (RK2), 3 (RK4), 4 (All)
# ------------------------------------------------------------------
def solve_differential_integral(param):
    global y_euler, y_rk2, y_rk4

    for i in range(1, len(t)):
        # 적분항 누적 계산
        integral[i] = integral[i-1] + np.exp(-t[i-1]) * dt

        # Euler 방법
        if param == 1 or param == 4:
            y_euler[i] = y_euler[i-1] + dt * f(t[i-1], y_euler[i-1], integral[i-1])

        # RK2 방법
        if param == 2 or param == 4:
            k1 = f(t[i-n:=i-1], y_rk2[i-1], integral[i-1])
            k2 = f(t[i-1] + dt, y_rk2[i-1] + dt * k1, integral[i-1])
            y_rk2[i] = y_rk2[i-1] + 0.5 * dt * (k1 + k2)

        # RK4 방법
        if param == 3 or param == 4:
            k1 = f(t[i-1], y_rk4[i-1], integral[i-1])
            k2 = f(t[i-1] + dt/2, y_rk4[i-1] + dt/2 * k1, integral[i-1])
            k3 = f(t[i-1] + dt/2, y_rk4[i-1] + dt/2 * k2, integral[i-1])
            k4 = f(t[i-1] + dt, y_rk4[i-1] + dt * k3, integral[i-1])
            y_rk4[i] = y_rk4[i-1] + (dt/6) * (k1 + 2*k2 + 2*k3 + k4)

    if param not in [1, 2, 3, 4]:
        raise ValueError("param은 1(Euler), 2(RK2), 3(RK4), 4(All) 중 하나여야 한다.")

# -----
