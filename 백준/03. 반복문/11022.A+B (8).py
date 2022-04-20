# Case #1: 1 + 1 = 2
import sys

t = int(sys.stdin.readline())

for i in range(1, t+1):
    a,b = map(int, sys.stdin.readline().split())
    sys.stdout.write("Case #"+str(i)+": "+str(a)+" + "+str(b)+" = "+str(a+b)+"\n")