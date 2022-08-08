import sys

input_num = int(sys.stdin.readline())
input_dis = list(map(int, sys.stdin.readline().split()))
input_val = list(map(int, sys.stdin.readline().split()))

dis = 0
add_dis = 0
val = input_val[0]
add_val = 0
all_val = 0

# [2, 3, 1]
# [5, 6, 7, 1]

for i in range(input_num-1):
    if input_val[i] > input_val[i+1]:
        add_dis += input_dis[i]
        add_val = input_val[i] * add_dis
        add_dis = 0
    else:
        add_dis += input_dis[i]
    if val > input_val[i]:
        val = input_val[i]