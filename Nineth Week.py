# 1978 소수 찾기

from primePy import primes

sum = 0
length = int(input())
inp = input().split(" ")
for t in inp:
    t = int(t)
    if primes.check(t) == True:
        sum +=1
        if t == 1:
            sum -= 1

    else:
            continue
print(sum)






# def prime_number(number): #개수
#     for num in range(number):
#         inp = map(int,input().split(" "))
#         lis = []
#         for x in range(1,inp):
#             for y in range(1,inp):
#                 prime = x*y
#                 if prime == number:
#                     lis.append(prime)
#     return len(lis)
#
#
#
# prime_number(4)