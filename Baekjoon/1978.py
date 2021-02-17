#1978 소수찾기

num = int(input())
lis = map(int,input().split(" "))

count = 0

for x in lis:
    if x!=1:
        share = []
        for y in range(1,x+1):
            if x%y ==0:
               share.append(y)
        if len(share) == 2:
            count+=1

print(count)