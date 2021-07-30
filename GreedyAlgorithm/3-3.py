# 숫자 카드 게임

n, m = map(int, input().split())
answer = 0
for _ in range(n):
    numbers = map(int, input().split())
    answer = max(min(numbers), answer)

print(answer)