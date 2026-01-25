# =========================================================
# Section (1.13) matplotlib 그래프 시각화
# =========================================================

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("sin(x)")
plt.title("Sine Function")
plt.grid(True)
plt.show()
