M = int(input()) # M 이상
N = int(input()) # N 이하
prime = []

for i in range(M, N+1):
    if i == 2:
        prime.append(i)
        continue
    for j in range(2, i):
        if i % j == 0:
            break
        else:
            if j == i-1:
                prime.append(i)
#print(prime)

if len(prime) == 0:
    print(-1)
else:
    print(sum(prime))
    print(min(prime))