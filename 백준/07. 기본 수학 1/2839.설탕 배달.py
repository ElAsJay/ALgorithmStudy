n = int(input())

sugar = -1
a = int(n/5)

while True:
    b = n-a*5
    if b%3 == 0:
        print(int(b/3) + a)
        break
    else:
        if a==0:
            print(-1)
            break
        else:
            a -= 1