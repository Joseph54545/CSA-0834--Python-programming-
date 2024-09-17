mat1 = [[1, 2], [5, 3]]
mat2 = [[2, 3], [4, 1]]

result = [[mat1[i][j] + mat2[i][j] for j in range(len(mat1[0]))] for i in range(len(mat1))]

for row in result:
    print(" ".join(map(str, row)))
