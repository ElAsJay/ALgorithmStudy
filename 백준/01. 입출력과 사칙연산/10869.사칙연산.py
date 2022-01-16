# A+B, 둘째 줄에 A-B, 셋째 줄에 A*B, 넷째 줄에 A/B, 다섯째 줄에 A%B

a, b = input().split()
a = int(a)
b = int(b)

print(a+b)
print(a-b)
print(a*b)
print(int(a/b))
print(a%b)