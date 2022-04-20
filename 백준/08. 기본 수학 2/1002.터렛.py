def turret():
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    d = (pow(x1-x2,2)+pow(y1-y2,2))**(1/2)
    r_list = [r1, r2, d]
    m = max(r_list)
    r_list.remove(m)
    if r1==r2 and d == 0:
        print(-1)
    elif m < sum(r_list):
        print(2)
    elif m == sum(r_list):
        print(1)
    else:
        print(0)

T = int(input())

for x in range(T):
    turret()
