"""
(2.3) 이분법 (Bisection Method)
(2.3.2) 이분법 알고리즘
Numerical Analysis with Python
"""

# -------------------------------------------------
# (2.3.2) 이분법 알고리즘 (반복 과정 출력 포함)
# -------------------------------------------------
def bisection(f, a, b, tol=1e-6, max_iter=100):
    """
    이분법(Bisection Method) 구현 함수 (반복 과정 출력 포함)

    Parameters:
        f: 근을 구할 함수
        a: 구간의 시작점
        b: 구간의 끝점
        tol: 허용 오차
        max_iter: 최대 반복 횟수

    Returns:
        근의 근사값
    """
    if f(a) * f(b) >= 0:
        raise ValueError("구간 [a, b]에 근이 포함되지 않았습니다.")
    
    print(f"초기 구간: [a, b] = [{a}, {b}]")
    iter_count = 0

    while abs(b - a) > tol and iter_count < max_iter:
        c = (a + b) / 2  # 중간값
        print(
            f"반복 {iter_count + 1}: "
            f"[a, b] = [{a:.6f}, {b:.6f}], "
            f"c = {c:.6f}, f(c) = {f(c):.6e}"
        )

        # 정확한 근 또는 허용 오차 만족
        if f(c) == 0 or abs(b - a) < tol:
            print(f"최종 구간: [a, b] = [{a:.6f}, {b:.6f}]")
            return c

        # 부호 변화에 따라 구간 축소
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

        iter_count += 1

    print(f"최종 구간: [a, b] = [{a:.6f}, {b:.6f}]")
    return (a + b) / 2


# -------------------------------------------------
# 예제: 2차 다항식 f(x) = x^2 - 4
# -------------------------------------------------
def quadratic_function(x):
    return x**2 - 4


if __name__ == "__main__":
    # 초기 구간
    a = 1
    b = 5
    tol = 1e-6

    # 이분법 실행
    root = bisection(quadratic_function, a, b, tol)

    # 결과 출력
    print(f"\nf(x) = x^2 - 4의 근: x = {root:.6f}")
    print(f"f({root:.6f}) = {quadratic_function(root):.6e}")
