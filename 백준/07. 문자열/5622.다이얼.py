# (A,B,C):3 (D,E,F):4 (G,H,I):5 (J,K,L):6 (M,N,O):7 (P,Q,R,S):8 (T,U,V):9 (W,X,Y,Z):10
dial = input()
t = 0
for x in dial:
    if x>='A':
        t += 3
    if x>='D':
        t += 1
    if x>='G':
        t+=1
    if x>= 'J':
        t+=1
    if x>='M':
        t+=1
    if x>='P':
        t+=1
    if x>='T':
        t+=1
    if x>='W':
        t+=1
print(t)
# -----------------------------------------

num = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
dial = input()
t = 0
for x in dial:
    for n in num:
        if x in n:
            # num 리스트에서 n 인덱스 검색 + 3 (기본2)
            t += num.index(n) + 3
print(t)