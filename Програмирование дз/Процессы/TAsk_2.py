import multiprocessing

arr = multiprocessing.Array('i', 5)
cur_file = "file1.txt"
def ploshad(v, sh, dl, filename,arr):
    pl = 2*(v*dl)+2*(sh*dl)
    print(pl)
    with open(f"{filename}", "a") as f:
        f.write(f"{pl}\n")
    arr[0] = pl
    print(arr)


def kraska(pl, filename):
    rashod = pl * 5
    with open(f"{filename}", "a") as f:
        f.write(str(rashod))

if __name__ == "__main__":
    plo = multiprocessing.Process(target=ploshad, args=(2, 4, 5, cur_file,arr,))
    plo.start()
    plo.join()
    rashod = multiprocessing.Process(target=kraska, args=(arr[0], cur_file,))
    rashod.start()




    print("все")
