T = int(input())

num = []
# 10 <= N <= 1,000
for n in range(1, T+1):
    tmp = n
    r = 0; j = 1
    while tmp != 0:
        if tmp % 10 == 3 or tmp % 10 == 6 or tmp % 10 == 9:
            r += 1
        tmp = int(tmp/10)
    if r == 0:
        num.append(n)
    if r != 0:
        num.append('-'*r)

for x in num:
    print(x, end=' ')
