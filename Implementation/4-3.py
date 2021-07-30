# 왕실의 나이트

n = input()
row, col = int(ord(n[0]) - 96), int(n[1])

moves = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
count = 0

for move in moves:
    row_next, col_next = move[0] + row, move[1] + col
    if row_next > 0 and row_next <= 8 and col_next > 0 and col_next <= 8:
        count += 1

print(count)