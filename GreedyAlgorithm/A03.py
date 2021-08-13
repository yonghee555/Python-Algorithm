# 문자열 뒤집기
# https://www.acmicpc.net/problem/1439

S = input()
answer = [0, 0]
now = S[0]
answer[int(now)] += 1
for s in S:
    if s != now:
        answer[int(s)] += 1
        now = s
print(min(answer))