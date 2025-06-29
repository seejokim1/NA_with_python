# NA_with_python
파이썬을 이용한 알기쉬운 수치해석 홍능출판
# NA_with_python (by section)
본 저장소는 각 섹션(예: 1.1, 2.2 등)에 해당하는 파이썬 실습 코드들을 모아둔 자료입니다.
아래는 각 파일에 대한 간단한 설명입니다.
| 파일명 | 설명 |
|--------|------|
| `section_10_1.py` | Forward Euler 반복 y(x) 그래프 그리기 |
| `section_10_2.py` | def blasius(eta, y): |
| `section_11_2.py` | 선 스타일 및 색상 설정 시각화 legend를 오른쪽에 배치 사용자 입력 |
| `section_12_1.py` | def stiffness_matrix(n, h, k): FEM 외부 힘 벡터 계산 함수 def force_vector(n, h): F[i] = f(x_i) * h  # 외부 힘 계 |
| `section_12_4.py` | 파이썬 수치해석 예제 코드 |
| `section_1_1.py` | def __init__(self, name): def speak(self): |
| `section_1_10.py` | f(x) 함수 정의 def f(x): f'(x) 도함수 정의 def fprime(x): 함수 출력 예제 |
| `section_1_11.py` | 두 행렬의 곱을 계산하는 함수 정의 def AmultiB(A, B): 행렬 곱이 가능한지 확인 (A의 열 개수 == B의 행 개수) 조건이 맞지 않으면 예외 발생 결과 행렬 초기화 |
| `section_1_12.py` | def __init__(self, func, d_func): def evaluate(self, x): def derivative(self, x): def visualize(self |
| `section_1_13.py` | 데이터 준비 |
| `section_1_2.py` | 파이썬 수치해석 예제 코드 |
| `section_1_5.py` | 파이썬 수치해석 예제 코드 |
| `section_1_6.py` | 성능 비교 Python 리스트 연산 |
| `section_1_7.py` | 함수 정의: 입력값 x를 제곱하여 반환하는 함수 f(x) def f(x): 반복문: range(0, 4)로 0부터 3까지 반복 |
| `section_1_8.py` | 파이썬 수치해석 예제 코드 |
| `section_1_9.py` | 행렬을 파일에 저장 |
| `section_2_2.py` | 결과 출력 |
| `section_2_3.py` | 결과 출력 |
| `section_2_4.py` | 함수와 도함수 정의 |
| `section_3_1.py` | 결과 출력 |
| `section_3_3.py` | 결과 출력 |
| `section_3_4.py` | def sor_method(A, b, omega, tol=1e-10, max_iter=1000): Convergence check |
| `section_4_1.py` | x 값 정의 및 원래 함수 y = exp(x) 계산 |
| `section_4_2.py` | 수치미분 함수 def numerical_derivative(f, x, h=1e-5, method='central'): Richardson 외삽법 |
| `section_5_1.py` | 우측 리만 합 시각화 |
| `section_5_2.py` | def y( x ): |
| `section_5_3.py` | def richardson_extrapolation(f, a, b, n1, n2): 두 개의 복합 사다리꼴 공식 값 계산 Richardson Extrapolation 공식 def  |
| `section_5_4.py` | 적분할 함수 정의 def func(x): Romberg 적분 설정 Romberg 적분 수행 정확한 적분값 계산 (f(x) = sin(x)의 해석적 적분) 절대 오차 계산 결과 출력 |
| `section_5_5.py` | 결과 출력 |
| `section_5_6.py` | def newton_poly(coef, x_data, x): Newton Interpolation coefficients |
| `section_6_3.py` | 데이터 포인트 (점 4개) |
| `section_6_4.py` | 데이터 포인트 (점 4개) |
| `section_6_5.py` | def newton_poly(coef, x_data, x): Newton Interpolation coefficients |
| `section_7_1.py` | 주어진 데이터 포인트 |
| `section_7_3.py` | y = -(theta0 + theta1*x + theta2*x^2 + noise) |
| `section_8_1.py` | 첫 번째 함수 정의: 원 (circle) f(x, y) = x^2 + y^2 - 4 def myCirc(x, y): 두 번째 함수 정의: 쌍곡선 (hyperbolic) g(x, y |
| `section_8_2.py` | 파이썬 수치해석 예제 코드 |
| `section_9_5.py` | 파이썬 수치해석 예제 코드 |
| `section_9_6.py` | 방정식 정의 def f(t, y, integral): Euler, RK2 및 RK4 선택적으로 사용 def solve_differential_integral(param): 적분항  |
| `section_9_7.py` | 파이썬 수치해석 예제 코드 |
