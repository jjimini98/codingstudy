#1085 직사각형 탈출
# x,y,w,h = map(int,input().split(" "))
# print(min(x,y,w-x,h-y))


# #3009 네번째 점
# import itertools
#
# final_list = []
# dotx_list = []
# doty_list = []
# for num in range(0,3):
#     dot_list = []
#     inp = input().split(" ")
#     dotx = int(inp[0])
#     doty = int(inp[1])
#     dotx_list.append(dotx)
#     doty_list.append(doty)
#
#     dot_list.append(dotx)
#     dot_list.append(doty)
#     final_list.append(dot_list)
#
# print(dotx_list)
# print(doty_list)
# print(dot_list)
# print(final_list)
#
#
# caselist = list(itertools.product(dotx_list, doty_list))
# caseset= set(caselist)
# caselist = list(caselist)
#
# print(caselist)
# print(caseset) #[(30, 20), (30, 10), (30, 20), (10, 20), (10, 10), (10, 20), (10, 20), (10, 10), (10, 20)]
# print(caselist)
#
# for x in final_list:
#     x = tuple(x)
#     if x in caselist:
#         caselist.remove(x)
#
# print(caselist[0][0],end=" ")
# print(caselist[0][1])



# 4153 직각삼각형
#
# while True:
#     a,b,c = map(int,input().split(" "))
#     if a == 0 & b==0 & c==0:
#         break
#     squarea = a**2
#     squareb = b**2
#     squarec = c**2
#     maxNum = max(squarea,squareb,squarec)
#     lis = []
#     lis.append(squarea)
#     lis.append(squareb)
#     lis.append(squarec)
#
#     lis.remove(maxNum)
#
#     sum = 0
#     for x in lis:
#         sum+=x
#
#     if sum==maxNum:
#         print("right")
#     else:
#         print("wrong")
#


# 3053 택시기하학
# https://itholic.github.io/kata-taxicab-circle/

# import math
#
# radius = int(input())
#
# pie = math.pi * (radius**2)
#
# print('%.6f'%float(pie))
# print('%.6f'%float((radius**2)*2))
#

# 1002 터렛

from sympy import Symbol, solve
a, b = Symbol('a','b')
x, y = Symbol('x', 'y') # 적의 위치
equation = (a**2) -(x**2) + (b**2) - (y**2)
solve(equation, x,y, dict=True)

