import os
import time

def current_directory():
    cwd = os.getcwd()
    print(cwd)

def file_path(filename):
    path = os.path.abspath((filename))
    print(path)

current_directory()
filename="sample.txt"
file_path(filename)

epc = time.time()
print(epc)
