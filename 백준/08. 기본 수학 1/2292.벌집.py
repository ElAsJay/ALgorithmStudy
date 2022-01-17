import math
import sys

#-------------풀이 (1): 시간 초과--------------------- 
a = int(sys.stdin.readline()) - 1
# 2~7: 2, 8~19: 3, 20~37: 4, 38~61:5
# 1~6       7~18    19~36    37~60
# 0.x-1       1.x-3   3.x-6  6.x-10
# 1         2-3      4-6     7-10 <- x
# 1         1+1      1+1+2   1+1+2+3

x = math.ceil(a / 6)

i = 1
while True:
    way = 1+sum(range(i))
    tmp = 1+sum(range(i+1))
    if x>=way and x<tmp:
        print(i+1)
        break
    else:
        i+=1

#-------------풀이 (2): 성공--------------------- 
b = int(input())

base = 2
count = 1
while b >= base:
    base += 6*count
    count += 1
print(count)
