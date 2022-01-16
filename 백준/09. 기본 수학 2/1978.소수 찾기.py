T = int(input())
num = list(map(int, input().split()))
prime = 0
for n in num:
    # 에라토스테네스의 체
    if n == 1:
        continue
    elif n == 2:
        prime += 1
    else:
        for i in range(2, n):
            if n % i == 0:
                break
            if i == n-1:
                prime+=1
print(prime)