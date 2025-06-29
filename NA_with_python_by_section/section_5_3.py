for k in range(1, n):  # 중간 구간의 함수값 누적
        x = x + h
        In += 2 * f(x)
    return (In + f(b)) * h * 0.5
def richardson_extrapolation(f, a, b, n1, n2):
    """
    Richardson Extrapolation을 사용하여 적분값 계산
    Parameters:
    - f: 적분할 함수
    - a: 적분 구간 시작점
    - b: 적분 구간 끝점
    - n1: 첫 번째 구간 분할 수
    - n2: 두 번째 구간 분할 수 (n2 > n1)
    Returns:
    - Richardson Extrapolation으로 계산된 적분값
    """
    # 두 개의 복합 사다리꼴 공식 값 계산
    I1 = trapezcomp(f, a, b, n1)  # 적분값 (n1 구간)
    I2 = trapezcomp(f, a, b, n2)  # 적분값 (n2 구간)
    # Richardson Extrapolation 공식
    I_richardson = (4 * I2 - I1) / (4 - 1)
    return I1, I2, I_richardson
if __name__ == '__main__':
    def func(x):
        return np.sin(x)  # 적분할 함수 f(x) = sin(x)
    # 적분 구간 및 분할 수
    a = 0
    b = np.pi / 2
    n1 = 4  # 첫 번째 분할 수
    n2 = 8  # 두 번째 분할 수 (n2 > n1)
    # Richardson Extrapolation 수행
    I1, I2, I_richardson = richardson_extrapolation(func, a, b, n1, n2)
    # 출력