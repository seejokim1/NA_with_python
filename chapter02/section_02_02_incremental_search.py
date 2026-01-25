"""
(2.2) 증분법 (Incremental Search Method)
(2.2.3) 파이썬 소스 코드 함수 구현
Numerical Analysis with Python
"""

# -------------------------------------------------
# (2.2.3) 증분법 함수 구현 (교재 원본)
# -------------------------------------------------
def incremental_search(f, x_start, x_end, step_size):
    """
    점진탐색법 구현 함수

    Parameters:
        f: 탐색할 함수
        x_start: 탐색 시작점
        x_end: 탐색 끝점
        step_size: 구간 분할 간격

    Returns:
        근이 포함된 구간 또는 None
    """
    x = x_start
    while x < x_end:
        if f(x) * f(x + step_size) < 0:  # 부호 변화 점검
            return (x, x + step_size)
        x += step_size
    return None  # 근이 발견되지 않음


# -------------------------------------------------
# (2.2.4) 예제
# -------------------------------------------------
def f(x):
    return x**3 - x - 2


if __name__ == "__main__":
    x_start = 0.0
    x_end = 2.0
    step_size = 0.1

    result = incremental_search(f, x_start, x_end, step_size)

    if result:
        print("근이 포함된 구간:", result)
    else:
        print("근을 찾지 못했습니다.")
