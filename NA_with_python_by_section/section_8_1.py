① 코드 
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
# 첫 번째 함수 정의: 원 (circle) f(x, y) = x^2 + y^2 - 4
def myCirc(x, y):
    return x**2 + y**2 - 4
# 두 번째 함수 정의: 쌍곡선 (hyperbolic) g(x, y) = y - 2x - 1
def myHyp(x, y):
    return y - 2*x - 1
# 3D 그래프 생성