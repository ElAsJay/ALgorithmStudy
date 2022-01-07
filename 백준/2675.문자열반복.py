def re():
    r, s = input().split()
    r = int(r)
    p = ""
    for c in s:
        p += c*r
    print(p)

t = int(input())
for i in range(t):
    re()