# 연산자 끼워넣기
# https://www.acmicpc.net/problem/14888

max_result = int(-1e9)
min_result = int(1e9)

N = int(input())
A = list(map(int, input().split()))
op = list(map(int, input().split()))

def dfs(i, result, sum, sub, mul, div):
    if i == N:
        global max_result, min_result
        max_result, min_result = max(max_result, result), min(min_result, result)
        return
    if sum > 0:
        dfs(i + 1, result + A[i], sum - 1, sub, mul, div)
    if sub > 0:
        dfs(i + 1, result - A[i], sum, sub - 1, mul, div)
    if mul > 0:
        dfs(i + 1, result * A[i], sum, sub, mul - 1, div)
    if div > 0:
        dfs(i + 1, int(result / A[i]), sum, sub, mul, div - 1)

dfs(1, A[0], op[0], op[1], op[2], op[3])
print(max_result)
print(min_result)