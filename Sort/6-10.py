# 위에서 아래로

array = []
n = int(input())
for _ in range(n):
    array.append(int(input()))

array.sort(reverse=True)
for i in array:
    print(i, end=' ')