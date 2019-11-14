import os

def write_to_file1():
    f = open("file.txt", "a") # "a" means append
    f.write("ahoj" + os.linesep)
    f.write("ahoj" + os.linesep)
    f.close()

def write_to_file2():
    with open("file.txt", "w") as f:
        f.write("ahoj" + "\n")
        f.write("ahoj" + os.linesep)

def online_write_to_file():
    open("file.txt", "a").write("LL")

if __name__ == '__main__':
    with open("file.txt", "br") as f:
        s = f.read()
        for c in s:
            print(int(c))
