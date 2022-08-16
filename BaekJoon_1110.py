input_first = int(input())
input_value = input_first
input_list = [int(i) for i in str(input_first)]
new_num = -1
sum_list = [input_list[0]]
sum_value = 0
count = 0
# input_list = [2, 6]
while new_num != input_value:
    # print('before sum_list = ', sum_list)
    # print('before input_list = ', input_list)
    if len(input_list) == 1:
        input_list.append(input_list[-1])
        input_list[0] = 0
        # print(input_list)
    sum_value = input_list[0] + input_list[-1]       # 초기값은 input_list[0]이 어야하고,
    sum_list = [int(j) for j in str(sum_value)]     #이후는 input_list[1]이 어야함
    input_list = [input_list[-1], sum_list[-1]] #input_list의 값을 저장하는 것과 동시에
    new_num = (input_list[0]*10) + (input_list[-1])
    count += 1
    # print('after sum_list = ', sum_list)
    # print('after input_list = ', input_list)
    # print(new_num)
    # print('===================')

print(count)

# sum_value =  8
# sum_list =  [8]
# [2, 6]
# sum_value =  14
# sum_list =  [1, 4]
# [2, 6]
# sum_value =  10
# sum_list =  [1, 0]
# [2, 6]