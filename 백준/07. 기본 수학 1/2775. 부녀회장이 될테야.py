def residence(floor, room):
    base = list(set(range(1, room+1)))
    for _ in range(floor):
        for i in range(1, room):
            base[i] += base[i-1]
    return base[room-1]

T = int(input())
for i in range(T):
    a = int(input())
    b = int(input())
    print(residence(a,b))