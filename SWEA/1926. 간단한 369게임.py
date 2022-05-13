import sys

T = int(input())

num = []
# 10 <= N <= 1,000
for n in range(1, T+1):
    tmp = n
    r = 0
    for j in range(1,4):
        t = pow(10, j)
        if tmp % t == 3 or tmp%t == 6 or tmp%t == 9:
            r +=1
        tmp -= (n%t)*t
    if r == 0:
        num.append(n)
    if r != 0:
        num.append('-'*r)

for x in num:
    print(x, end=' ')
