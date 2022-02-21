import re, read_file, remove_parentheses, copy, os, retrieve_coord

def transf(retrieved_coord):
    from numpy import mat
    from math import sin, cos, radians, degrees, \
                  radians, asin, atan2, fabs, pi

    def translation_z(dis):
        t = mat([
                  [ 1, 0, 0, 0],
                  [ 0, 1, 0, 0],
                  [ 0, 0, 1, dis],
                  [ 0, 0, 0, 1],
                                  ])
        return t
    def translation_x(dis):
        t = mat([
                  [ 1, 0, 0, dis],
                  [ 0, 1, 0, 0],
                  [ 0, 0, 1, 0],
                  [ 0, 0, 0, 1],
                                  ])
        return t
    def rot_y(de):
        t = mat([
                  [ cos(de), 0, sin(de), 0],
                  [ 0,       1,       0, 0],
                  [-sin(de), 0, cos(de), 0],
                  [0, 0, 0, 1]
                                              ])
        return t
    def rot_z(de):
        t = mat([
                  [ cos(de), -sin(de), 0, 0],
                  [ sin(de),  cos(de), 0, 0],
                  [       0,        0, 1, 0],
                  [0, 0, 0, 1]
                                              ])
        return t
    def rot_x(de):
        t = mat([
                  [1, 0, 0, 0],
                  [0, cos(de), -sin(de), 0],
                  [0, sin(de), cos(de), 0],
                  [0, 0, 0, 1]
                                              ])
        return t


    transfered_coord = []
    for i in retrieved_coord:
        #print(i)
        pch_x, pch_y, pch_z, pch_b, pch_c = float(i[1]), float(i[2]), float(i[3]), radians(float(i[4])), radians(float(i[5]))
        apt_coord = rot_z(pch_c) * translation_z(100/25.4) * rot_x(pch_b) * translation_z(450/25.4) * mat([pch_x, pch_y, pch_z, 1]).T
        apt_x, apt_y, apt_z = apt_coord[0,0], apt_coord[1,0], apt_coord[2,0]

        apt_vector = rot_z(pch_c) * rot_x(pch_b) * mat([0,0,1,1]).T
        apt_i, apt_j, apt_k = apt_vector[0,0], apt_vector[1,0], apt_vector[2,0]

        temp = [i[0], round(apt_x,5), round(apt_y,5), round(apt_z,5), round(apt_i,9), round(apt_j,9), round(apt_k,9)]
        transfered_coord.append(temp)

    '''
    output
    '''
    dir = os.getcwd()

    filename_out = rf"{dir}\transfered_coord.txt"
    file_out = open(filename_out, mode='w', encoding='utf-8')
    for i in transfered_coord:
        file_out.write(i[0].ljust(60) + ' ')
        for j in i[1:]:
            file_out.write(str(j).ljust(16) + ' ')
        file_out.write('\n')
    file_out.close



    return transfered_coord



if __name__ == "__main__":

    input_lines = remove_parentheses.remove_par(read_file.read_file())

    retrieved_coord = retrieve_coord.retrieve_coord(input_lines)
    transfered_coord = transf(retrieved_coord)
    print('======================')
    for i in transfered_coord:
        print(i)
