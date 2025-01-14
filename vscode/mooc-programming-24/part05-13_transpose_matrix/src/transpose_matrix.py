# Write your solution here
def transpose(matrix: list):
    new_list=[row[:] for row in matrix]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j]=new_list[j][i]

