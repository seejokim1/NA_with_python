for score in scores:
    if score >= 90:
        grades.append('A')
    elif score >= 80:
        grades.append('B')
    elif score >= 70:
        grades.append('C')
    else:
        grades.append('D')
print("점수:", scores)
print("등급:", grades)