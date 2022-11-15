from PIL import Image
import numpy as np
import os
from numpy import *

# Operator matrix
# {Prosedur membuat matrix 0 dengan ukuran baris row dan kolom col}
def createMatrix(row, col):
    Matrix = [[0 for i in range(col)] for j in range(row)]
    return Matrix

def length(list):
    l = list
    ctr = 0
    for i in l:
        ctr+=1
    return ctr

# {Prosedur print matrix}
def printMatrix(Matrix):
    row = length(Matrix)
    col = length(Matrix[0])
    for i in range(row):
        print("[", end="")
        for j in range(col):
            print(Matrix[i][j], end="")
            if (j < col-1):
                print(",", end='')
        print("]", end="")
        print()

# {fungsi yang mengembalikan penjumlahan matrix dari Matrix1 dan Matrix2}
def addMatrix(Matrix1, Matrix2):
    row = length(Matrix1)
    col = length(Matrix1[0])
    M = Matrix1
    for i in row:
        for j in col:
            M[i][j] += Matrix2[i][j]
    return M

# {fungsi yang mengembalikan pengurangan matrix dari Matrix1 dan Matrix2}
def subtractMatrix(Matrix1, Matrix2):
    row = length(Matrix1)
    col = length(Matrix1[0])
    M = Matrix1
    for i in row:
        for j in col:
            M[i][j] -= Matrix2[i][j]
    return M

# {fungsi yang mengembalikan matriks Md yang dikali konstanta n}
def kaliConstMatrix(Matrix, n):
    row = length(Matrix)
    col = length(Matrix[0])
    M = Matrix
    for i in row:
        for j in col:
            M[i][j] *= n
    return M

# {fungsi yang mengembalikan perkalian matrix Matrix1 dan Matrix2}
def multiplyMatrix(Matrix1, Matrix2):
    result = createMatrix(length(Matrix1), length(Matrix2[0]))
    row = length(result)
    col = length(result[0])
    colM1 = length(Matrix1[0])
    for i in range(row):
        for j in range(col):
            result[i][j] = 0
            for l in range(colM1):
                result[i][j] += Matrix1[i][l]*Matrix2[l][j]
    return result

# {fungsi yang mengembalikan transpose matrix}
def transpose(Matrix):
    #Mtr = M yang ditranspose
    #row Mtr = col M, col Mtr = row M
    row = length(Matrix)
    col = length(Matrix[0])
    M = Matrix
    Mtr = createMatrix(col, row)
    temp = [0 for i in range(col)]
    for i in range(row):
        for j in range(col):
            temp[j] = M[i][j]
        for k in range(col):
            Mtr[k][i] = temp[k]
    return Mtr

# {fungsi yang mengembalikan konkatenasi dari 2 matrix atau 
# lebih tepatnya menghasilkan matrix1 diaugmentasi dengan matrix2}
def concatMatrix(Matrix1, Matrix2):
    M1 = Matrix1
    M2 = Matrix2
    resultCol = length(M1[0])+length(M2[0])
    rowM1 = length(M1)
    colM1 = length(M1[0])
    result = createMatrix(rowM1, resultCol)
    for i in range(rowM1):
        for j in range(resultCol):
            if (j<colM1):
                result[i][j] = M1[i][j]
            else :
                result[i][j] = M2[i][j-colM1]
    return result

# {fungsi yang mengembalikan suatu matrix yang dijadikan 1 baris dengan konkatenasi}
def intoOneRow(Matrix):
    row = length(Matrix)
    oneRow = [Matrix[0]]
    for i in range(1,row):
        oneRow = concatMatrix(oneRow, [Matrix[i]])
    return oneRow
# {fungsi yang mengembalikan suatu matrix yang dijadikan 1 kolom dengan konkatenasi dan transpose}
def intoOneCol(Matrix):
    return transpose(intoOneRow(Matrix))

# w dan h adalah width dan height gambar dalam pixel-pixel
# def search (folder):
#     images = [file for file in os.listdir(ui.folder) if file.endswith(('jpeg', 'png', 'jpg'))]
#     for img in images:
#         image = Image.open(img)
#         print(f"Original size : {image.size}")
#         pixel=image.load()

#         image_grayscale= image.convert('L')
#         test_resized = image_grayscale.resize((256, 256))
#         # test_resized.save('test_resized.jpg')
#         test_resized.show()

#         np_resized = np.array(test_resized)
#         print("Ukuran barunya:",np_resized.shape)

#         numpydata = asarray(test_resized)
#         print("Matriks numpy:",numpydata)

def searchImg (folder):
    for (root,dirs,files) in os.walk(folder, topdown=True):
        print ("|------------------------------------------|")
        print ("|                                          |")
        print (root)
        print ("|                                          |")
        print ("|------------------------------------------|")
        print (files)

# height = 256
# width = 256
# Matrix = createMatrix(height, width)

# fileCount = 0                               #untuk menghitung jumlah file jadi harusnya seukuran M. Ini hanya untuk contoh
# for i in range(M):
#     addMatrix(trainingMatrix, numpydata) #matrix-matrix dijumlahkan
#     fileCount+=1
# meanTrainingMatrix = kaliConstMatrix(trainingMatrix, 1/fileCount, 540, 540)   #menghitung mean matrix(?)