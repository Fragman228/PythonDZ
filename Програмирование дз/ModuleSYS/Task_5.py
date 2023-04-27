import sys
import os
a = sys.argv
coms_list = []
with open(fr"C:\Users\Святослав\Програмирование дз\ModuleSYS\task_5\{a[1]}", "r") as f:
    for i in f.readlines():
        coms_list.append(i)

    os.system(coms_list[0])
    os.system(coms_list[1])
    f.close()
