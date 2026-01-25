"""
(3.2.4) 후진 대입 (Backward Substitution)
Numerical Analysis with Python
"""

import numpy as np

# 후진 대입(Back Substitution)을 수행하는 함수
def back_substitution(a, b, n):
    """
    후진 대입(Back Substitution) 과정:
    상삼각 행렬 형태의 계수 행렬 A와 벡터 b를 사용해 미지수 x를 계산.

    Args:
        a: (numpy.ndarray) 상삼각 행렬 형태의 계수 행렬 (n x n 크기)
        b: (numpy.ndarray) 상수 벡터
        n: (int) 행렬의 크기 (a는 n x n 행렬)

    Returns:
        x: (numpy.ndarray) 계산된 미지수 벡터
    """
    # 미지수 x를 저장할 벡터 (초기값: 모두 0)
    x = np.zeros((n, 1))

    # 마지막 행부터 계산
    x[n-1] = b[n-1] / a[n-1, n-1]

    # 아래에서 위로 계산
    for row in range(n-2, -1, -1):
        sums = b[row]
        for j in range(row+1, n):
            sums = sums - a[row, j] * x[j]
        x[row] = sums / a[row, row]

    print('A = \n%s and b = %s' % (a, b))
    return x


# 상삼각 행렬 A와 상수 벡터 b 정의
A = np.array([[1, 1, 2],
              [0, -2, 1],
              [0, 0, 2]])

b = np.array([2, 6, 4])

# 후진 대입 수행
x = back_substitution(A, b, 3)

# 결과 출력
print('x = %s' % (x))
