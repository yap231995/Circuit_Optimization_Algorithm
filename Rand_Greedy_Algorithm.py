import numpy as np
import random
import heapq
from util import *

def HW_Row_more_than_one(matrix):
    m = len(matrix)  # Number of Rows
    n = len(matrix[0])  # Number of Columns
    for i in range(m): #For each Row
        HW_row = 0
        for j in range(n): #For each Column in that Row
            HW_row += matrix[i][j] #Calculate the Hamming Weight.
        if (HW_row > 1):
            return True
    return False

'''
Input: 
H: Priority Queue (Min_Heap) with Depths of all the columns with 1 in the row r. Lowest depth has the priority.
gd: goal_depth of row r. 
Output: 
return True if variables of depths in Priority Queue H can be calculated(i.e XOR) to be within the goal depth.     
'''
def Feasible(H, gd):
    while len(H) > 1:
        d1 = heapq.heappop(H)
        d2 = heapq.heappop(H)
        heapq.heappush(H,1+max(d1,d2))
    d = heapq.heappop(H)
    if d <= gd:
        return True
    return False


def Feasible_Update(matrix, goal_depth_r, depth_lst, s, c1,c2,r):
    if matrix[r][c1] == 1 and matrix[r][c2] == 1:
        H = []
        for col in range(s-1):
            if col != c1 and col != c2: ##Dont include {c1,c2} because we want to assume that they have been used.
                if matrix[r][col] == 1:
                    depth_col = depth_lst[col]
                    heapq.heappush(H,depth_col)
        heapq.heappush(H,1+max(depth_lst[c1], depth_lst[c2]))
        return Feasible(H, goal_depth_r)
    return False

'''
Input: 
matrix: a binary matrix of mxn 
goal_depth: goal of the depth, list of length m 
depth_lst: input depth for each column of matrix, list of length n
'''
def Rand_Greedy_Algorithm(matrix, goal_depth, depth_lst):
    m = len(matrix)  # Number of Rows
    n = len(matrix[0]) #Number of Columns
    s = n+1 #The index of the next new column
    v_c_lst = np.eye(n,n, dtype = int)  ##v_c_lst Rows: v(c), Columns different variables at play
    circuit_lst = []  ##v_c_lst Rows: v(c), Columns different variables at play
    while HW_Row_more_than_one(matrix) == True: ##If there exist a row in matrix
        c = np.zeros(s*s).reshape(s, s)
        max_cij = 0
        max_cij_lst = []
        for j in range(1, s-1):
            for i in range(0, j):
                for row in range(m):
                    if Feasible_Update(matrix, goal_depth[row], depth_lst, s, i,j,row) == True:
                        c[i,j] += 1
                ##Keep a list of (i,j) such that it has the max number of rows such that Feasible Update holds.
                if max_cij == c[i,j]:
                    max_cij_lst.append((i,j))
                elif max_cij < c[i,j]:
                    max_cij_lst.clear()
                    max_cij = c[i,j]
                    max_cij_lst.append((i,j))
        besti, bestj = random.choice(max_cij_lst) ##Randomly pick (i,j) such that it has max number of rows such that Feasible_Update holds
        circuit_lst.append((besti,bestj))
        depth_s = max(depth_lst[besti],depth_lst[bestj])
        depth_lst.append(depth_s)
        for row in range(m):
            if Feasible_Update(matrix, goal_depth[row], depth_lst,s, besti,bestj,row)==True:
                matrix[row][besti] = 0
                matrix[row][bestj] = 0
                matrix[row].append(1)
            else:
                matrix[row].append(0)
        vector = np.bitwise_xor(v_c_lst[besti], v_c_lst[bestj])
        v_c_lst = np.append(v_c_lst, [vector], axis=0)
        s = s+1
    return matrix, v_c_lst, depth_lst, circuit_lst



matrix = [[1,0,1,1], [0,1,1,1], [1,1,1,1], [1,1,0,1]]
goal_depth = [2,3,4,3]
depth_lst = [0,2,1,0]
matrix, v_c_lst, depth_lst, circuit_lst = Rand_Greedy_Algorithm(matrix, goal_depth,depth_lst)
print("matrix: ")
Printmatrix(matrix)
print("v_c_lst: ")
print(v_c_lst)
print("depth_lst")
print(depth_lst)
print("circuit_lst")
print(circuit_lst)


# for row in range(m):
#     print(Feasible_Update(matrix, goal_depth[row], depth_lst, n+1, i, j, row))
#Feasible_Update(matrix, goal_depth[row], depth_lst, n+1, i, j, row)