#2581 소수

M = int(input())
N = int(input())


input_list = []

for x in range(M,N+1):
        input_list.append(x)
        print(input_list)
for t in input_list:
        if t%2==0:
          input_list.remove(t)
        elif t%3 ==0:
            input_list.remove(t)
        elif t % 5 == 0:
            input_list.remove(t)
        elif t % 7 == 0:
            input_list.remove(t)
        elif t % 11 == 0:
            input_list.remove(t)
        elif t % 13 == 0:
            input_list.remove(t)
        elif t % 17 == 0:
            input_list.remove(t)
        elif t % 19 == 0:
            input_list.remove(t)



sum = 0
for t in input_list:
    if len(input_list) == 0:
        print(-1)
    else:
        sum+=t
        print(sum)
        print(min(input_list))