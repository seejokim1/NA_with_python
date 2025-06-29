while len(A[-1]) < cols:  
            A[-1].append(0.0)  # 행에 0.0 추가
    return A  # 생성된 2차원 배열 반환
# 두 행렬의 곱을 계산하는 함수 정의
def AmultiB(A, B):
    rowsA = len(A)  # A 행렬의 행 개수
    colsA = len(A[0])  # A 행렬의 열 개수
    rowsB = len(B)  # B 행렬의 행 개수
    colsB = len(B[0])  # B 행렬의 열 개수
    # 행렬 곱이 가능한지 확인 (A의 열 개수 == B의 행 개수)
    if colsA != rowsB:
        # 조건이 맞지 않으면 예외 발생
        raise ArithmeticError('colsA != rowsB')  
    # 결과 행렬 초기화
    
    # 결과 행렬의 크기는 rowsA x colsB
    AmultiB = A_0(rowsA, colsB)  
    # 행렬 곱 계산
    for i in range(rowsA):  # A의 행 반복
        for j in range(colsB):  # B의 열 반복
            sum = 0  # 곱셈과 덧셈의 결과를 저장할 변수
            
            # A의 열과 B의 행 반복
            for ii in range(colsA): 
                # A의 i행과 B의 j열의 곱을 누적
                sum = sum + A[i][ii] * B[ii][j] 
                
            # 결과 행렬의 (i, j) 위치에 저장
            AmultiB[i][j] = sum  
    return AmultiB  # 결과 행렬 반환
# 행렬 선언