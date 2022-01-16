while True:
    lines = list(map(int, input().split()))
    if lines[0] == lines[1] == lines[2] == 0:
        break
    else:
        c = max(lines)
        lines.remove(c)
        if c**2 == lines[0]**2 + lines[1]**2:
            print("right")
        else:
            print("wrong")

