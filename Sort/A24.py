# 안테나
# https://www.acmicpc.net/problem/18310

import sys
input = sys.stdin.readline

N = int(input())
house = list(map(int, input().split()))
house.sort()
print(house[(N - 1) // 2])