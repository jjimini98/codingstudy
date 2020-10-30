# 2839 설탕배달

# //는 몫 % 나머지

number = int(input())

if number < 5:
    print(number - 5)

elif number % 3 == 0:
    if number <= 10:
        print(number // 3)
    else:
        five = number % 5
        three = number % 3
        print(five + three)

elif number % 5 == 0:
    print(number // 5)

else:
    five = number % 5
    three = number % 3
    print(five + three)

# 2839 설탕배달 version 2

total = int(input())
if total < 5:
    print(-1)
else:
    f_share = total // 5
    f_rest = total % 5

    if f_rest >= 3:
        t_share = f_rest // 3
        t_rest = f_rest % 3
        print(f_share + t_share + t_rest)

    else:
        print(f_share + 1)

# 2292 벌집

a = int(input())
list = [1]
n = 6
standard = 1

while n < 1000000:
    standard = standard + n
    list.append(standard)
    n = n + 6

for x in list:
    if a <= x:
        print(list.index(x) + 1)
        break

    else:
        continue


#2869 달팽이는 올라가고 싶다

import math
a,b,v = map(int, input().split())

total = math.ceil((v-a)/(a-b)) + 1
print(total)

