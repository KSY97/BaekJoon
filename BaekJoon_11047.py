input_coin = input().split()  # 입력한 숫자를 분할해 input_coin에 리스트형태로 넣음
coin_num = int(input_coin[0])  # 입력한 숫자중 앞부분을 코인의 총 갯수(coin_num)
coin_sum = int(input_coin[1])  # 입력한 숫자중 뒷부분을 코인의 합(coin_sum)으로 넣음
coin_list = []  # 코인의 값을 넣을 리스트 형태의 변수
coin_min = 0  # 코인의 합을 얻기위한 동전의 최소 개수

for i in range(0, coin_num):  # 코인의 값을 coin_list에 넣음
    coin_list.append(int(input()))

coin_list.sort(reverse=True)  # coin_list에 넣은 값들을 내림차순으로 정렬

for i in range(0, coin_num):  # coin_list의 값들을 큰 순서대로 불러옴
    if coin_list[i] <= coin_sum:  # coin_list의 값이 coin_sum보다 크면 그 값은 무시
        coin_min += (coin_sum // coin_list[i])  # 그렇지 않다면 해당 값으로 coin_sum에 몇번 넣을수있는지
        # 계산 후 coin_min에 추가
        coin_sum %= coin_list[i]  # 그리고 나머지 값을 coin_sum에 넣음
        if (coin_sum % coin_list[i]) != 0:  # coin_sum이 0이 될때까지 진행
            continue
        else:
            break

print(coin_min)  # 최소 개수 출력