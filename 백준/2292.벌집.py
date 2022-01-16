import math
a = int(input())
# 2~7: 1, 8~19: 2, 20~37: 3, 38~61:4
# 1~6       7~18    19~36    37~60
# 0.x-1       1.x-3   3.x-6  6.x-10
# 1         2-3      4-6     7-10 <- x
# 1         1+1      1+1+2   1+1+2+3

x = math.ceil((a-1) / 6)
#print(x)
if x == 1:
    print(2)
else:
    i = 1
    i = int(math.sqrt())
    while True:
        way = int(i*(i+1)/2)
        tmp = int((i+1)*(i+2)/2)
        if x>=(1+way) and x<(1+tmp):
            print(i+2)
            break
        else:
            i+=1