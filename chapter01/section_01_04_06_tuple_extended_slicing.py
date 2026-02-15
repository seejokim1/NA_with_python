# ==========================================================
# section_01_06_tuple_extended_slicing.py
# Chapter 1 - Tuple Extended Slicing
# ==========================================================

# 튜플 정의
T = (0, 1, 2, 3, 4, 5, 6)

print("Original tuple:", T)

# 1️⃣ 전체 복사
T_copy = T[:]
print("T_copy:", T_copy)

# 2️⃣ 부분 슬라이싱
T_slice_1 = T[1:4]        # index 1 ~ 3
print("T[1:4]:", T_slice_1)

T_slice_2 = T[:3]         # 처음부터 index 2까지
print("T[:3]:", T_slice_2)

T_slice_3 = T[3:]         # index 3부터 끝까지
print("T[3:]:", T_slice_3)

# 3️⃣ step 사용
T_step = T[::2]           # 2칸 간격
print("T[::2]:", T_step)

# 4️⃣ 역순 추출
T_reverse = T[::-1]
print("T[::-1]:", T_reverse)

# 5️⃣ 음수 인덱스 활용
T_negative = T[-4:-1]
print("T[-4:-1]:", T_negative)
