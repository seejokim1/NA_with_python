# section_07_02_02_polyfit_polynomial_approximation.py
# (7.2.2) np.polyfit 이용한 m 차 다항식 근사 소스코드

import numpy as np
import matplotlib.pyplot as plt

# ------------------------------------------------------------------
# 주어진 데이터 포인트
# ------------------------------------------------------------------
x = np.array([1, 2, 3, 4, 5], dtype=float)     # x 좌표
y = np.array([1, 4, 9, 16, 25], dtype=float)  # y 좌표

# ------------------------------------------------------------------
# m 차 다항식 근사 (최소자승법)
# ------------------------------------------------------------------
coeff1 = np.polyfit(x, y, 1)  # 1차 다항식 근사
coeff2 = np.polyfit(x, y, 2)  # 2차 다항식 근사
coeff3 = np.polyfit(x, y, 3)  # 3차 다항식 근사

# 다항식으로부터 y 값 계산
poly1 = np.polyval(coeff1, x)
poly2 = np.polyval(coeff2, x)
poly3 = np.polyval(coeff3, x)

# ------------------------------------------------------------------
# 결과 시각화
# ------------------------------------------------------------------
plt.figure(figsize=(8, 6))

# 데이터 포인트
plt.scatter(
    x, y,
    color='red', label='Data Points', zorder=5
)

# 다항식 근사 곡선
plt.plot(x, poly1, color='blue', label='1차 다항식 근사', linewidth=2)
plt.plot(x, poly2, color='green', label='2차 다항식 근사', linewidth=2)
plt.plot(x, poly3, color='black', label='3차 다항식 근사', linewidth=2)

# 그래프 설정
plt.xlabel('x')
plt.ylabel('y')
plt.title('np.polyfit을 이용한 m 차 다항식 근사')
plt.legend()
plt.grid(True)

plt.show()
