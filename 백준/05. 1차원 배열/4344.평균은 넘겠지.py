t = int(input())
for i in range(t):
    n = list(map(int, input().split()))
    avg = sum(n[1:])/n[0]
    h = 0
    for score in n[1:]:
        if score > avg:
            h += 1
    rate = h/n[0] * 100
    print(f'{rate:.3f}%')