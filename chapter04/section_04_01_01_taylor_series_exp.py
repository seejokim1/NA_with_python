"""
(4.1.1) Taylor Series (Maclaurin Series) Python 코드
exp(x)의 테일러 급수 근사

Numerical Analysis with Python
"""

import numpy as np
import matplotlib.pyplot as plt


def taylor_exp_series(x, order):
    """
    exp(x)의 Maclaurin 급수 근사 계산

    Parameters:
        x     : numpy array
        order : 다항식 차수

    Returns:
        y : Taylor 근사값
    """
    y = np.zeros_like(x, dtype=float)
    for n in range(order + 1):
        y += x**n / np.math.factorial(n)
    return y


# x 값 정의
x = np.arange(0, 3.01, 0.01)

# 실제 함수
y_exact = np.exp(x)

# Taylor 근사
y0 = taylor_exp_series(x, 0)  # 0차
y1 = taylor_exp_series(x, 1)  # 1차
y3 = taylor_exp_series(x, 3)  # 3차

# 그래프 출력
plt.figure(figsize=(8, 6))

plt.plot(x, y_exact, 'k', linewidth=3, label='y = exp(x)')
plt.plot(x, y0, 'b--', linewidth=2, label='0th order')
plt.plot(x, y1, 'r-.', linewidth=2, label='1st order')
plt.plot(x, y3, 'g--', linewidth=2, label='3rd order')

plt.title("Taylor Series Approximation of exp(x)")
plt.xlabel("x")
plt.ylabel("y")
plt.axis([0, 3, 0, 10])
plt.grid(True)
plt.legend()
plt.show()
