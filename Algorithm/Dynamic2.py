import sys

n = int(sys.stdin.readline())
k_list = list(map(int, sys.stdin.readline().split()))

d = [0] * n

d[0] = k_list[0]
if k_list[0] > k_list[1]:
    d[1] = k_list[0]
else:
    d[1] = k_list[1]

for i in range(2, n):
    if d[i-1] > k_list[i]+d[i-2]:
        d[i] = d[i-1]
    else:
        d[i] = k_list[i]+d[i-2]

print(d)
print(d[-1])
