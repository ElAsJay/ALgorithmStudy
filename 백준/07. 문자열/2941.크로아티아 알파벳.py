croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
#for x in range(97, 123):
#    croatia.append(chr(x))

s = input()

c = 0
for y in croatia:
    if y in s:
        c += s.count(y)
        s=s.replace(y, ".")
        #print(s)
#print(c) #영어 알파벳도 리스트 croatia에 추가한 경우
print(len(s))