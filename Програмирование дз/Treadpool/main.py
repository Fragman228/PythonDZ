import threading
from time import sleep
ochered = []
def familia(n):
    while True:
        if n == "off":
            break
        else:
            print("Введите фамилию: ")

p1 = threading.Thread(target=familia, args=(input("Введите фамиию человека,которого хотите отчислить:\n"),))

p1.start()
sleep(1)
print(ochered)

def otchislenie():
    for i in range(len(ochered)):
        print(f"Студент {ochered[i]} успешно отчислен")
        return i

p2 = threading.Thread(target=otchislenie, args=(otchislenie(),)).start()
