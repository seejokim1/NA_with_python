# Forward Euler 반복
for n in range(n_steps - 1):
    x[n + 1] = x[n] + dx
    y[:, n + 1] = (np.eye(2) + dx * A_) @ y[:, n]
# y(x) 그래프 그리기