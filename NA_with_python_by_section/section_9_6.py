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
            y_rk4[i] = y_rk4[i-1] + (dt / 6) * (k1_rk4 + 2 * k2_rk4 + 2 * k3_rk4 +