'''
def solution(s):
    answer = 0
    same = 1
    diff = 0
    p = s[0]

    for i in range(1, len(s)):
        if s[i] == p:
            same += 1
        else:
            diff += 1
            if same == diff:
                if i < len(s) - 1:
                    answer += solution(s[i+1:])
                break
    return answer + 1
'''
def solution(s):
    answer = 0
    lst = ["", 0, 0]
    idx = 1
    for c in s:
        if lst[0] == "":
            lst[0] = c
            lst[1] += 1
        else:
            if c == lst[0]:
                lst[1] += 1
            else:
                lst[2] += 1
                if lst[1] == lst[2]:
                    answer += 1
                    lst = ["", 0, 0]
    if lst[0] != "":
        answer += 1
    return answer
        

print(solution("banana"))
print(solution("abracadabra"))
print(solution("aaabbaccccabba"))
print(solution("baaa"))
print(solution("aaba"))