import os

def file_list():
    d = input()

    fw = open(f"C:\\Users\\ElAsJay\\Desktop\\Programming\\Python_Study\\파이썬으로 배우는 알고리즘 트레이딩\\07.파일 다루기\\flist.txt", "wt")
    fw.write(f"[*] Path: "+d + "\n")
    for file in os.listdir(d):
        fw.write(file + '\n')

file_list()