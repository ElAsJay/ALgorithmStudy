N = int(input())
w_list = []
h_list = []
for i in range(N):
    w, h = map(int, input().split())
    w_list.append(w)
    h_list.append(h)

for i in range(N):
    tmp = 1
    for j in range(N):
        if w_list[i] <w_list[j] and h_list[i] < h_list[j]:
            tmp += 1
#    p.append(tmp)
    print(tmp, end=" ")