② 예제 코드 실행 결과
    return I
if __name__ == '__main__':
    # 적분할 함수 정의
    def func(x):
        return np.sin(x)  # 함수 f(x) = sin(x)
    # Romberg 적분 설정
    a = 0  # 적분 구간 시작점
    b = np.pi / 2  # 적분 구간 끝점
    p_rows = 4  # Romberg 행렬 크기
    # Romberg 적분 수행
    print("Romberg 적분 결과:")
    I = romberg(func, a, b, p_rows)
    solution = I[p_rows-1, p_rows-1]  # 최종 적분값
    # 정확한 적분값 계산 (f(x) = sin(x)의 해석적 적분)
    exact_value = 1.0  # ∫[0, π/2] sin(x) dx = 1
    # 절대 오차 계산
    error = abs(exact_value - solution)
    # 결과 출력
    print("\n최종 Romberg 적분값 =", solution)
    print("정확한 적분값 =", exact_value)
    print("절대 오차 =", error)