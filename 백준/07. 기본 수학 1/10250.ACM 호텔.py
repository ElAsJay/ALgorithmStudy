# 6 12 6을 입력했을 때 601호가 제대로 나오도록 하는 것을 놓치면 안됨!!
def room():
    h, w, n = map(int, input().split())
    floor = n%h
    if floor == 0:
        floor = h
        num = int(n/h)
    else:
        num = 1+int(n/h)
    print(str(floor)+'{0:02d}'.format(num))

T = int(input())

for i in range(T):
    room()