"""
(3.1.4) 해 존재를 위한 행렬의 행공간(row space)과 영공간(null space)
Numerical Analysis with Python
"""

import numpy as np
from scipy.linalg import null_space

# 행렬과 벡터 정의
A = np.array([[1, 2], [2, 4]])  # 계수 행렬
b = np.array([8, 4])  # 상수 벡터

# 선형 연립방정식의 해 찾기
try:
    x_particular = np.linalg.solve(A, b)  # 특정 해 계산
except np.linalg.LinAlgError:
    x_particular = "해를 구할 수 없음 (행렬이 특이행렬)"

# 영공간(null space) 계산
null_space_vector = null_space(A)

# 결과 출력
print("계수 행렬 A:")
print(A)
print("\n상수 벡터 b:")
print(b)
print("\n특정 해 (x_particular):")
print(x_particular)
print("\n영공간 벡터 (null_space):")
print(null_space_vector)
