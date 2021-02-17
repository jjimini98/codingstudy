# 2부터 100까지의 소수 구하기

for i in range(2, 101):     # i 값이 2부터 1씩 증가하면서 100이 될때까지 반복
    chk = True
    for j in range(2, i):   # j 값이 1부터 1씩 증가하면서 i-1이 될때까지 반복
        if i%j == 0:        # i를 j로 나눈 나머지가 0이면
            chk = False     # chk에 False을 저장하고
            break           # 반복문 종료
    if chk:                 # chk 값이 False가 아니면 소수이므로 출력
        print(i, end=" ")
