from util import *
## Consider the matrix as matrix[col][row] with only 0 and 1


'''
This gives us the number of Xor created through the algorithm. 
'''
def CalculateNumOfXOR(matrix, counter):
    Num_Xor = counter
    for i in range(len(matrix)):
        Num_Xor += (HammingWeight(matrix[i])-1)
    return Num_Xor


'''
Input:
matrix - Binary Matrix of list of list
Output: 
matrix - the final state of the Binary matrix
Num_XOR - number of XOR in the circuit 
lst - To keep what are the variables for a XOR gate for each column in the matrix.
'''
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
                HW = HammingWeight(AND_GATE_COL(coli, colj)) ## Caculate the Hamming Weight of coli & colj.
                if(HW > hmax): #Record the column with maximum Hamming Weight when AND.
                    hmax = HW
                    maxi = i
                    maxj = j
        if(hmax > 1):
            #Initialised the best column that was chosen above and AND them.
            mxcoli = matrix[maxi]
            mxcolj = matrix[maxj]
            new_col = AND_GATE_COL(mxcolj,mxcoli)
            #Create a new column with that new column
            matrix.append(new_col)
            #Here we set the old columns that have 1 in new column to 0.
            NOT_new_col = NOT_GATE_COL(new_col)
            matrix[maxi] = AND_GATE_COL(mxcoli,NOT_new_col)
            matrix[maxj] = AND_GATE_COL(mxcolj,NOT_new_col)
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
# print(AND_GATE_COL(col1,col2))
# print(NOT_GATE_COL(col1))


"""
The example here was given by QuanQuan in https://dr.ntu.edu.sg/bitstream/10356/83155/1/Masters_Thesis_TAN_QUAN_QUAN.pdf
for his Master Thesis, Optimising implementation of block ciphers.
"""
matrix = [[1,1,0,1,0,0,1],[1,1,1,1,1,1,0], [0,0,1,1,1,1,1],[1,0,0,1,1,0,1], [0,1,0,0,0,0,0],[0,0,1,0,0,0,0], [0,0,0,1,0,0,0], [0,0,0,0,1,0,0],[0,0,0,0,0,1,0]]
#Printmatrix(Transpose(matrix))
matrix, num_xor, lst = Paar_algorithm(matrix)
Printmatrix(Transpose(matrix))
print(num_xor)
print(lst)