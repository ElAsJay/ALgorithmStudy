def p(n):
    for i in range(2, n+1):
        if n%i == 0:
            print(i)
            n = int(n/i) # int형 변환 필요
            p(n) # 재귀
            break # 반복되지 않도록 break

n = int(input())

# prime number
if n == 1:
    print("")
else:
    p(n)