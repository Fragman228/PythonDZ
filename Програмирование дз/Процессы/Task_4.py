import multiprocessing
import time
import random

def igra():
    while True:
        time.sleep(1)
        n = input("Введите число: ")
        if n == "off":
            break
        m = random.randint(1, 6)
        if m == int(n):
            print("Вы победили")
        else:
            print("Вы, к сожалению, проиграли(")

def podpiska():
    vremya = 30
    time.sleep(vremya)
    print(f"Подписка закончилась, она длилась {vremya} секунд")

if __name__ == "__main__":
    pr1 = multiprocessing.Process(target=podpiska)
    pr1.start()
    b = pr1.is_alive()
    while b == True:
        print(b)
        igra()

    pr1.join()
    print(b)



