# 7     컴퓨터의 수
# 6     경로의 수
# 1 2                   0 []
# 2 3                   1 [2, 5]
# 1 5                   2 [3, 5]
# 5 2                   3 [2]
# 5 6                   4 [7]
# 4 7                   5 [2, 6]
#                       6 [5]
#                       7 [4]

import sys


def DFS(graph_list_t, dfs_list_t, start = 1):
    for i in graph_list_t[start]:
        if not(i in dfs_list_t):
            dfs_list_t.append(i)
            # print(dfs_list_t)
            DFS(graph_list_t, dfs_list_t, i)

num_computer = int(sys.stdin.readline())
num_linked = int(sys.stdin.readline())

graph_list = []
dfs_list = []

for i in range(num_computer+1):
    graph_list.append([])

for i in range(num_linked):
    temp_list = list(map(int, sys.stdin.readline().split()))
    if temp_list[0] != 1:
        graph_list[temp_list[1]].append(temp_list[0])
    if temp_list[1] != 1:
        graph_list[temp_list[0]].append((temp_list[1]))

# print(graph_list)

DFS(graph_list, dfs_list)

print(len(dfs_list))