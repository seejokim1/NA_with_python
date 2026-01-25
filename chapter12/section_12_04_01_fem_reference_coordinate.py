# section_12_04_01_fem_reference_coordinate.py
# (12.4) 기준좌표계에서의 유한요소법(FEM)
# (12.4.1) 기준좌표계에서의 유한요소법(FEM) 예제
# -*- coding: UTF-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from scipy import linalg

# ------------------------------------------------------------------
# 미분방정식 정보
# d/dx ( a(x) du/dx ) = f(x)
# u(0) = 1, u(1) = e
# ------------------------------------------------------------------
class ode:

    @staticmethod
    def exact_solution(x):
        return np.exp(x)

    @staticmethod
    def function_a(x):
        return 1.0

    @staticmethod
    def function_f(x):
        return -np.exp(x)

    @staticmethod
    def function_g(x):
        if x == 0:
            return 1.0
        elif x == 1:
            return np.exp(1.0)

# ------------------------------------------------------------------
# 기준좌표계 [-1,1] 가우스 적분점
# ------------------------------------------------------------------
def generate_Gauss_reference_1D(nGQP):
    if nGQP == 4:
        w = [0.3478548451, 0.3478548451, 0.6521451549, 0.6521451549]
        xi = [0.8611363116, -0.8611363116, 0.3399810436, -0.3399810436]
    elif nGQP == 2:
        w = [1.0, 1.0]
        xi = [-1 / np.sqrt(3), 1 / np.sqrt(3)]
    return np.array(w), np.array(xi)

# ------------------------------------------------------------------
# 기준좌표계 → 실제좌표계 변환
# ------------------------------------------------------------------
def generate_Gauss_local_1D(w_ref, xi_ref, a, b):
    w = (b - a) * w_ref / 2
    x = (b - a) * xi_ref / 2 + (a + b) / 2
    return w, x

# ------------------------------------------------------------------
# 1차 선형 형상함수
# ------------------------------------------------------------------
def SFN_1D(x, vertices, i):
    if i == 1:
        return (vertices[1] - x) / (vertices[1] - vertices[0])
    elif i == 2:
        return (x - vertices[0]) / (vertices[1] - vertices[0])

def SFN_1D_deri(vertices, i):
    if i == 1:
        return -1.0 / (vertices[1] - vertices[0])
    elif i == 2:
        return  1.0 / (vertices[1] - vertices[0])

# ------------------------------------------------------------------
# 요소 내부 FEM 해
# ------------------------------------------------------------------
def FE_solution_1D(x, uh_local, vertices):
    return (uh_local[0] * SFN_1D(x, vertices, 1)
          + uh_local[1] * SFN_1D(x, vertices, 2))

# ------------------------------------------------------------------
# 전역 강성행렬 및 하중벡터 조립
# ------------------------------------------------------------------
def assemble_1D(left, right, num_elements, nGQP):

    h = (right - left) / num_elements
    nodes = np.linspace(left, right, num_elements + 1)

    A = np.zeros((num_elements + 1, num_elements + 1))
    b = np.zeros(num_elements + 1)

    w_ref, xi_ref = generate_Gauss_reference_1D(nGQP)

    for e in range(num_elements):
        vertices = [nodes[e], nodes[e + 1]]
        w, xg = generate_Gauss_local_1D(w_ref, xi_ref, vertices[0], vertices[1])

        for a in range(2):
            for b_idx in range(2):
                for q in range(len(w)):
                    A[e + a, e + b_idx] += (
                        w[q]
                        * ode.function_a(xg[q])
                        * SFN_1D_deri(vertices, a + 1)
                        * SFN_1D_deri(vertices, b_idx + 1)
                    )

            for q in range(len(w)):
                b[e + a] += (
                    w[q]
                    * ode.function_f(xg[q])
                    * SFN_1D(xg[q], vertices, a + 1)
                )

    # Dirichlet 경계 조건
    A[0, :] = 0.0
    A[0, 0] = 1.0
    b[0] = ode.function_g(left)

    A[-1, :] = 0.0
    A[-1, -1] = 1.0
    b[-1] = ode.function_g(right)

    return A, b, nodes

# ------------------------------------------------------------------
# 메인 함수
# ------------------------------------------------------------------
def main():
    left, right = 0.0, 1.0
    nGQP = 4

    num_elements = int(input("Enter the number of elements: "))

    A, b, nodes = assemble_1D(left, right, num_elements, nGQP)
    uh = linalg.solve(A, b)

    # 결과 시각화
    x_fine = np.linspace(left, right, 200)
    exact_y = ode.exact_solution(x_fine)

    fem_y = []
    for x in x_fine:
        for i in range(len(nodes) - 1):
            if nodes[i] <= x <= nodes[i + 1]:
                fem_y.append(FE_solution_1D(x, uh[i:i+2], [nodes[i], nodes[i+1]]))
                break
    fem_y = np.array(fem_y)

    plt.figure(figsize=(10, 6))
    plt.plot(x_fine, exact_y, label="Exact Solution", color="blue")
    plt.plot(x_fine[:len(fem_y)], fem_y, "--", label="FEM Solution", color="red")

    plt.figtext(0.15, 0.65, r"$\frac{d}{dx}\left(a(x)\frac{du}{dx}\right)=f(x)$", fontsize=12)
    plt.figtext(0.15, 0.55, r"$u(0)=1,\; u(1)=e$", fontsize=12)

    plt.xlabel("x")
    plt.ylabel("u(x)")
    plt.title("기준좌표계 FEM 해와 이론해 비교")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
