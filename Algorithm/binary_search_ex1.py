#                15
# 20
# ===============||=====  5
# 14             ||
# ============== ||
# 10             ||
# ==========     ||
# 17             ||
# ===============||==    2

def find_point(list_f):
    end = max(list_f)
    start = 1

    return start, end


def binary_search(list_f, start, end, m):
    middle = (start + end) // 2
    print('middle = ', middle)
    result = 0

    for i in list_f:
        if i - middle > 0:
            result += (i - middle)

    # print('result = ', result)
    if start > end:
        return middle
    elif result == m:
        return middle
    elif result > m:
        # print('>')
        # print('middle+1 = ', middle+1)
        return binary_search(list_f, middle+1, end, m)
    else:
        # print('<')
        # print('middle-1 = ', middle - 1)
        return binary_search(list_f, start, middle-1, m)

import sys
n, m = map(int, sys.stdin.readline().split())
rice_cake_list = list(map(int, sys.stdin.readline().split()))

start, end = find_point(rice_cake_list)
result = binary_search(rice_cake_list, start, end, m)

print(result)