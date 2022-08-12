# [노드 수, 경로 수, 시작 노드]
# 4 5 1                             0 [[]
# 1 2                               1 [2, 3, 4]
# 1 3                               2 [4]
# 1 4                               3 [4]
# 2 4                               4 [2, 3]]
# 3 4                               노드 : 1, 2, 3, 4
# 노드 4개 경로 5개

def BFS_way(list_a, start_w , list_BFS, check_BFS):
    # print(list_BFS)
    for i in list_a[start_w]:
        print(i)
        if not(i in list_BFS):
            list_BFS.append(i)
            check_BFS.append(i)

    while len(check_BFS) != 0:
        print(check_BFS)
        for j in list_a[check_BFS.pop(0)]:
            if not (j in list_BFS):
                list_BFS.append(j)
                check_BFS.append(j)
                print(list_BFS)
                print(check_BFS)


    # for j in list_a[start_w]:
    #     if not(j in check_BFS):
    #         print('here')
            # BFS_way(list_a, j, list_BFS, check_BFS)

    # if len(list_BFS) != num_node_w-1 :
    #     for j in range(len(list_a[start_w])):
    #         if not (list_a[list_a[start_w][j]] in list_BFS):
    #             BFS_way(list_a, list_a[start_w][j], num_node_w, list_BFS)


import sys

info = list(map(int, sys.stdin.readline().split()))
num_node = info[0]
num_way = info[1]
start = info[2]
stack_list = []
BFS_list = []
check_list=[]
for i in range(num_node+1):
    stack_list.append([])

for i in range(num_way):
    n = list(map(int, sys.stdin.readline().split()))
    if n[1] == start:
        if n[0] == start:
            continue
        stack_list[n[1]].append(n[0])
        stack_list[n[1]].sort()
        continue

    stack_list[n[0]].append(n[1])
    stack_list[n[0]].sort()
    if n[0] == start:
        continue
    stack_list[n[1]].append(n[0])
    stack_list[n[1]].sort()

print(stack_list)

# BSF
# BFS_list.append(start)
#
#
# if len(BFS_list) != num_node:
#     BFS_list.append(stack_list[BFS_list[start]][i])
#
# print(BFS_list)
BFS_way(stack_list, start, BFS_list, check_list)

print(BFS_list)
print(check_list)
# 6 5 1
# 1 2
# 1 4
# 2 3
# 3 6
# 4 5
