T = int(input())

avg = []

for _ in range(T):
    num = list(map(int, input().split()))
    avg.append(round(sum(num)/10))

for t in range(T):
    print(f'#{t+1} {avg[t]}')