import sys
import re

input_formula = sys.stdin.readline()
num = list(map(int, re.split('[+,-]', input_formula)))
sign = re.findall('[+, -]',input_formula)

cnt1 = 0
cnt2 = 0
sub = 0
for x in sign:
    if x == '+':
        sum = num[cnt1] + num[cnt1+1]
        num.pop(cnt1)
        num[cnt1] = sum
        cnt1 -= 1

    cnt1 += 1

for y in num:
    if len(num) == 1:
        result = y
    else:
        if (sub == 0) & (cnt2 == 0):
            sub = y
        else:
            result = sub - y
            sub = result
    cnt2 += 1

print(result)
# [20, 30, 40 ,50]
#  0   1   2   3
# ['-', '+', '-']
#  0   1   2