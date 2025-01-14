
def sudoku_grid_correct(sudoku: list):
    
    
    # Verificação das linhas
    for row in range(len(sudoku)):
        rep = 0
        aux = []
        for column in range(len(sudoku[row])):
            if sudoku[row][column] != 0:
                aux.append(sudoku[row][column])
        aux.sort()
        for i in range(len(aux)):
            if rep != aux[i]:
                rep = aux[i]
            else:
                return False
            
    # Verificação das colunas
    for column in range(len(sudoku)):
        rep = 0
        aux = []
        for row in range(len(sudoku)):
            if sudoku[row][column] != 0:
                aux.append(sudoku[row][column])
        aux.sort()
        for i in range(len(aux)):
            if rep != aux[i]:
                rep = aux[i]
            else:
                return False
            
    # Verificação das subgrades 3x3
    for box_row in range(0, 9, 3):
        rep = 0
        for box_col in range(0, 9, 3):
            aux = []
            for i in range(3):
                for j in range(3):
                    if sudoku[box_row + i][box_col + j] != 0:
                        aux.append(sudoku[box_row + i][box_col + j])
            aux.sort()
            for i in range(len(aux)):
                if rep != aux[i]:
                    rep = aux[i]
                else:
                    return False
    
    return True