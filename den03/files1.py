import datetime
import glob
import os
import shutil

def print_dir():
    basepath = '../den01'
    for entry in os.listdir(basepath):  # or os.scandir
        if os.path.isfile(os.path.join(basepath, entry)):
            print("File: ", entry)
        if os.path.isdir(os.path.join(basepath, entry)):
            print("Directory: ", entry)

def make_dirs():
    os.chdir("..")
    os.makedirs("2019/11/13", exist_ok=True)
    os.makedirs(os.path.join("2019", "11", "13"), exist_ok=True)

def filter_by_glob():
    os.chdir("../..")
    print(glob.glob("**/*.py", recursive=True))

def ls_la():
    basepath = '../den01'
    for entry in os.listdir(basepath):
        stat = os.stat(os.path.join(basepath, entry))
        print(stat)
        date =  datetime.datetime.fromtimestamp(stat.st_mtime)
        print(date.isoformat())

if __name__ == '__main__':
    ls_la()


