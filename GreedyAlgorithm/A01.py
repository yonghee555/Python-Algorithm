# 모험가 길드

N = int(input())
f = list(map(int, input().split()))
f.sort()

answer = 0
count = 0
for i in f:
    count += 1
    if i <= count:
        answer += 1
        count = 0
print(answer)