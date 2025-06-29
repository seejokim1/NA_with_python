import numpy as np
def sor_method(A, b, omega, tol=1e-10, max_iter=1000):
    """
    SOR(Successive Over-Relaxation) Method to solve Ax = b.
    Parameters:
    - A: Coefficient matrix
    - b: Constant vector
    - omega: Relaxation factor (ω)
    - tol: Tolerance for convergence
    - max_iter: Maximum number of iterations
    Returns:
    - x: Solution vector
    - iter_count: Number of iterations
    """
    n = len(b)
    x = np.zeros(n)  # Initial guess
    for iter_count in range(max_iter):
        x_old = x.copy()
        for i in range(n):
            sigma = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x[i] = (1 - omega) * x_old[i] + omega * (b[i] - sigma) / A[i][i]
        
        # Convergence check
        if np.linalg.norm(x - x_old, ord=np.inf) < tol:
            return x, iter_count + 1
    raise ValueError("SOR method did not converge")