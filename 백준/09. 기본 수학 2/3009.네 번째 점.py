x = []
y = []
for i in range(3):
    x_tmp, y_tmp = map(int, input().split())
    x.append(x_tmp)
    y.append(y_tmp)

# x
if x[0] == x[1]:
    x_result=x[2]
elif x[0] == x[2]:
    x_result=x[1]
else:
    x_result = x[0]

# y
if y[0] == y[1]:
    y_result = y[2]
elif y[0] == y[2]:
    y_result = y[1]
else:
    y_result=y[0]

print(x_result, y_result)
