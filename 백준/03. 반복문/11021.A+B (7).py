# Case #1: 2
import sys
t = int(sys.stdin.readline())

for i in range(1, t+1):
    a,b = map(int, sys.stdin.readline().split())
    s = a+b
    sys.stdout.write("Case #"+str(i)+": "+ str(s)+'\n')