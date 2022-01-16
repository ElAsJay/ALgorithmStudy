h, m = input().split()
h = int(h)
m = int(m)

if m<45:
    m = 60 - (45 - m)
    if h==0:
        h = 23
    else:
        h -= 1
else:
    m -= 45
print(str(h)+" "+str(m))