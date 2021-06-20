from util import *

#matrix here is matrix[row][col].
#We assume that $M is a mxn 0-1 matrix with hamming weight at most 2^k in any row.
#m = row_dim, n = col_dim, k = max depth
'''
Input: 
matrix -binary matrix 
k - goal depth
i - phase 
ip - column for that the phase is up until.
Output: 
True if there exist a row with at least 2**(k-i) hamming weight
else False.
'''
def HW_Row_atleast_two_k_minus_i(matrix,k,i, ip):
    row_dim = len(matrix)
    if (2**(k-i-1) < 1):
        return False
    for row in range(row_dim):
        HW_row = 0
        for j in range(ip):
            HW_row += matrix[row][j]
        print("HW_row "+ str(row) +": " + str(HW_row))
        if (HW_row > 2**(k-i-1)):
            return True
    return False

'''
Input: 
matrix -binary matrix 
ip - column for that the phase is up until.
Output: 
True - if there exist a row with hamming weight = 2
else False.
i - the row such that is Hamming weight = 2
lst[0] =  the index of the first column with =1 
lst[1] =  the index of the second column with =1 
'''
def HW_Row_two(matrix,ip):
    row_dim = len(matrix)
    for i in range(row_dim):
        HW_row = 0
        for j in range(ip):
            HW_row += matrix[i][j]
        if (HW_row == 2):
            lst = []
            for j in range(ip):
                if matrix[i][j] == 1:
                    lst.append(j)

            return (True, i, lst[0], lst[1])
    return (False, None, None, None)

'''
Input: 
matrix - binary matrix with hamming weight at most 2**k in any row
m - number of row 
n - number of column 
k - goal depth. 
Output: 
matrix: the final matrix 
'''
def Low_Depth_Greedy(matrix, m,n, k):
    s = n+1 # index fo the next column
    i = 0 #phase
    ip = n #columns up to n that have XOR depth of at most i
    dict_XOR = {} ## store keys = column index and value =the columns that are in pairs
    flag = HW_Row_atleast_two_k_minus_i(matrix,k,i,ip)
    print("Start: ")
    Printmatrix(matrix)
    while(flag):
        # print()
        # print("Phase i: " + str(i))
        # print("Phase ip: " + str(ip))

        flag2, row_index, j1,j2 = HW_Row_two(matrix, ip)
        # print("HW_Row_two j1: " +str(j1))
        # print("HW_Row_two j2: " +str(j2))
        new_col = []
        if (flag2 == True):
            dict_XOR[s] = (j1, j2)
            for r in range(m):
                if (r == row_index):
                    new_col.append(1)
                else:
                    new_col.append(0)
            matrix = Transpose(matrix)
        else:
            hmax = 0
            matrix = Transpose(matrix)

            for col1 in range(ip):
                for col2 in range(col1+1,ip-1):
                    colj1 = matrix[col1]
                    colj2 = matrix[col2]
                    AND_column = AND_GATE_COL(colj1, colj2)
                    HW = HammingWeight(AND_column)
                    if (HW > hmax):
                        hmax = HW
                        j1 = col1
                        j2 = col2
                        new_col = AND_column
            # print("Greedy j1: " + str(j1))
            # print("Greedy j2: " + str(j2))
            dict_XOR[s] = (j1,j2)

        ##Change the column
        mxcolj1 = matrix[j1]
        mxcolj2 = matrix[j2]
        matrix.append(new_col)
        NOT_new_col = NOT_GATE_COL(new_col)
        matrix[j1] = AND_GATE_COL(mxcolj1, NOT_new_col)
        matrix[j2] = AND_GATE_COL(mxcolj2, NOT_new_col)
        s = s+1
        matrix = Transpose(matrix)
        # print("After iteration: ")
        Printmatrix(matrix)
        flag = HW_Row_atleast_two_k_minus_i(matrix,k,i,ip)
        if(flag == False):
            ip = s-1
            i = i+1
            # print("Update")
            flag = HW_Row_atleast_two_k_minus_i(matrix,k,i,ip)

    # print("Ending:")
    print(dict_XOR)
    Printmatrix(matrix)
    return matrix



matrix = [[1,1,0,1,0,0,1],[1,1,1,1,1,1,0], [0,0,1,1,1,1,1],[1,0,0,1,1,0,1], [0,1,0,0,0,0,0],[0,0,1,0,0,0,0], [0,0,0,1,0,0,0], [0,0,0,0,1,0,0],[0,0,0,0,0,1,0]]
matrix = Transpose(matrix)
m = len(matrix)
n = len(matrix[0])
k = 2
Low_Depth_Greedy(matrix, m, n, k)