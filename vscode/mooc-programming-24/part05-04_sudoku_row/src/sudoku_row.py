# Write your solution here
def row_correct(sudoku: list, row_no: int):
    aux=[]
    rep=0
    for i in range(len(sudoku[row_no])):
        if sudoku[row_no][i]!=0:
            aux.append(sudoku[row_no][i])
    aux.sort()
    for i in range(len(aux)):
        if rep!=aux[i]:
            rep=aux[i]
        else:
            return False
    return True
