# Write your solution here
def row_sums(my_matrix: list):
    for i in range(len(my_matrix)):
        new_n=sum(my_matrix[i])
        my_matrix[i].append(new_n)

