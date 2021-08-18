# 럭키 스트레이트
# https://www.acmicpc.net/problem/18406

N = list(map(int, input()))
mid = len(N) // 2
if sum(N[:mid]) == sum(N[mid:]):
    print("LUCKY")
else:
    print("READY")