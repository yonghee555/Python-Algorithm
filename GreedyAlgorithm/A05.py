# 볼링공 고르기

N, M = map(int, input().split())
weight = list(map(int, input().split()))
weight.sort()

answer = 0
for i in range(len(weight)):
    for j in range(i, len(weight)):
        if weight[i] != weight[j]:
            answer += 1
print(answer)