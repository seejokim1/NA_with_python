"""
(2.3) 이분법 (Bisection Method)
(2.3.3) Python SciPy 라이브러리를 활용한 이분법
Numerical Analysis with Python
"""

from scipy.optimize import bisect


# -------------------------------------------------
# 함수 정의
# -------------------------------------------------
f = lambda x: x**2 - 4


# -------------------------------------------------
# SciPy 이분법 실행
# -------------------------------------------------
if __name__ == "__main__":
    root = bisect(f, 1, 3)
    print("SciPy 이분법으로 구한 근:", root)
