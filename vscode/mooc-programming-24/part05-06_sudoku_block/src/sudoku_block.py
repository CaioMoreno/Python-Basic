# Write your solution here
def block_correct(sudoku: list, row_no: int, column_no: int):
    aux=[]
    rep=0
    row=row_no
    for row in range(row_no, row_no+3):
        column=column_no
        for column in range(column_no, column_no+3):
            if sudoku[row][column]!=0:
                aux.append(sudoku[row][column])
    aux.sort()
    for i in range(len(aux)):
        if rep!=aux[i]:
            rep=aux[i]
        else:
            return False
    return True

