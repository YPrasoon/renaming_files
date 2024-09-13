#Renaming in bulk

import os
import pathlib 
import time

def main():
    i = 0
    source_folder = input("input the source folder : ") # need to copy the source folder name here
    workpath = pathlib.PureWindowsPath(source_folder)   
    path = workpath.as_posix() + "/"
    #path = path + "/"
    for filename in os.listdir(path):
        my_dest = "testfile_" + str(i) + ".jpg"
        my_source = path + filename
        my_dest = path + my_dest
        os.rename(my_source, my_dest)
        i += 1
    time.sleep(1)
    print(".")
    time.sleep(1)
    print('.')
    time.sleep(1)
    print('.')
    time.sleep(1)
    print("Renaming complete")

if __name__ == '__main__':
    main()
