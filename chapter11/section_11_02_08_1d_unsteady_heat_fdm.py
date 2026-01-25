# section_11_02_08_1d_unsteady_heat_fdm.py
# (11.2) 유한차분법의 수치해석
# (11.2.8) 1차원 비정상 열전달 FDM 수치해석

import numpy as np
import matplotlib.pyplot as plt

# ------------------------------------------------------------------
# 1차원 비정상 열전달 방정식
# ∂u/∂t = a^2 ∂²u/∂x²
# ------------------------------------------------------------------
def Heat(param=3, n=4, m=24, plot_steps=10):

    # --------------------------------------------------------------
    # 공간 및 시간 영역
    # --------------------------------------------------------------
    x0, xL = 0.0, 1.0     # 공간 구간
    t0, tL = 0.0, 1.0     # 시간 구간

    dx = (xL - x0) / (n + 1)
    dt = (tL - t0) / (m + 1)

    a2 = 1.0
    r = a2 * dt / dx**2   # 안정성 계수

    # --------------------------------------------------------------
    # 계수 행렬 A, B
    # param = 0 : Explicit
    # param = 1 : Implicit
    # param = 3 : Crank–Nicholson
    # --------------------------------------------------------------
    A = np.zeros((n, n))
    B = np.zeros((n, n))

    for i in range(n):
        # 대각 성분
        A[i, i] = 1 + 2 * r * (1 if param == 1 else 0.5)
        B[i, i] = 1 - 2 * r * (0.5 if param == 3 else 0)

        # 하부 대각
        if i > 0:
            A[i, i - 1] = -r * (1 if param in [1, 3] else 0)
            B[i, i - 1] =  r * (0.5 if param == 3 else 0)

        # 상부 대각
        if i < n - 1:
            A[i, i + 1] = -r * (1 if param in [1, 3] else 0)
            B[i, i + 1] =  r * (0.5 if param == 3 else 0)

    # --------------------------------------------------------------
    # 격자점
    # --------------------------------------------------------------
    x = np.linspace(x0, xL, n + 2)
    t = np.linspace(t0, tL, m + 2)

    # --------------------------------------------------------------
    # 초기 조건 및 경계 조건
    # --------------------------------------------------------------
    BC_L = lambda x, t: 0.0
    BC_R = lambda x, t: 0.0
    IC   = lambda x, t: np.sin(np.pi * x)

    # 초기 벡터
    b = np.zeros((n, 1))
    for j in range(n):
        b[j, 0] = IC(x[j + 1], t[0])

    # --------------------------------------------------------------
    # 시간 적분
    # --------------------------------------------------------------
    bnew = b.copy()
    results = []

    results.append(
        np.concatenate(([BC_L(x[0], t[0])],
                        b.flatten(),
                        [BC_R(x[-1], t[0])]))
    )

    for j in range(1, m + 2):

        if param == 0:          # Explicit
            bnew = B @ bnew
        elif param == 1:        # Implicit
            bnew = np.linalg.solve(A, bnew)
        elif param == 3:        # Crank–Nicholson
            bnew = np.linalg.solve(A, B @ bnew)
        else:
            raise ValueError("param은 0(Explicit), 1(Implicit), 3(C-N) 중 하나여야 한다.")

        col = bnew.flatten()
        results.appen
