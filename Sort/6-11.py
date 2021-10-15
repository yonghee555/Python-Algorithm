# 성적이 낮은 순서로 학생 출력하기

array = []

n = int(input())
for _ in range(n):
    name, grade = input().split()
    array.append((name, int(grade)))

array.sort(key=lambda x: x[1])

for student in array:
    print(student[0], end=' ')