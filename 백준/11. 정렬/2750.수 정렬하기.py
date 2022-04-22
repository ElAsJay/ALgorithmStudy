T = int(input())

num=[]
for _ in range(T):
    num.append(int(input()))

num.sort()

for i in range(T):
    print(num[i])
