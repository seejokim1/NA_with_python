"""
(2.4) 뉴턴–랩슨법 (Newton–Raphson Method)
(2.4.6) Python SciPy 이용한 뉴턴–랩슨법
Numerical Analysis with Python
"""

from scipy.optimize import newton


# -------------------------------------------------
# 함수와 도함수 정의
# -------------------------------------------------
f = lambda x: x**3 - 6*x**2 + 11*x - 6
df = lambda x: 3*x**2 - 12*x + 11


# -------------------------------------------------
# SciPy 뉴턴–랩슨법 실행
# -------------------------------------------------
if __name__ == "__main__":
    root = newton(f, x0=2.5, fprime=df)
    print("SciPy 뉴턴-랩슨법으로 구한 근:", root)
