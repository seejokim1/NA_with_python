"""
(2.2) 증분법 (Incremental Search Method)
Numerical Analysis with Python

교재 본문 예제 코드
"""

import numpy as np

# -------------------------------------------------
# 함수 정의
# -------------------------------------------------
def f(x):
    return x**3 - x - 2


# -------------------------------------------------
# 증분법 함수
# -------------------------------------------------
def incremental_search(f, x_start, x_end, dx):
    """
    Incremental Search Method
    """
    x = x_start
    roots = []

    while x < x_end:
        if f(x) * f(x + dx) < 0:
            roots.append((x, x + dx))
        x += dx

    return roots


# -------------------------------------------------
# 실행 예제
# -------------------------------------------------
if __name__ == "__main__":

    x_start = 0.0
    x_end   = 2.0
    dx      = 0.1

    intervals = incremental_search(f, x_start, x_end, dx)

    print("근이 존재하는 구간:")
    for interval in intervals:
        print(interval)
