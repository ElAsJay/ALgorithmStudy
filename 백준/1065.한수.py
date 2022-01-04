# 함수 version
def count(n):
    han = 0
    for i in range(1, n+1):
        if i<100:
            han += 1
        else:
            # 정수 i를 문자열로 변환해 각 자리를 정수 배열의 값으로 구성
            i_list = list(map(int, str(i)))
            # ex. 237 -> '237' -> [2, 3, 7]
            if i_list[0]-i_list[1] == i_list[1]-i_list[2]:
                han += 1
    print(han)

num = int(input())
count(num)

-------------------------------------------------------------
num = int(input())
h = 0
for i in range(1, num+1):
    if i<100:
        h +=1
    else:
        n = list(map(int, str(i)))
        if n[0]-n[1] == n[1]-n[2]:
            h += 1
print(h)
