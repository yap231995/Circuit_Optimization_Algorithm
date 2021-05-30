
## Consider the matrix as matrix[col][row] with only 0 and 1
def HammingWeight(vector):
    length = len(vector)
    HW = 0
    for i in range(length):
        HW += vector[i]
    return HW

def AND_GATE(col1,col2):
    lst = []
    for i in range(len(col1)):
        lst.append(col1[i]& col2[i])
    return lst
def NOT_GATE(col):
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


def CalculateNumOfXOR(matrix, counter):
    Num_Xor = counter
    for i in range(len(matrix)):
        Num_Xor += (HammingWeight(matrix[i])-1)
    return Num_Xor
def Paar_algorithm(matrix):

    last_col = len(matrix)
    hmax = 2 # ensure it go in at the start.
    lst = []
    counter = 0

    while(hmax > 1):
        hmax = 0
        maxi = 0
        maxj = 0
        for i in range(last_col):
            for j in range(i+1,last_col-1):
                coli = matrix[i]
                colj = matrix[j]
                HW = HammingWeight(AND_GATE(coli, colj))
                if(HW > hmax):
                    hmax = HW
                    maxi = i
                    maxj = j
        # print("maxi: " + str(maxi))
        # print("maxj: " + str(maxj))
        if(hmax > 1):
            mxcoli = matrix[maxi]
            mxcolj = matrix[maxj]
            new_col = AND_GATE(mxcolj,mxcoli)
            matrix.append(new_col)
            NOT_new_col = NOT_GATE(new_col)
            matrix[maxi] = AND_GATE(mxcoli,NOT_new_col)
            matrix[maxj] = AND_GATE(mxcolj,NOT_new_col)
            last_col += 1
            counter +=1
            lst.append((maxi, maxj)) ## To keep what are the variables for a XOR gate.
            # print("Change matrix " + str(counter) +": ")

        x = Transpose(matrix)
        Num_XOR = CalculateNumOfXOR(x, counter)
    return (matrix,Num_XOR, lst)

# col1 = [1,0,0,1]
# col2 = [1,0,1,0]
# print(HammingWeight(col1))
# print(AND_GATE(col1,col2))
# print(NOT_GATE(col1))

matrix = [[1,1,0,0,0,0,1],[1,1,1,1,1,1,0], [0,0,1,1,1,1,1],[1,0,0,1,1,0,1], [0,1,0,0,0,0,0],[0,0,1,0,0,0,0], [0,0,0,1,0,0,0], [0,0,0,0,1,0,0],[0,0,0,0,0,1,0]]
#Printmatrix(Transpose(matrix))
matrix, num_xor, lst = Paar_algorithm(matrix)
Printmatrix(Transpose(matrix))
print(num_xor)
print(lst)