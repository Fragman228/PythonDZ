

import time
import threading

def reminder(n, tm):
    time.sleep(tm)
    print(n)
    time.sleep(1)
    print("Пргорамма завершается")


p1 = threading.Thread(target=reminder, args=(input("О чем вы хотите себе напомнить?    "), 10,))

p1.start()


