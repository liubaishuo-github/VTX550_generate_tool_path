import os
def read_file():
    dir = os.getcwd()
    #print(dir)
    filename = f"{dir}\VTX550.pch"
    #print(filename)
    with open(filename, encoding='utf-8-sig') as f:
        lines = f.readlines()
    return lines




if __name__ == "__main__":

    txt = read_file()

    for i in txt:
        print(i)

    print(type(txt))
