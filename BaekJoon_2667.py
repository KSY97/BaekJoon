import sys
from collections import deque


def bfs(start_row_f, start_col_f, shape_f):
    n, m = start_row_f, start_col_f
    cnt = 0
    row_deque.append(n)
    col_deque.append(m)
    while row_deque and col_deque:
        n = row_deque.popleft()
        m = col_deque.popleft()
        # print('1')
        # print(n,m)
        if not house_check[n][m]:
            # print('2')
            house_check[n][m] = True
            cnt += 1
            if n-1 >= 0:
                if not house_check[n-1][m]:
                    row_deque.append(n - 1)
                    col_deque.append(m)
            if n+1 < shape_f:
                if not house_check[n+1][m]:
                    row_deque.append(n + 1)
                    col_deque.append(m)
            if m-1 >= 0:
                if not house_check[n][m-1]:
                    row_deque.append(n)
                    col_deque.append(m - 1)
            if m+1 < shape_f:
                if not house_check[n][m+1]:
                    row_deque.append(n)
                    col_deque.append(m + 1)

    return cnt


def find_start(shape_f):
    for i in range(shape_f):
        for j in range(shape_f):
            if not house_check[i][j]:
                start_row_f, start_col_f = i, j
                # print(start_row_f, start_col_f)
                return start_row_f, start_col_f


def make_check(shape_f):
    for i in range(shape_f):
        for j in range(shape_f):
            if house_list[i][j] == 1:
                house_check[i][j] = False
            else:
                house_check[i][j] = True


def check_true(shape_f):
    for i in range(shape_f):
        for j in range(shape_f):
            if not house_check[i][j]:
                return False
    return True


input_shape = int(sys.stdin.readline())

house_list = []
house_check = []
result_list = []
row_deque = deque()
col_deque = deque()

for i in range(input_shape):
    input_house = list(str(sys.stdin.readline().strip()))
    house_list.append([])
    house_check.append([])
    for j in input_house:
        house_list[i].append(int(j))
        house_check[i].append(0)

make_check(input_shape)
bfs_cnt = 0
while True:
    start_row, start_col = find_start(input_shape)
    result_list.append(bfs(start_row, start_col, input_shape))
    bfs_cnt += 1
    if check_true(input_shape):
        break

result_list.sort()
print(bfs_cnt)
for x in result_list:
    print(x)