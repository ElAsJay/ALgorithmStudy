a, b = map(str, input().split())

# 내 풀이: 리스트 역순으로 값 비교
for i in range(2, -1, -1):
    if a[i] > b[i]:
        c = a
        break
    elif a[i] < b[i]:
        c = b
        break
print(c[2]+c[1]+c[0])

# --------------------------------------
# 리스트 특성 이용
a = int(a[::-1])
b = int(b[::-1])

if a > b:
    print(a)
else:
    print(b)