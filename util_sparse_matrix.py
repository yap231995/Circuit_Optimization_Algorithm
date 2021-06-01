#Let matrix be formed by the following way:
#dimension, total_number_non_zero, number_nonzero_per_row, position_of_the_nozero.
row = 5
col = 5
dim = [row,col]
nz = 6 #total sum of value in  nz_per_row and length of pos
nz_per_row = [1,0,2,2,1]
pos = [0,1,4,2,3,4]
matrix = [dim, nz, nz_per_row, pos]

def Convert_SparseMatrix_to_Matrix(matrix):
    row = matrix[0][1]
    col = matrix[0][1]
    listmatrix = []
    nz_per_row = matrix[2]
    pos = matrix[3]
    counter = 0
    for i in range(row):
        listmatrix_row = [0 for k in range(col)]
        number_non_zero_row_i = nz_per_row[i]
        while(number_non_zero_row_i > 0):
            position = pos[counter]
            listmatrix_row[position] = 1
            counter += 1
            number_non_zero_row_i -=1
        listmatrix.append(listmatrix_row)
    return listmatrix


def Printmatrix(listmatrix):
    row = len(listmatrix)
    for i in range(row):
        print(listmatrix[i])


listmatrix = Convert_SparseMatrix_to_Matrix(matrix)
Printmatrix(listmatrix)






