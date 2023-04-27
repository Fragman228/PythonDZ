import os
import queue
import threading

path = r"C:\Users\Святослав\Програмирование дз\Treadpool"
def puti(smn,path):
    path += f"\{smn}"
    return path


def crfile(path):
    os.chdir(path)
    os.system("echo Hello World > file.txt")

countline = 0
names = []

with open("Names.txt", encoding="utf-8") as f:
    for line in f:
        countline += 1
        names.append(line)

q = queue.Queue(maxsize=countline)

for i in range(countline):
    q.put(threading.Thread(target=puti, args=(names[i-1])))

print(q.get())






