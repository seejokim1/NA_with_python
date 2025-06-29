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
        raise ValueError("Invalid method. Choose 'forward', 'backward', 'central', or