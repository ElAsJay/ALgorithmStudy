def solution(A,B):
    answer = 0
    sortA = sorted(A)
    sortB = sorted(B, reverse=1)
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    for i in range(len(A)):
        answer += (sortA[i]*sortB[i])
    print(A, B, answer)

    return answer

solution([1,4,2], [5,4,4])
solution([1,2], [3,4])