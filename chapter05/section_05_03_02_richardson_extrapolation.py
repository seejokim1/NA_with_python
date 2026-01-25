"""
(5.3.2) Richardson Extrapolation 파이썬 코드
Numerical Analysis with Python

교재 본문 예제 코드
"""

import numpy as np

def trapezcomp(f, a, b, n):
    """
    복합 사다리꼴 공식으로 적분값 계산
    """
    h = (b - a) / n
    x = a
    In = f(a)
    for k in range(1, n):
        x = x + h
        In += 2 * f(x)
    return (In + f(b)) * h * 0.5

def richardson_extrapolation(f, a, b, n1, n2):
    """
    Richardson Extrapolation을 사용하여 적분값 계산
    """
    I1 = trapezcomp(f, a, b, n1)
    I2 = trapezcomp(f, a, b, n2)
    I_richardson = (4 * I2 - I1) / (4 - 1)
    return I1, I2, I_richardson

if __name__ == '__main__':

    def func(x):
        return np.sin(x)

    a = 0
    b = np.pi / 2
    n1 = 4
    n2 = 8

    I1, I2, I_richardson = richardson_extrapolation(func, a, b, n1, n2)

    print("사다리꼴 적분값 (n1 구간) =", I1)
    print("사다리꼴 적분값 (n2 구간) =", I2)
    print("Richardson Extrapolation 적분값 =", I_richardson)

    exact_value = 1.0
    error = abs(exact_value - I_richardson)

    print("정확한 값 =", exact_value)
    print("Richardson Extrapolation 오차 =", error)
