#11653 소인수분해


num = int(input())

lis = []
for i in range(2, 101):
    chk = True
    for j in range(2, i):
        if i % j == 0:
            chk = False
            break
    if chk:
        lis.append(i)

def divide(num):
    for x in lis:
        if num%x ==0:
            print(x)
            print(num)
            divide(num//x)
            if num == 0 :
                break

        else:
            continue


divide(num)