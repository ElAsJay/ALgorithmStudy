import math
r = int(input())

#print(round(r*r*math.pi, 6)) # 소수점 아래 0 표시 X
print("{:.6f}".format(r*r*math.pi))
print("{:.6f}".format(2*r*r))