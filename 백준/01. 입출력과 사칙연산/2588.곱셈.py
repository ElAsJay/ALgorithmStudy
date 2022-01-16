a = int(input())
b = int(input())

h = int(b/100)
t = int((b-h*100)/10)
o = b - h*100 - t*10

print(a*o)
print(a*t)
print(a*h)

print(a*o+10*a*t+100*a*h)