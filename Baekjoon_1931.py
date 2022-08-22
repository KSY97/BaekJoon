import sys                            # stdin.readline()을 사용하기 위한 임포트

meet_num = int(sys.stdin.readline())  # 총 회의의 개수를 meet_num에 넣음
meet_time = []                        # 입력받은 회의의 시작시간과 끝시간을 넣을 리스트

for i in range(0, meet_num):          # 회의의 수만큼 회의 시간을 입력받음
    meet_time.append(list(map(int, sys.stdin.readline().split())))
meet_time.sort()                      # 각 회의 시간 의 시작시간을 오름차순으로 정렬
meet_time.sort(key = lambda x:x[1])   # 정렬한 각 회의 시간의 끝시간을 오름차순으로 정렬
meet_max = 1                          # meet_max는 최대 가능한 회의의 개수
                                      # 첫 회의 시간을 기준으로 뒤의 회의 시간을 비교하기위해
                                      # 1로 초기화(첫 회의는 빼고 반복문 비교 계산하기 때문)
meet_value = meet_time[0][1]          # 무엇을 기준으로 비교건지 기준이 될 회의를 정해줌(정렬했을때 첫 회의)

for x in range(1, meet_num):               # [0] 회의(첫 회의)는 제외하고 반복문
    if meet_time[x][0] >= meet_value:      # 기준이 되는 회의의 끝나는 시간과 비교할 회의의 시작시간을
                                           # 비교해서 서로 겹치지 않는다면
        meet_max += 1                      # 회의 갯수 추가
        meet_value = meet_time[x][1]       # 기준 회의를 비교한 회의로 전환
print(meet_max)                       # 총 회의의 갯수 출력





# [0, 6], [1, 4], [2, 13], [3, 5], [3, 8], [5, 7], [5, 9], [6, 10], [8, 11], [8, 12], [12, 14]
#  7       4       12       3       6       3       5       5        4        5        3
#          v                                v                        v                 v
