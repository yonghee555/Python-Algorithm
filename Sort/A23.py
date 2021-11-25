# 국영수
# https://www.acmicpc.net/problem/10825

import sys
input = sys.stdin.readline

students = []
N = int(input())
for _ in range(N):
    students.append(list(input().split()))
students.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))
for s in students:
    print(s[0])