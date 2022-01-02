# set을 통해 필터링 및 집합 구성
arr = set(range(1, 10000))
dar = set()

for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    dar.add(i)

# 차집합 사용
self_numbers = arr - dar
# sorted -> 정렬
for i in sorted(self_numbers):
    print(i)
