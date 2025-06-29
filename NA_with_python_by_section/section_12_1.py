def stiffness_matrix(n, h, k):
    K = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i == j:
                K[i, j] = 2 * k / h  # 대각선 요소
            elif abs(i - j) == 1:
                K[i, j] = -k / h  # 인접 요소
    return K
# FEM 외부 힘 벡터 계산 함수
def force_vector(n, h):
    F = np.zeros(n)
    for i in range(n):
        x_i = i * h  # 노드 위치
        F[i] = ode.function_f(x_i)* h  # 외부 힘 계산
        #F[i] = f(x_i) * h  # 외부 힘 계산
    return F
# 이론해 함수
def corrected_analytical_solution(x):
    return np.exp(x)
# 입력 데이터