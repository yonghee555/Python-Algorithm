# 퇴사
# https://www.acmicpc.net/problem/14501

N = int(input())
T = []
P = []
dp = [0] * (N + 1)
for _ in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

for i in range(N):
    # 전날까지의 최대 금액이 더 크다면 업데이트
    dp[i] = max(dp[i - 1], dp[i])
    # 상담이 기간 안에 끝나는지 확인
    if i + T[i] > N:
        continue
    else:
        dp[i + T[i]] = max(dp[i + T[i]], dp[i] + P[i])

print(max(dp))