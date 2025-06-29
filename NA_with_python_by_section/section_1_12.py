def __init__(self, func, d_func):
        self.func = func        # 함수
        self.d_func = d_func    # 함수의 미분
    def evaluate(self, x):
        """함수 값을 계산"""
        return self.func(x)
    def derivative(self, x):
        """미분 값을 계산"""
        return self.d_func(x)
    def visualize(self, x_range):
        """함수와 미분의 그래프를 가시화"""
        x = np.linspace(x_range[0], x_range[1], 500)
        y = self.evaluate(x)
        y_prime = self.derivative(x)
        plt.figure(figsize=(10, 6))
        plt.plot(x, y, label='f(x)', linewidth=2)
        plt.plot(x, y_prime, label="f'(x)", linestyle='--', linewidth=2)
        plt.axhline(0, color='black', linestyle='-', linewidth=0.8)
        plt.title('Function and its Derivative')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.legend()
        plt.grid(True)
        plt.show()
# 함수와 미분 정의