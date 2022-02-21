import re, read_file, remove_parentheses, copy, os
def retrieve_coord(input_lines):
    lines = []
    ordered_lines=[]

    for i in input_lines:
        result = re.findall('[XYZAC]\[?-?(?:\d+)?\.?\d+', i.strip())
        if result != []:
            for index, j in enumerate(result):
                result[index] = j.replace('[',  '')
            result.insert(0, i.strip())
            lines.append(result)

    '''
    order the AXIS
    '''
    axis_order = 'XYZAC'
    result = ['name', 'X0.', 'Y0.', 'Z0.', 'A0.', 'C0.']
    #print("lines is:\n", lines)
    for line in lines:

        result[0] = line[0]
        for index, axis_name in enumerate(axis_order):
            for axis in line[1:]:
                if axis[0] == axis_name:
                    result[index + 1] = axis[1:]
                    break

        temp = copy.deepcopy(result)
        ordered_lines.append(temp)

    '''
    output
    '''
    dir = os.getcwd()

    filename_out = rf"{dir}\retrieved_coord.txt"
    file_out = open(filename_out, mode='w', encoding='utf-8')
    for i in ordered_lines:
        #print("in retrieve_coord modual:", i)
        file_out.write(i[0].ljust(60) + ' ')
        for j in i[1:]:
            file_out.write(j.ljust(10) + ' ')
        file_out.write('\n')
    file_out.close


    return ordered_lines



if __name__ == "__main__":

    input_lines = remove_parentheses.remove_par(read_file.read_file())

    temp = retrieve_coord(input_lines)
    print('======================')
    for i in temp:
        print(i)
