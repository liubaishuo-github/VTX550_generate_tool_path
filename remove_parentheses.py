import re, read_file
def remove_par(input_lines):
    lines = []
    for i in input_lines:
        result = re.sub('\(.*?\)', '', i.strip())
        lines.append(result.replace(" ",""))

    return lines




if __name__ == "__main__":

    input_lines = read_file.read_file()


    print(input_lines)


    for i in remove_par(input_lines):
        print(i)
