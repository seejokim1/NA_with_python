"""
(5.5.2) Simpson's 1/3rd Rule 프로그래밍
Numerical Analysis with Python

교재 본문 예제 코드
"""

# 함수와 적분 범위 설정
def f(x):
    """
    함수 정의: f(x) = x + 3
    """
    return x + 3

# 적분 구간과 분할 수
a = 0   # 적분 구간 시작점
b = 10  # 적분 구간 끝점
n = 100  # 구간 분할 수 (짝수 필요)

# 합 초기화
sum1 = 0     # 사다리꼴 공식 중간 합
sumeven = 0  # Simpson 짝수항 합
sumodd = 0   # Simpson 홀수항 합

# 구간별 합 계산
for i in range(1, n):
    x = a + (b - a) / n * i

    if i % 2 == 0:
        sumeven += f(x)
    else:
        sumodd += f(x)

    sum1 += f(x)

# 사다리꼴 공식
trapezoid = (b - a) * (f(a) + 2 * sum1 + f(b)) / (2 * n)

# Simpson's 1/3 Rule
simpson = (b - a) * (f(a) + 4 * sumodd + 2 * sumeven + f(b)) / (3 * n)

# 정확한 해석적 적분값
exact_value = (0.5 * b**2 + 3 * b) - (0.5 * a**2 + 3 * a)

# 오차 계산
trapezoid_error = abs(exact_value - trapezoid)
simpson_error = abs(exact_value - simpson)

# 결과 출력
print("사다리꼴 공식의 값 =", trapezoid)
print("심슨 공식의 값 =", simpson)
print("정확한 적분값 =", exact_value)
print("사다리꼴 공식의 오차 =", trapezoid_error)
print("심슨 공식의 오차 =", simpson_error)
