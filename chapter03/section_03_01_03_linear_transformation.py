"""
(3.1.3) 행렬의 선형변환
Numerical Analysis with Python
"""

import numpy as np

# 행렬 A 정의
A = np.array([[-2, 1],
              [1, -3]])

# 기본 벡터
e1 = np.array([1, 0])  # x축 단위 벡터
e2 = np.array([0, 1])  # y축 단위 벡터

# 변환 결과 계산
transformed_e1 = A @ e1
transformed_e2 = A @ e2

print("A:\n", A)
print("Transformed e1 (green vector):", transformed_e1)
print("Transformed e2 (red vector):", transformed_e2)
