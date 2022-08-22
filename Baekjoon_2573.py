# [0, 0, 0, 0, 0, 0, 0]     [True,  True,   True,   True,   True,   True,   True]
# [0, 2, 4, 5, 3, 0, 0]     [True,  False,  False,  False,  False,  True,   True]
# [0, 3, 0, 2, 5, 2, 0]     [True,  False,  True,   False,  False,  False,  True]
# [0, 7, 6, 2, 4, 0, 0]     [True,  False,  False,  False,  False,  True,   True]
# [0, 0, 0, 0, 0, 0, 0]     [True,  True,   True,   True,   True,   True,   True]
import sys
from collections import deque


def find_startpoint(iceberg_check_f, row_f, col_f):
    start_row, start_col = 0, 0
    check = False
    for i in range(row_f):
        for j in range(col_f):
            if not(iceberg_check_f[i][j]):
                start_row, start_col = i, j
                check = True
                break

        if check:
            break

    return start_row, start_col


# def dfs(iceberg_check_f, start_row, start_col, row_f, col_f):
#     n, m = start_row, start_col
#     iceberg_check_f[n][m] = True
#
#     if m+1 < col_f:
#         # print('m+1 = ', m + 1)
#         if not (iceberg_check_f[n][m+1]):
#             dfs(iceberg_check_f, n, m+1, row_f, col_f)
#
#     if m-1 >= 0:
#         # print('m-1 = ', m - 1)
#         if not (iceberg_check_f[n][m-1]):
#             dfs(iceberg_check_f, n, m-1, row_f, col_f)
#
#     if n+1 < row_f:
#         # print('n+1 = ', n + 1)
#         if not (iceberg_check_f[n+1][m]):
#             dfs(iceberg_check_f, n+1, m, row_f, col_f)
#
#     if n-1 >= 0:
#         # print('n-1 = ', n - 1)
#         if not (iceberg_check_f[n-1][m]):
#             dfs(iceberg_check_f, n-1, m, row_f, col_f)


def bfs(iceberg_check_f, start_row, start_col, row_f, col_f, x_f, y_f):
    n, m = start_row, start_col
    y_f.append(n)
    x_f.append(m)

    while x_f and y_f:
        n = y_f.popleft()
        m = x_f.popleft()
        if not iceberg_check_f[n][m]:
            iceberg_check_f[n][m] = True
            if n-1 >= 0:
                if not iceberg_check_f[n-1][m]:
                    y_f.append(n - 1)
                    x_f.append(m)
            if m+1 < col_f:
                if not iceberg_check_f[n][m+1]:
                    y_f.append(n)
                    x_f.append(m + 1)
            if n+1 < row_f:
                if not iceberg_check_f[n+1][m]:
                    y_f.append(n + 1)
                    x_f.append(m)
            if m-1 >= 0:
                if not iceberg_check_f[n][m-1]:
                    y_f.append(n)
                    x_f.append(m - 1)


def after_one_year(iceberg_list_f, iceberg_origin_f, iceberg_check_f, row_f, col_f):
    for n in range(row_f):
        for m in range(col_f):
            # print('1')
            if not (iceberg_check_f[n][m]):
                # print('2')
                if iceberg_origin_f[n][m] != 0:
                    # print('11')
                    if n-1 >= 0:
                        # print('22')
                        if iceberg_origin_f[n-1][m] == 0:
                            # print('33')
                            if iceberg_list_f[n][m] > 0:
                                iceberg_list_f[n][m] -= 1
                                # print('3')

                    if n+1 < row_f:
                        if iceberg_origin_f[n+1][m] == 0:
                            if iceberg_list_f[n][m] > 0:
                                iceberg_list_f[n][m] -= 1
                                # print('4')
                    if m-1 >= 0:
                        if iceberg_origin_f[n][m-1] == 0:
                            if iceberg_list_f[n][m] > 0:
                                iceberg_list_f[n][m] -= 1
                                # print('5')

                    if m+1 < col_f:
                        if iceberg_origin_f[n][m+1] == 0:
                            if iceberg_list_f[n][m] > 0:
                                iceberg_list_f[n][m] -= 1
                                # print('6')


def make_check_list(iceberg_list_f, row_f, col_f):
    iceberg_check_f = []
    for n in range(row_f):
        iceberg_check_f.append([])
        for m in range(col_f):
            if iceberg_list_f[n][m] == 0:
                iceberg_check_f[n].append(True)
            else:
                iceberg_check_f[n].append(False)

    return iceberg_check_f


def check_true(iceberg_check_f):
    for i in iceberg_check_f:
        for j in i:
            if not j:
                return False
    return True


def check_zero(iceberg_list_f):
    for i in iceberg_list_f:
        for j in i:
            if j > 0:
                return False
    return True


def deep_copy(iceberg_list_f, iceberg_origin_f, row_f, col_f):
    for n in range(row_f):
        for m in range(col_f):
            iceberg_origin_f[n][m] = iceberg_list_f[n][m]


input_shape = list(map(int, sys.stdin.readline().split()))
row = input_shape[0]
column = input_shape[1]

iceberg_list = []
iceberg_origin = []
iceberg_check_origin = []
x = deque([])
y = deque([])
years_cnt = 0

for i in range(row):
    iceberg_list.append([])
    iceberg_origin.append([])
    iceberg_check_origin.append([])
    temp_list = map(int, sys.stdin.readline().split())
    for j in temp_list:
        iceberg_list[i].append(j)
        iceberg_origin[i].append(j)
        iceberg_check_origin[i].append(j)


while True:
    bfs_cnt = 0
    deep_copy(iceberg_list, iceberg_origin, row, column)
    iceberg_check = make_check_list(iceberg_list, row, column)
    deep_copy(iceberg_check, iceberg_check_origin, row, column)
    start_n, start_m = find_startpoint(iceberg_check, row, column)
    while True:
        bfs(iceberg_check, start_n, start_m, row, column, x, y)
        if not check_true(iceberg_check):
            start_n, start_m = find_startpoint(iceberg_check, row, column)
            bfs_cnt += 1
        else:
            bfs_cnt += 1
            break

    if bfs_cnt < 2:
        after_one_year(iceberg_list, iceberg_origin, iceberg_check_origin, row, column)
        years_cnt += 1
        iceberg_check = make_check_list(iceberg_list, row, column)
        if check_zero(iceberg_list):
            years_cnt = 0
            break
    else:
        break

print(years_cnt)
