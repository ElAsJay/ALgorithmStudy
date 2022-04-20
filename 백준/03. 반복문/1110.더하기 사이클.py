a = int(input())

y = a%10
x = (a-y)/10

c = 0
while True:
    tmp = y+x
    tmp = tmp%10
    tmp = y*10 + tmp
    c+=1
    if tmp == a:
        print(c)
        break
    else:
        y = tmp%10
        x = (tmp-y)/10