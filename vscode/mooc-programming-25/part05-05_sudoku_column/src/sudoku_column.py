# Write your solution here
def column_correct(sudoku: list, column_no: int):
    aux=[]
    rep=0
    for row in range(9):
        if sudoku[row][column_no]!=0:
            aux.append(sudoku[row][column_no])
    aux.sort()
    for i in range(len(aux)):
        if rep!=aux[i]:
            rep=aux[i]
        else:
            return False
    return True