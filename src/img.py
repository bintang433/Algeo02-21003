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

# {fungsi yang menghasilkan salinan suatu matriks}
def copyMatrix(Matrix):
    rowCopy = length(Matrix)
    colCopy = length(Matrix[0])
    copy = [[0 for j in range(colCopy)] for i in range(rowCopy)]
    for i in range(rowCopy):
        for j in range(colCopy):
            copy[i][j] = Matrix[i][j]
    return copy
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

# {fungsi yang menghasilkan matrix segitiga atas dari suatu matrix}
def intoUpperTriangle(Matrix):
    M = copyMatrix(Matrix)
    rowM = length(M)
    colM = length(M[0])
    def kurangBasis(row, rowBasis):
        for i in range(rowM):
            M[row][i] -= rowBasis[i]
    def tambahBasis(row, rowBasis):
        for i in range(colM):
            M[row][i] += rowBasis[i]
    def rowKaliConst(row, n):
        for i in range(colM):
            M[row][i] *= n
    def listKaliConst(list, n):
        for i in range(length(list)):
            list[i] *= n
    def swapRow(row1, row2):
        Mcopy = copyMatrix(M)
        for i in range(colM):
            M[row1][i] = Mcopy[row2][i]
            M[row2][i] = Mcopy[row1][i]
    for idxBasis in range(rowM-1):
        basis = [0 for i in range(colM)]
        # jika nilai basis diawali 0, tuker sama yang non 0
        if (M[idxBasis][idxBasis]==0):
            scanNot0 = idxBasis+1
            while (scanNot0 < rowM and M[scanNot0][idxBasis]==0):
                scanNot0+=1
            if (scanNot0>=rowM):
                continue
            else:
                swapRow(idxBasis,scanNot0)
        # mengisi basis dari baris yang dijadikan baris 1 utama
        for i in range(colM):
            basis[i] = M[idxBasis][i]/M[idxBasis][idxBasis]
        elimRow = idxBasis + 1
        while (elimRow<rowM):
            while (M[elimRow][idxBasis]!=0):
                if (M[elimRow][idxBasis]>0 and M[elimRow][idxBasis]<1):
                    pecahan = M[elimRow][idxBasis]
                    basisAdapt = [basis[i] for i in range(length(basis))]
                    listKaliConst(basisAdapt, pecahan)
                    kurangBasis(elimRow, basisAdapt)
                elif (M[elimRow][idxBasis]>0):
                    kurangBasis(elimRow, basis)
                elif (M[elimRow][idxBasis]<0):
                    tambahBasis(elimRow, basis)
            elimRow+=1
    return M

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

#test (mencari matrix kovarian)
# M1 = [
#     [2,0,1],
#     [1,2,0],
#     [0,2,4]
# ]
# M2 = [
#     [1,1,1],
#     [0,1,0],
#     [1,2,2]
# ]
# trainingMatrix = addMatrix(trainingMatrix,M1)
# trainingMatrix = addMatrix(trainingMatrix,M2)
# meanTrainingMatrix = kaliConstMatrix(trainingMatrix, 1/fileCount)   #menghitung mean matrix(?)
# A = concatMatrix(meanDiffM1, meanDiffM2)
# print("concat of meandiffs")
# printMatrix(A)
# C = multiplyMatrix(A, transpose(A))
# print("Kovarian")
# printMatrix(C)
# Mtest = [
#     [5,7],
#     [10,8]
# ]
# Mtest = [
#     [5,7,7],
#     [10,8,9],
#     [4,2,9]
# ]
# Mtest = [
#     [5,7,7,9],
#     [10,8,9,3],
#     [4,2,9,2],
#     [4,8,8,5]
# ]
Mtest = [
    [0,7,7,9,3,2],
    [0,8,9,3,4,7],
    [0,2,9,2,6,1],
    [0,8,8,5,4,1],
    [0,3,2,8,7,9],
    [0,8,7,11,4,10]
]
print("----Matrix awal----")
printMatrix(Mtest)
u = intoUpperTriangle(Mtest)
print("----Result----")
printMatrix(u)