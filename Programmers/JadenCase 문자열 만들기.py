def solution(s):
    answer = ''
    isFirst = 1
    text = list(s)
    for word in text:
        if word != " ":
            if isFirst:
                answer += word.upper()
                isFirst = 0
            else:
                answer += word.lower()
        else:
            answer += word
            isFirst = 1

    return answer

print(solution("3people unFollowed me"))
