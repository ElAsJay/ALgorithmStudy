a = int(input())
b = int(input())
c = int(input())

m = list(str(a*b*c))
for i in range(10):
    print(m.count(str(i)))