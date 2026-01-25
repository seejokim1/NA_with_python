"""
(5.2.2) 사다리꼴 적분(Trapezoidal Rule) Python 프로그래밍 1
Numerical Analysis with Python

교재 본문 예제 코드
"""

# 사다리꼴 공식 구현: 에러 출력 및 주석 추가

def f(x):
    # 정의된 함수: f(x) = x + 3
    return x + 3

# 적분 구간 [a, b]
a = 0  # 시작 값
b = 10  # 끝 값

# 구간 분할 수
n = 100  # 사다리꼴 구간 수
sum1 = 0  # 중간점 합 초기화

# 사다리꼴 공식의 중간점 계산
for i in range(1, n):  # 1부터 n-1까지 반복 (수정: 범위 오류)
    x = a + (b - a) / n * i  # 현재 x값 계산
    sum1 += f(x)  # 중간점 함수 값 누적

# 사다리꼴 적분 공식
trapezoid = (b - a) * (f(a) + 2 * sum1 + f(b)) / (2 * n)

# 출력
print("사다리꼴 공식의 적분값 =", trapezoid)

# 정확값 계산 (적분값 f(x) = x + 3의 해석적 적분 결과: F(x) = 0.5*x^2 + 3x)
exact_value = (0.5 * b**2 + 3 * b) - (0.5 * a**2 + 3 * a)

# 절대 오차 계산
error = abs(exact_value - trapezoid)
print("정확한 값 =", exact_value)
print("절대 오차 =", error)

