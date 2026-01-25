"""
(2.4) 뉴턴–랩슨법 (Newton–Raphson Method)
(2.4.4) 파이썬 소스 코드 함수 구현
(반복 과정 상세 출력)
"""

def newton_raphson(f, df, x0, tol=1e-6, max_iter=100):
    """
    뉴턴-랩슨법 구현 함수 (반복 과정 상세 출력)

    Parameters:
        f: 근을 구할 함수
        df: 함수의 도함수
        x0: 초기 추정치
        tol: 허용 오차
        max_iter: 최대 반복 횟수

    Returns:
        근의 근사값
    """
    x = x0
    print(f"초기 추정값: x0 = {x0}")
    for i in range(max_iter):
        fx = f(x)
        dfx = df(x)
        if abs(fx) < tol:
            print(f"반복 {i + 1}: x = {x:.6f}, f(x) = {fx:.6e}, 수렴")
            return x
        if dfx == 0:
            raise ValueError("미분값이 0이 되어 수렴하지 않습니다.")
        print(f"반복 {i + 1}: x = {x:.6f}, f(x) = {fx:.6e}, f'(x) = {dfx:.6e}")
        x -= fx / dfx
    raise ValueError("최대 반복 횟수를 초과하여 수렴하지 않았습니다.")


# -------------------------------------------------
# 함수와 도함수 정의
# -------------------------------------------------
f = lambda x: x**3 - 6*x**2 + 11*x - 6
df = lambda x: 3*x**2 - 12*x + 11


# -------------------------------------------------
# 뉴턴–랩슨법 실행
# -------------------------------------------------
x0 = 2.1  # 초기 추정값
root = newton_raphson(f, df, x0)
print("뉴턴-랩슨법으로 구한 근:", root)
