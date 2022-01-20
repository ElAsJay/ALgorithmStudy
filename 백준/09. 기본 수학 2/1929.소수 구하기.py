# 에라토스테네스의 체 알고리즘 공부 선행 필요
m, n = map(int, input().split())

nums = [False]*(2) + [True]*(n-1) # 0,1은 소수X -> 2~n까지 True로 초기화
for i in range(2,n+1):
    if nums[i] == True:
        for j in range(i+i, n+1, i):
            nums[j] = False

for x in range(m, n+1):
    if nums[x] == True:
        print(x)