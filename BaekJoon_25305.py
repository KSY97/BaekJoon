import sys
n, k = map(int, sys.stdin.readline().split())
grade_list = list(map(int, sys.stdin.readline().split()))
grade_list.sort(reverse=True)
print(grade_list[k-1])