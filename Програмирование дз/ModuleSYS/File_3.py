import os
import sys
a = []
for i in sys.argv:
    a.append(i)

os.mkdir(r"C:\Users\Святослав\Програмирование дз\ModuleSYS\task_3")
os.chdir(r"C:\Users\Святослав\Програмирование дз\ModuleSYS\task_3")
os.system(f"echo {a[1]} > {a[1]}")

