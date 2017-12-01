import numpy as np

node1s = {}
allNodes = {}
dampingfactor = 0.85

def GetMatrix(size):
    matrix1 = np.zeros((size, size))
    for mat_row in range(0, size):
        node1 = mat_row + 1
        outlinks = allNodes[str(node1)]
        for mat_col in range(0, size):
            node2 = mat_col + 1
            if str(node2) in outlinks:
                no_of_outlinks = len(outlinks)
                matrix1[mat_row][mat_col] = 1.0/float(no_of_outlinks)
                
    return np.around(matrix1.transpose(),3)

def __init__(size):
    matrix2 = np.matrix((1.0/size) * np.ones((size, 1)))
    matrix2 = (1-dampingfactor)*matrix2
    vector = np.matrix((1.0/size) * np.ones((size, 1)))
    return(matrix2, vector)

def ComputePageRank(matrix1, matrix2, vector):
        iterationCount = 1
        rank = np.matrix(dampingfactor * matrix1 * vector + matrix2)
        while not (sum(abs(rank-vector))) <= 0.001:
            vector = rank
            rank = np.matrix(dampingfactor * matrix1 * vector + matrix2)
            iterationCount = iterationCount + 1
        return(iterationCount, vector)

def GetAllNodes():
    f = input("Enter path to the graph of number format text file")
    with open(f, 'r') as file:
        for line in file:
            i, j, k = line.split(" ")
            if i in node1s:
                node1s.get(i).append(j)
            else:
                node1s[i] = []
                node1s[i].append(j)

    allNodes = node1s.copy() 
    
    for key in node1s.keys():
        outlinks = node1s.get(key)
        for val in outlinks:
            if not val in node1s.keys():
                allNodes[val] = []
    
    return allNodes

allNodes = GetAllNodes()
size = len(allNodes)

matrix1= GetMatrix(size)

matrix2, vector = __init__(size)

total_iterations, R = ComputePageRank(matrix1, matrix2, vector)

print("a) Matrix M\n" , matrix1)
print("b) Original rank vector (rj)\n", vector)
print("c) Converged rank vector (R)\n " , R)
print("d) No of iterations required " , total_iterations)

