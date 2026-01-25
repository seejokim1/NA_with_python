# =========================================================
# Section (1.10) 함수(Function)
# =========================================================

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))
