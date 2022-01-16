x = int(input())
order = 1 # 순서: 1 - 3 - 6 - 10 - ...
count = 1 # 개수: 1 - 2 - 3 - 4 - ...

while True:
#    print('order: {0}, count:{1}'.format(order, count))
    order += count
    count += 1    
    if x < order:
        break

#print('[*] order: {0}, count:{1}'.format(order, count))
s = count
base = order - x

if count%2 == 0:
    print('{0}/{1}'.format(base, s-base))
else:
    print('{0}/{1}'.format(s-base, base))