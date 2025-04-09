import random

totalGrid = 0

def parseInput():
    global totalGrid
    rowN = int(input("Enter the number of rows: "))
    while rowN < 1:
        print("ERROR: Invalid Row Number input!")
        rowN = int(input("Re-Enter the number of rows: "))

    colN = int(input("Enter the number of cols: "))
    while colN < 1:
        print("ERROR: Invalid Col Number input!")
        colN = int(input("Re-Enter the number of cols: "))

    totalGrid = rowN * colN

    mineN = int(input("Enter the number of mines: "))
    while mineN > totalGrid:
        print("ERROR: Invalid mine input!")
        mineN = int(input("Re-Enter the number of mines: "))
    return mineN, rowN, colN


def mineOrNot(remainingMine):
    probability = (totalGrid-remainingMine) / totalGrid
    return random.uniform(0, 1) <= probability

def createMatrix(n, row, col):
    # Initilize a matrix of rowN x coln with `.`
    matrix = [[ "." for i in range(col) ] for j in range(row)]
    counter = 0
    while counter < n:
        for r in range(0, row):
            for c in range(0, col):
                if not mineOrNot(n-counter) and counter != n:
                    matrix[r][c] = "*"
                    counter += 1
                if counter == n:
                    return matrix

def writeMatrix(matrix, fileName="mine.txt"):
    with open(fileName, 'w') as file:
        for row in matrix:
            file.write(' '.join([str(item) for item in row]))
            file.write('\n')

mineN, rowN, colN = parseInput()

writeMatrix(createMatrix(mineN, rowN, colN))