import numpy as np
import random

class Color:
    GREEN  = '\033[32;1m'
    YELLOW = '\033[33;1m'
    END    = '\033[0m'

def matrix_read (path):
    file = open(path, "r")
    rows, cols = [int(x) for x in next(file).split()]
    A = np.zeros((rows, cols))
    for line in file:
        i, j, value = [np.float64(x) for x in line.split()]
        A[int(i-1)][int(j-1)] = value
    file.close()
    return A

def matrix_save (A, path):
    file = open(path, "w")
    file.write(str(len(A)) + " " + str(len(A[0])) + "\n")
    for i in range(len(A)):
        for j in range(len(A[0])):
            if (A[i][j] != 0):
                file.write(str(i+1) + " " + str(j+1) + " " + str(A[i][j]) + "\n")
    file.close()

def matrix_random (rows, cols, min, max):
    A = np.zeros((rows, cols))
    for i in range(len(A)):
        for j in range(len(A[0])):
            # A[i][j] = random.randint(min, max)
            A[i][j] = random.uniform(min, max)
    return A

def check (e):
    print("\nLendo matriz A...")
    A = matrix_read("matrix/A.txt")
    print("Lendo matriz B...")
    B = matrix_read("matrix/B.txt")
    print("Lendo matriz C...")
    C = matrix_read("matrix/C.txt")
    print("Multiplicando AB...")
    AB = np.dot(A, B)
    print("Comparando AB com C...")
    if (len(C) != len(AB) or len(C[0]) != len(AB[0])):
        print(Color.YELLOW + "Tamanho errado!\n" + Color.END)
        return
    for i in range(len(C)):
        for j in range(len(C[0])):
            if(abs(AB[i][j] - C[i][j]) > e):
                print(Color.YELLOW + "Valor errado!\n" + Color.END)
                return
    print(Color.GREEN + "Tudo certo!\n" + Color.END)

def main ():
    # check(1)
    matrix_save(matrix_random(1400, 1500, -100, 100), "matrix/A.txt")
    matrix_save(matrix_random(1500, 1600, -100, 100), "matrix/B.txt")

main()