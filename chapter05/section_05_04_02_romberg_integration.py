"""
(5.4.2) Romberg integration Python 프로그래밍
Numerical Analysis with Python

교재 본문 예제 코드
"""

import numpy as np

# 복합 사다리꼴 공식 함수 정의
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

# Romberg 적분 함수 정의
def romberg(f, a, b, p):
    """
    Romberg 적분법으로 적분값 계산
    """
    I = np.zeros((p, p))
    for k in range(0, p):
        I[k, 0] = trapezcomp(f, a, b, 2**k)

        for j in range(0, k):
            I[k, j+1] = (4**(j+1) * I[k, j] - I[k-1, j]) / (4**(j+1) - 1)

        print(f"Step {k + 1}: {I[k, 0:k+1]}")

    return I

if __name__ == '__main__':

    def func(x):
        return np.sin(x)

    a = 0
    b = np.pi / 2
    p_rows = 4

    print("Romberg 적분 결과:")
    I = romberg(func, a, b, p_rows)
    solution = I[p_rows-1, p_rows-1]

    exact_value = 1.0
    error = abs(exact_value - solution)

    print("\n최종 Romberg 적분값 =", solution)
    print("정확한 적분값 =", exact_value)
    print("절대 오차 =", error)
