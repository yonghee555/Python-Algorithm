# 시각
n = int(input())

result = 0
for i in range(n + 1):
    if i == 3 or i == 13 or i == 23:
        result += 60 * 60
    else:
        result += 45 * 15 + 15 * 60

print(result)
