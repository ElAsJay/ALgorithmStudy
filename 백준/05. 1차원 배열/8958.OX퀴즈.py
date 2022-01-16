def check():
    s = input()
    score = 0
    tmp = 0
    for i in range(len(s)):
        if s[i] == 'O':
            tmp += 1
            score += tmp
        elif s[i] == 'X':
            tmp = 0
    return score


T = int(input())

for t in range(T):
    print(check())