def prime(n):
    nums = [False]*2 + [True]*(2*n-1)
    for i in range(2, 2*n+1):
        if nums[i] == True:
            for j in range(i+i, 2*n+1, i):
                nums[j] = False
    for i in range(2, n+1):
        if nums[i] == True:
            nums[i] = False
    return nums.count(True)

while True:
    n = int(input())
    if n ==0:
        break
    else:
        print(prime(n))