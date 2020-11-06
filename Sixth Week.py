# # 2941 크로아티아 알파벳
# alphabet = input()
# cro = ["c=","c-","dz=","d-","lj","nj","s=","z="]
# sum = 0
#
# for x in cro :
#     if x in alphabet:
#         sum+=1
#         alphabet= alphabet.replace(x, ' ')
#     else:
#         continue
#
# count = len(alphabet)
# print(count)
#
# #1110 더하기 사이클 ( 모르겠음)
#
# number = int(input())
#
# def cycle(number):
#     routine = 0
#     number10 = number//10
#     number1 = number%10
#
#     add_number = number10 + number1
#
#     new_number = (number10*10) + (add_number*1)
#
#     if new_number != number :
#         routine+=1
#         return cycle(number)
#
#     else :
#         return routine
#
# # 1316 그룹단어체커 (find 함수)
# # sum = 0
# #
# # for t in range(int(input())):
# #     word = input()
# #     test = word[0]
# #     for x in word:
# #             if word.find(x) + word.index(test)<=0:
# #                 if word.find(x)+ word.index(test) == 1:
# #                     sum+=1
# #                     break
# #             if x != test:
# #                 sum+=1
# #             if len(x) == 1:
# #                 sum+=1
# #
# # print(sum)

# 다른방법
sum = 0

result = 0
for t in range(int(input())):
    word = input()
    lis = [word[0]]

    for x in range(0,len(word)-1):
            if word[x] == word[x+1]:
                continue
            else:
                lis.append(word[x+1])

    if len(set(lis)) == len(lis):
        result += 1

print(result)


# OX 퀴즈
sum = 0
for x in range(int(input())):
    result = input().split("X")
    for y  in result :
        if len(y) == 0 :
            continue
        else:




