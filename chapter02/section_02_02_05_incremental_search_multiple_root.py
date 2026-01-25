"""
(2.2) 증분법 (Incremental Search Method)
(2.2.5) 중근을 갖는 경우
Numerical Analysis with Python
"""

import numpy as np

# -------------------------------------------------
# (2.2.5) 중근을 고려한 증분 탐색 함수 (교재 원본)
# -------------------------------------------------
def incremental_search_with_derivative(f, df, x_start, x_end, step_size, tol=1e-6):
    """
    점진탐색법에 기울기 조건 추가

    Parameters:
        f: 함수
        df: 함수의 도함수
        x_start: 시작점
        x_end: 끝점
        step_size: 탐색 간격
        tol: 기울기 허용 오차

    Returns:
        중근이 존재할 수 있는 구간 또는 None
    """
    x = x_start
    while x < x_end:
        if abs(f(x)) < tol or abs(df(x)) < tol:  # 함수 값 또는 기울기가 0에 가까움
            return x
        x += step_size
    return None


# -------------------------------------------------
# 예제: 중근을 가지는 함수
# -------------------------------------------------
f = lambda x: (x - 1)**2        # 중근 함수
df = lambda x: 2 * (x - 1)      # 도함수


if __name__ == "__main__":
    root = incremental_search_with_derivative(f, df, 0, 2, 0.1)
    print("중근에 근접한 점:", root)
