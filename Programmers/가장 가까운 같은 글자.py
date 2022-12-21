def solution(s):
    answer = []
    s = list(s)
    s2 = {}
    for i in range(len(s)):
        c = s[i]
        if c in s2:
            answer.append(i - s2[c])
            s2[c] = i
        else:
            answer.append(-1)
            s2[c] = i
    return answer

print(solution("banana"))
print(solution("footbar"))