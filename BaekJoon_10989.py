import sys

n = int(sys.stdin.readline())
temp_cnt = [0]*(10001)
for _ in range(n):
    temp_cnt[int(sys.stdin.readline())] += 1

for i in range(len(temp_cnt)):
    # print('i = ', i)
    # print('temp_cnt[i] = ', temp_cnt[i])
    for _ in range(temp_cnt[i]):
        print(i)