N, M = map(int, input().split()) # N: 카드의 개수, M: 기준값
card = list(map(int, input().split()))
s_card = []
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            tmp = card[i] + card[j] + card[k]
            if tmp <= M:
                s_card.append(tmp)
print(max(s_card))