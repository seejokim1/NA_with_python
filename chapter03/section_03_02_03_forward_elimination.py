"""
(3.2.3) 전진 소거 알고리즘 (Forward Elimination)
Numerical Analysis with Python
"""

import numpy as np

# 전진 소거를 수행하는 함수
def forward_elimination(A, b, n):
    """
    가우스 소거법의 전진 소거 단계:
    주어진 행렬 A와 벡터 b에 대해, A를 상삼각 행렬로 변환하고
    b를 변환된 A에 맞게 조정한다.

    Args:
        A: (numpy.ndarray) 계수 행렬 (n x n 크기)
        b: (numpy.ndarray) 상수 벡터
        n: (int) 행렬의 크기 (A는 n x n 행렬)

    Returns:
        A: (numpy.ndarray) 상삼각 형태로 변환된 행렬
        b: (numpy.ndarray) 변환된 벡터
    """
    for row in range(0, n-1):  # 첫 번째 행부터 마지막 전 행까지 반복
        for i in range(row+1, n):  # 현재 행 아래의 모든 행에 대해 반복
            factor = A[i, row] / A[row, row]

            for j in range(row, n):
                A[i, j] = A[i, j] - factor * A[row, j]

            b[i] = b[i] - factor * b[row]

    print('A = \n%s and b = %s' % (A, b))
    return A, b


# 초기 행렬 A와 벡터 b 정의
A = np.array([[-1, 1, 2],
              [3, -2, 1],
              [2, -1, 2]])

print("Original A:\n", A)

b = np.array([2, 6, 4])

# 전진 소거 수행
A, b = forward_elimination(A, b, 3)

# 결과 출력
print("Upper Triangular Matrix A:\n", A)
print("Modified Vector b:\n", b)
