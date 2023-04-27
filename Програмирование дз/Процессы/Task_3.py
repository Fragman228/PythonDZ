import multiprocessing
import time

def dengi(n):
    print(f"Выможете получить {n / 75} долларов")
    time.sleep(0.5)



if __name__ == '__main__':
    while True:
        n = input("Сколько денег вы хотите обменять?, чтбы завершить процесс нажмите на off:\n")
        if n == "off":
            break
        b = multiprocessing.Process(target=dengi, args=(int(n),))
        b.start()
        b.join()
