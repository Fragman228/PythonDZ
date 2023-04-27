import multiprocessing

def task1(strt = 1):
    counter = 0
    while strt != 100_000_000:
        if strt % 2 == 1:
            counter += 1
        strt += 1
    print(f"Всего {counter} делителей")
def task2(strt = 1):
    counter = 0
    while strt != 100_000_000:
        if strt % 2 == 0:
            counter += 1
        strt += 1
    print(f"Всего {counter} делителей")
if __name__ == "__main__":

    p1 = multiprocessing.Process(target=task1)
    p2 = multiprocessing.Process(target=task2)

    p1.start()
    p2.start()






