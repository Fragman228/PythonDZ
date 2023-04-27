import threading

ochered = []

def delit(ch):
    count = 0
    spisok = []
    for i in range(1, ch):
        if ch % i == 0:
            count += 1
            spisok.append(i)
    print(count, spisok)
n = 0
while True:
    n = input("Введите число\n")
    if n == 'off':
        break
    ochered.append(int(n))

for i in range(len(ochered)):
    potok = threading.Thread(target=delit, args=(ochered[i],)).start()

