T = int(input())

for t in range(T):
    N = int(input())
    a = 0; b=0;c=0;d=0;e=0 # a: 2의 지수, b: 3의 지수, c: 5의 지수, d: 7의 지수, e: 11의 지수
    while N != 1:
        if N%2 == 0:
            a += 1
            N /= 2
        elif N%3 == 0:
            b += 1
            N /= 3
        elif N%5 == 0:
            c += 1
            N /= 5
        elif N%7 == 0:
            d += 1
            N /= 7
        elif N%11 == 0:
            e += 1
            N /= 11
    
    print(f"#{t+1} {a} {b} {c} {d} {e}")