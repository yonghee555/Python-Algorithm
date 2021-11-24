# 편집 거리

str1 = input().rstrip()
str2 = input().rstrip()

l1, l2 = len(str1), len(str2)

dp = [[0] * (l2 + 1) for _ in range(l1 + 1)]

for i in range(l1 + 1):
    dp[i][0] = i
for i in range(l2 + 1):
    dp[0][i] = i

for i in range(1, l1 + 1):
    for j in range(1, l2 + 1):
        if str1[i - 1] == str2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1]
        else:
            dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1 

print(dp[l1][l2])