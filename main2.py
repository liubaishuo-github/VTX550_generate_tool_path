import read_file, remove_parentheses, retrieve_coord, rotation_matrix, generate_lines_catia

pch_file = read_file.read_file()
non_parentheses_pch_file = remove_parentheses.remove_par(pch_file)
retrieved_coord = retrieve_coord.retrieve_coord(non_parentheses_pch_file)
transfered_coord = rotation_matrix.transf(retrieved_coord)



generate_lines_catia.generate_lines_catia(transfered_coord)
#generate_lines_catia.generate_points_catia(transfered_coord)
