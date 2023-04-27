import time
import threading

def tiker():
    while True:
        print("Бомба тикает")
        time.sleep(3)
tk = threading.Thread(target=tiker, daemon=True).start()
while True:
    c = int(input("\nВведите код от бомбы\n"))
    if c == 777:
        break
    else:
        print("Код неверный")

