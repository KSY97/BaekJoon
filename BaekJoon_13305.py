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
# [5, 2, 4, 1]

for i in range(input_num-1):
    if val == 0:
        val = input_val[i]

    if val > input_val[i]:
        val = input_val[i]

    add_dis += input_dis[i]
    add_val = val * add_dis
    all_val += add_val
    add_dis = 0
    add_val = 0

    # if input_val[i] > input_val[i+1]:
    #     add_dis += input_dis[i]
    #     add_val = val * add_dis
    #     all_val += add_val
    #     add_dis = 0
    #     add_val = 0
    #
    #     print(all_val)
    # else:
    #     add_dis += input_dis[i]
    #     add_val = val * add_dis
    #     all_val += add_val
    #     add_dis = 0
    #     add_val = 0



print(all_val)