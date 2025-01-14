# Write your solution here
def print_sudoku(sudoku: list):
    for i in range(len(sudoku)):
        if i%3==0:
            print()
        for j in range(len(sudoku[i])):
            if sudoku[i][j]==0:
                if j%3!=0 or j==0:
                    print("_ ", end="")
                else:
                    print(" _ ", end="")
            else:
                if j%3==0 and j!=0:
                    print(" ", end="")
                print(sudoku[i][j], end=" ")
        print()

def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):
    # Cria uma cópia profunda da lista sudoku
    new_list = [row[:] for row in sudoku]
    # Modifica o elemento desejado
    new_list[row_no][column_no] = number
    return new_list

