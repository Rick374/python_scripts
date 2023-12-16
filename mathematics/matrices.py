#!/usr/bin/env python3
import numpy as np
import argparse

class Matrix:
    def __init__(self, n_of_rows, n_of_columns):
        self.r = n_of_rows
        self.c = n_of_columns
        self.matrix = np.zeros((self.r, self.c))

    def inputElements(self):
        for i in range(self.r):
            for j in range(self.c):
                self.matrix[i, j] = float(input("Ingresa el elemento "+str(i+1)+","+str(j+1)+" : "))

    def displayMatrix(self):
        print("\nLa matriz ingresada es: ")
        print(self.matrix)

    def calcCofactor(self):
        """Calcula la matriz de cofactores"""
        sel_rows = np.ones(self.matrix.shape[0], dtype=bool)
        sel_columns = np.ones(self.matrix.shape[1], dtype=bool)
        CO = np.zeros_like(self.matrix)
        sgn_row = 1
        for row in range(self.matrix.shape[0]):
            sel_rows[row] = False
            sgn_col = 1
            for col in range(self.matrix.shape[1]):
                sel_columns[col] = False
                MATij = self.matrix[sel_rows][:, sel_columns]
                CO[row, col] = sgn_row * sgn_col * np.linalg.det(MATij)
                sel_columns[col] = True
                sgn_col = -sgn_col
            sel_rows[row] = True
            sgn_row = -sgn_row
        return CO

    def calcAdjugate(self):
        """Calcula la matriz adjunta"""
        print("Matriz Adjunta: ")
        print(self.calcCofactor().T)

    def calcDet(self):
        """Calcula el determinante de la matriz"""
        print("Determinante de la Matriz Ingresada: ")
        print(np.linalg.det(self.matrix))

    def calcInv(self):
        """Calcula matriz inversa"""
        print("Inversa de la Matriz Ingresada: ")
        print(np.linalg.inv(self.matrix))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('n_of_rows_a', type=int, help='Ingresar el numero de filas de la primera matriz')
    parser.add_argument('n_of_columns_a', type=int, help='Ingresar el numero de columnas de la  primera matriz')
    parser.add_argument('n_of_rows_b', nargs='?', default=None, type=int, help='Ingresar el numero de filas de la segunda matriz')
    parser.add_argument('n_of_columns_b', nargs='?', default=None, type=int, help='Ingresar el numero de columnas de la segunda matriz')
    args = parser.parse_args()
    matrix_a = Matrix(args.n_of_rows_a, args.n_of_columns_a)
    # matrix_b = Matrix(args.n_of_rows_b, args.n_of_columns_b)
    matrix_a.inputElements()
    # matrix_b.inputElements()
    matrix_a.displayMatrix()
    matrix_a.calcAdjugate()
    matrix_a.calcDet()
    matrix_a.calcInv()
