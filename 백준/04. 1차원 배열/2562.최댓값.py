s=[]
for i in range(9):
    s.append(int(input()))
print(max(s))
print(s.index(max(s))+1)