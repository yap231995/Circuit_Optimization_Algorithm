def HammingWeight(vector):
    length = len(vector)
    HW = 0
    for i in range(length):
        HW += vector[i]
    return HW


def AND_GATE_COL(col1,col2):
    lst = []
    for i in range(len(col1)):
        lst.append(col1[i]& col2[i])
    return lst

def NOT_GATE_COL(col):
    lst = []
    for i in range(len(col)):
        lst.append(col[i]^1)
    return lst

def Transpose(matrix):
    row = len(matrix[0])
    col = len(matrix)
    lst = []
    for i in range(row):
        row_lst = []
        for j in range(col):
            row_lst.append(matrix[j][i])
        lst.append(row_lst)
    return lst
def Printmatrix(listmatrix):
    row = len(listmatrix)
    for i in range(row):
        print(listmatrix[i])