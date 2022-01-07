s = input().upper()
# print(s)
alphabet = list(set(range(65, 91)))
c_list = []
for x in alphabet:
    c_list.append(s.count(chr(x)))
# print(c_list)

maximum = max(c_list)
m_ind = c_list.index(maximum)

if c_list.count(maximum) > 1:
    print("?")
else:
    print(chr(alphabet[m_ind]))