import os
for i in r"C:\Проэкты\Target":
    if fr"C:\Проэкты\Target\{i % 2}" == 0:
        os.rename(i, fr"C:\Проэкты\Папка {i}")
