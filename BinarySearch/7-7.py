# 부품 찾기
# set을 이용한 풀이

N = int(input())
components = set(map(int, input().split()))

M = int(input())
request = list(map(int, input().split()))

for i in request:
    print('yes' if i in components else 'no', end=' ')
print()