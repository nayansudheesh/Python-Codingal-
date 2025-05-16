import os

shutdown = input("Do you want to shut your computer down?")

if shutdown == 'no':
    exit()
else:
    os.system("shutdown /s /t 1")