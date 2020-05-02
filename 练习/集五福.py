s = input()
s_list = s.split(',')
res = [0] * 5
for p in s_list:
    for i, v in enumerate(p):
        res[i] += int(v)

print(min(res))

