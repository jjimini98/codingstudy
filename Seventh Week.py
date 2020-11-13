# 1546 평균

num = int(input())
sum = 0
score = map(int,input().split(" "))

lis = []

for x in score:
    lis.append(x)
max = max(lis)

for y in lis:
    y = y/max*100
    sum += y

print(sum/num)



#4344 평균은 넘겠지

test = int(input())


for x in range(0,test) :
    lis = []
    sum = 0

    ipt = input().split(" ")
    for y in ipt :
        y = int(y)
        lis.append(y)

    total = lis[0]
    score_list= lis[1:]

    fin_lis=[]

    for z in score_list:
        sum +=z
    all = sum/total

    count = 0

    for t in score_list:
        if t>all:
            count+=1

    print(str('%.3f' %round(count/total * 100,3))+"%")


