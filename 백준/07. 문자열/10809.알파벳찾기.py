# 아스키코드를 활용해 알파벳을 배열화
alphabet = set(range(97, 123))
c = input()

for x in alphabet:
    print(c.find(chr(x)))
    # chr(x): 아스키 코드 -> 문자 변환
    # c.find(ch): 문자열 c에서 문자 ch를 검색하고, 최초의 위치를 반환한다. 없는 경우 -1을 반환한다.