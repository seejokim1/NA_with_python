"""
(3.2.6) 수치적 안정성을 위한 부분 피벗팅
Gaussian Elimination with Partial Pivoting
Numerical Analysis with Python
"""

import numpy as np

def gauss_elimination_with_pivoting(A, b):
    """
    가우스 소거법 (부분 피봇팅 포함, 과정 출력)

    Parameters:
        A: 계수 행렬 (numpy array)
        b: 상수 벡터 (numpy array)

    Returns:
        x: 해 벡터
    """
    n = len(b)

    print("초기 상태:")
    print("A =\n", A)
    print("b =", b)
    print()

    # 전진 소거
    for i in range(n):
        # 부분 피봇팅
        max_row = np.argmax(abs(A[i:, i])) + i
        if max_row != i:
            print(f"부분 피봇팅: 행 {i}와 행 {max_row} 교환")
            A[[i, max_row]] = A[[max_row, i]]
            b[[i, max_row]] = b[[max_row, i]]
            print("A =\n", A)
            print("b =", b)
            print()

        # 가우스 소거
        for j in range(i + 1, n):
            factor = A[j, i] / A[i, i]
            A[j, i:] -= factor * A[i, i:]
            b[j] -= factor * b[i]

        print(f"가우스 소거 후 (단계 {i + 1}):")
        print("A =\n", A)
        print("b =", b)
        print()

    # 후진 대입
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (b[i] - np.dot(A[i, i + 1:], x[i + 1:])) / A[i, i]

    return x


# 문제 정의
A = np.array([[0, 10, 10],
              [0, 0, 5],
              [1, 1, 1]], dtype=float)

b = np.array([20, 5, 3], dtype=float)

# 가우스 소거법 수행
x = gauss_elimination_with_pivoting(A, b)

# 결과 출력
print("최종 해 벡터 x:")
for i, val in enumerate(x):
    print(f"x{i+1} = {val}")
