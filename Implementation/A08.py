# 문자열 재정렬

S = input().rstrip()
strs = []
nums = 0
for s in S:
    if s >= '0' and s <= '9':
        nums += int(s)
    else:
        strs.append(s)

strs.sort()
if nums > 0:
    strs.append(str(nums))
print(''.join(strs))