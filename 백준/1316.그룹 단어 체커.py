T = int(input())
count = 0

def check():
    s = input()
    tmp = s[0]
    group = [tmp]
    flag = 1
    for i in range(1, len(s)):
        if s[i] == tmp:
            continue
        else:
            if s[i] in group:
                flag = 0
                break
            else:
                tmp = s[i]
                group.append(tmp)
    return flag


for t in range(T):
    count += check()
print(count)
    

