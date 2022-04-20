def is_prime(n):
    nums = [False]*(2) + [True]*(n-1) # 0,1은 소수X -> 2~n까지 True로 초기화
    prime = []
    for i in range(2,n+1):
        if nums[i] == True:
            for j in range(i+i, n+1, i):
                nums[j] = False
    return nums

def prime_sum(n):
    nums = is_prime(n)
    mid = n//2
    for i in range(mid, -1, -1):
        if nums[i] == False:
            continue
        else: # 소수인 경우
            j = n-i
            if nums[j] == True:
                print(min(i,j),max(i, j))
                break

T = int(input())

for _ in range(T):
    n = int(input())
    prime_sum(n)