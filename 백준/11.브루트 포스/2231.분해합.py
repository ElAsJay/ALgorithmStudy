def ctor(n):
    for i in range(1,n):
        nums = list(map(int, str(i)))
        s = i + sum(nums)
        if s == n:
            return print(i)
    return print(0)
ctor(int(input()))
