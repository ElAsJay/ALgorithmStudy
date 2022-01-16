# 자기 점수 중에 최댓값을 골랐다. 이 값을 M이라고 한다. 그리고 나서 모든 점수를 점수/M*100
t = int(input())
score = list(map(int, input().split()))
s = 0
m = max(score)
for i in range(t):
    s += score[i]/m*100
print(s/t)