"""
(3.2.5) 가우스 소거법 전체 코드 함수 구현
Numerical Analysis with Python
"""

import numpy as np

# 전진 소거 함수
def forward_elimination(A, b, n):
    """
    전진 소거(Forward Elimination) 과정:
    주어진 행렬 A와 벡터 b를 상삼각 형태로 변환.
    """
    for row in range(0, n-1):
        for i in range(row+1, n):
            factor = A[i, row] / A[row, row]
            for j in range(row, n):
                A[i, j] = A[i, j] - factor * A[row, j]
            b[i] = b[i] - factor * b[row]
    return A, b


# 후진 대입 함수
def back_substitution(a, b, n):
    """
    후진 대입(Back Substitution) 과정:
    상삼각 행렬 형태의 계수 행렬 A와 벡터 b를 사용해 미지수 x를 계산.
    """
    x = np.zeros((n, 1))
    x[n-1] = b[n-1] / a[n-1, n-1]

    for row in range(n-2, -1, -1):
        sums = b[row]
        for j in range(row+1, n):
            sums = sums - a[row, j] * x[j]
        x[row] = sums / a[row, row]

    return x


# 문제 정의
A = np.array([[2, 1, -1],
              [-3, -1, 2],
              [-2, 1, 2]], dtype=float)

b = np.array([8, -11, -3], dtype=float)
n = 3

print("주어진 연립 방정식:")
for i in range(n):
    equation = " + ".join([f"{A[i, j]}*x{j+1}" for j in range(n)]) + f" = {b[i]}"
    print(equation)
print()

# 전진 소거
A, b = forward_elimination(A, b, n)

# 후진 대입
x = back_substitution(A, b, n)

# 결과 출력
print("계수 행렬 (상삼각 형태):")
print(A)

print("\n변환된 상수 벡터:")
print(b)

print("\n미지수 벡터 (해):")
print(x)
