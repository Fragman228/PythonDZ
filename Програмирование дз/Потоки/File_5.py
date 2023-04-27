import threading
import os

def renam(i):
    with open(f"C:\Users\Святослав\Програмирование дз\Потоки\Files\file{i}", "w") as f:
        if "ids:12345" in f:
            f.write("id: 12345")

for i in range(0,10):
    ren = threading.Thread(target=renam, args=(i,)).start()

