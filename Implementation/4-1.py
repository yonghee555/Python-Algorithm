# 상하좌우

n = int(input())
plans = input().split()

x, y = 1, 1
move = {'L':(0, -1), 'R':(0, 1), 'U':(-1, 0), 'D':(1, 0)}

for p in plans:
    move_x, move_y = move[p][0], move[p][1]
    if move_x:
        tmp = x + move_x
        if tmp > 0 and tmp <= n:
            x = tmp
    else:
        tmp = y + move_y
        if tmp > 0 and tmp <= n:
            y = tmp

print(x, y)