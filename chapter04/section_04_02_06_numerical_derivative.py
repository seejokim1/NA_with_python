"""
(4.2.6) 수치미분 코드 구현
Numerical Analysis with Python

교재 본문 예제 코드
"""
import numpy as np
import matplotlib.pyplot as plt

# 수치미분 함수
def numerical_derivative(f, x, h=1e-5, method='central'):
    if method == 'forward':
        return (f(x + h) - f(x)) / h
    elif method == 'backward':
        return (f(x) - f(x - h)) / h
    elif method == 'central':
        return (f(x + h) - f(x - h)) / (2 * h)
    elif method == 'richardson':
        # Richardson 외삽법
        central_h = (f(x + h) - f(x - h)) / (2 * h)
        central_h2 = (f(x + h / 2) - f(x - h / 2)) / h
        return (4 * central_h2 - central_h) / 3
    else:
        raise ValueError("Invalid method. Choose 'forward', 'backward', 'central', or 'richardson'.")

h=0.1

# 3차 함수 및 도함수 정의
f = lambda x: x**3 - 6*x**2 + 11*x - 6  # 3차 함수
f_prime = lambda x: 3*x**2 - 12*x + 11  # 실제 도함수

# 계산 지점
x_vals = np.linspace(0, 4, 20)  # Discrete points in [0, 4]

# 수치 미분 값 계산
forward_values = np.array([numerical_derivative(f, x, h, 'forward') for x in x_vals])
backward_values = np.array([numerical_derivative(f, x, h, 'backward') for x in x_vals])
central_values = np.array([numerical_derivative(f, x, h, 'central') for x in x_vals])
richardson_values = np.array([numerical_derivative(f, x, h, 'richardson') for x in x_vals])
exact_values = np.array([f_prime(x) for x in x_vals])

# 에러 계산
forward_errors = np.abs(forward_values - exact_values)
backward_errors = np.abs(backward_values - exact_values)
central_errors = np.abs(central_values - exact_values)
richardson_errors = np.abs(richardson_values - exact_values)

# 그래프 시각화
plt.figure(figsize=(10, 6))
plt.scatter(x_vals, exact_values, label='Exact Derivative', color='black', marker='o', s=50, zorder=5)
plt.step(x_vals, forward_values, label='Forward Difference', where='mid', linestyle='-', alpha=0.7)
plt.step(x_vals, backward_values, label='Backward Difference', where='mid', linestyle='-', alpha=0.7)
plt.step(x_vals, central_values, label='Central Difference', where='mid', linestyle='-', alpha=0.7)
plt.step(x_vals, richardson_values, label='Richardson Extrapolation', where='mid', linestyle='-', alpha=0.7)

# 그래프 설정
plt.title('Discrete Derivative Approximations for a Cubic Function', fontsize=14)
plt.xlabel('x', fontsize=12)
plt.ylabel('Derivative Value', fontsize=12)
plt.legend()
plt.grid(True)
plt.show()

# 에러 시각화
plt.figure(figsize=(10, 6))
plt.plot(x_vals, forward_errors, label='Forward Difference Error', linestyle='--', marker='o')
plt.plot(x_vals, backward_errors, label='Backward Difference Error', linestyle='--', marker='o')
plt.plot(x_vals, central_errors, label='Central Difference Error', linestyle='--', marker='o')
plt.plot(x_vals, richardson_errors, label='Richardson Extrapolation Error', linestyle='--', marker='o')

# 그래프 설정
plt.title('Errors of Numerical Derivative Methods', fontsize=14)
plt.xlabel('x', fontsize=12)
plt.ylabel('Error', fontsize=12)
plt.legend()
plt.grid(True)
plt.show()
