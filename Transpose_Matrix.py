def transpose(matrix):    
    ## Creating another matrix & storing the transposed value
    m = len(matrix)
    n = len(matrix[0])

    result = list()
    for i in range(0,n):
        rows = []
        for j in range(0,m):
            rows.append(0)
        result.append(rows)
    
    for i in range(0,m):
        for j in range(0,len(matrix[i])):
            result[j][i] = matrix[i][j]
    return result

matrix = [[1,2,3],[4,5,6],[7,8,9]]

print(transpose(matrix))