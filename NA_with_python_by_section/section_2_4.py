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
# 함수와 도함수 정의