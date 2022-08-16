# 4 6
# 101111
# 101010
# 101011
# 111011
# [[1, 0, 1, 1, 1, 1],
#  [1, 0, 1, 0, 1, 0],
#  [1, 0, 1, 0, 1, 1],
#  [1, 1, 1, 0, 1, 1]]
import sys

input_dim = list(map(int, sys.stdin.readline().split()))
N = input_dim[0]
M = input_dim[1]
maze_list = []

# 빈 리스트 생성
for i in range(N):
    maze_list.append([])

for i in range(0, N):
    input_maze = str(sys.stdin.readline().strip())
    # print(i)
    for j in input_maze:
        a = int(j)
        maze_list[i].append(a)
        # print(a)

# 컬럼 설정
# for i in range(M):
#     maze_list[0].append(i)

# print(maze_list)
list_n = [0]
list_m = [0]
while maze_list[N-1][M-1] == 1:

    if len(list_n) != 0:
        n = list_n.pop(0)
        # print('n = ', n)
    if len(list_m) != 0:
        m = list_m.pop(0)
        # print('m = ', m)

    if m-1 >= 0:
        if maze_list[n][m-1] == 1:
            maze_list[n][m-1] += maze_list[n][m]
            # print('maze_list[n][m-1] = ', maze_list[n][m-1])
            list_n.append(n)
            list_m.append(m-1)
    if n-1 >= 0:
        if maze_list[n-1][m] == 1:
            maze_list[n-1][m] += maze_list[n][m]
            # print('maze_list[n-1][m] = ', maze_list[n-1][m])
            list_n.append(n-1)
            list_m.append(m)

    if m+1 < M:
        if maze_list[n][m+1] == 1:
            maze_list[n][m+1] += maze_list[n][m]
            # print('maze_list[n][m+1] = ', maze_list[n][m+1])
            list_n.append(n)
            list_m.append(m+1)
    if n+1 < N:
        if maze_list[n+1][m] == 1:
            maze_list[n+1][m] += maze_list[n][m]
            # print('maze_list[n+1][m] = ', maze_list[n+1][m])
            list_n.append(n+1)
            list_m.append(m)
#     print('list_n = ', list_n)
#     print('list_m = ', list_m)
#     print('maze_list[N-1][M-1] = ', maze_list[N-1][M-1])
#
# print(maze_list)
print(maze_list[N-1][M-1])