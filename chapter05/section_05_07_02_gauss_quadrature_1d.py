"""
(5.7.2) 가우스 구적법(Gauss–Legendre) 1중 적분
Numerical Analysis with Python

교재 본문 예제 코드
"""

import numpy as np

# 1D 함수 정의
def f_1d(x):
    return np.exp(-x**2)

# Gauss-Legendre 2점 법칙의 가중치와 노드
weights = np.array([1, 1])
nodes = np.array([-1 / np.sqrt(3), 1 / np.sqrt(3)])

# 적분 구간
a, b = 0, 1

# 구간 변환: [-1, 1] → [a, b]
transformed_nodes_1d = (b - a) / 2 * nodes + (b + a) / 2

# 가우스 구적법 적분 계산
integral_1d = (b - a) / 2 * np.sum(weights * f_1d(transformed_nodes_1d))

# 결과 출력
print(f"1중 적분 결과: {integral_1d}")
