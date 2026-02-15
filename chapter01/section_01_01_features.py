# =========================================================
# Chapter 1: 파이썬의 이해
# Section (1.1) 파이썬의 특징
# =========================================================

# ============================================
# 플랫폼 독립성 예제
# 파일 생성 후 읽기
# ============================================

# 1️⃣ 파일 생성 (쓰기 모드)
with open("example.txt", "w", encoding="utf-8") as file:
    file.write("Hello, Python!\n")
    file.write("This code works on Windows, macOS, and Linux.\n")

# 2️⃣ 파일 읽기 (읽기 모드)
with open("example.txt", "r", encoding="utf-8") as file:
    content = file.read()

# 3️⃣ 출력
print("파일 내용:")
print(content)

