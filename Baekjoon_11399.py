# [3, 1, 4, 3, 2]
# [1, 2, 3, 4, 5]
# [3, 4, 8, 11, 13] == 39

# [1, 2, 3, 3, 4]
# [2, 5, 1, 4, 3]
# [1, 3, 6, 9, 13] == 32

import sys

sys.stdin.readline()                                         # 사람의 수를 입력 받음
people_time = list(map(int, sys.stdin.readline().split()))   # 입력 받은 시간을 리스트 형태로 받음

people_time.sort()                   # 오름차순으로 정렬
time_sum = 0                         # 각 사람이 시간이 얼마나 걸리는지 계산
value_sum = 0                        # 걸리는 시간의 총합
time_sum_list = []                   # 각 사람이 얼마나 걸리는지 계산 한 값을 넣을 리스트

for x in people_time:                # 인원수만큼 반복
    time_sum += x                    # 각 사람이 시간이 얼마나 걸리는지 계산
    time_sum_list.append(time_sum)   # 각 사람이 시간이 얼마나 걸리는지 계산한 값을 리스트에 추가

for y in time_sum_list:              # 리스트에 추가한 계산값을 불러와서
    value_sum += y                   # 모두 더한 값

print(value_sum)                     # 걸리는 시간의 총합 출력
