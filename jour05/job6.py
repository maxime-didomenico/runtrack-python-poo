def init_tab(n):
    list = [[0 for j in range(n)] for i in range(n)]
    return list

def print_tab(tab):
    for i in range(len(tab)):
        for j in range(len(tab)):
            print(tab[i][j], end=" ")
        print()

def lineAreSafe(tab, x, y):
    i = 0
    while i < len(tab):
        if (tab[x][i] == 1 or tab[x][i] == 2) or (tab[i][y] == 1 or tab[i][y] == 2):
            return False
        i += 1
    return True

def diagonalAreSafe(tab, x, y):
    i = x
    j = y
    while i >= 0 and j >= 0:
        if tab[i][j] == 1 or tab[i][j] == 2:
            return False
        i -= 1
        j -= 1

    i = x
    j = y
    while i < len(tab) and j < len(tab):
        if tab[i][j] == 1 or tab[i][j] == 2:
            return False
        i += 1
        j += 1

    i = x
    j = y
    while i >= 0 and j < len(tab):
        if tab[i][j] == 1 or tab[i][j] == 2:
            return False
        i -= 1
        j += 1

    i = x
    j = y
    while i < len(tab) and j >= 0:
        if tab[i][j] == 1 or tab[i][j] == 2:
            return False
        i += 1
        j -= 1

    return True

def printQueenLine(tab, x, y):
    i = 0
    while i < len(tab):
        tab[x][i] = 1
        tab[i][y] = 1
        i += 1
    i = 0

def printDiagonal(tab, x, y):
    i = x-1
    j = y-1
    while i >= 0 and j >= 0:
        tab[i][j] = 1
        i -= 1
        j -= 1

    i = x+1
    j = y+1
    while i < len(tab) and j < len(tab):
        tab[i][j] = 1
        i += 1
        j += 1

    i = x-1
    j = y+1
    while i >= 0 and j < len(tab):
        tab[i][j] = 1
        i -= 1
        j += 1

    i = x+1
    j = y-1
    while i < len(tab) and j >= 0:
        tab[i][j] = 1
        i += 1
        j -= 1

def placeQueen(tab):
    i = 0
    j = 0

    while i < len(tab):
        while j < len(tab):
            if tab[i][j] == 0:
                printQueenLine(tab, i, j)
                printDiagonal(tab, i, j)
                tab[i][j] = 2
            j += 1
        i += 1
        j = 0

def changeTab(tab):
    i = 0
    j = 0
    while i < len(tab):
        while j < len(tab):
            if tab[i][j] == 1 or tab[i][j] == 0:
                tab[i][j] = 'O'
            elif tab[i][j] == 2:
                tab[i][j] = 'X'
            j += 1
        i += 1
        j = 0

def main():
    n = int(input("Entrez le nombre de dames : "))
    board = init_tab(n)
    placeQueen(board)
    #changeTab(board)
    print_tab(board)

main()
print(" ")