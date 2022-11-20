from PIL import Image
import numpy as np
import os
from numpy import *

# Operator matrix
# {Prosedur membuat matrix 0 dengan ukuran baris row dan kolom col}
def createMatrix(row, col):
    Matrix = [[0 for i in range(col)] for j in range(row)]
    return Matrix
def createIdentity(row,col):
    Matrix = createMatrix(row,col)
    for i in range(row):
        for j in range(col):
            if (i==j):
                Matrix[i][j] = 1
    return Matrix

# {fungsi yang mengembalikan length suatu list}
def length(list):
    l = list
    ctr = 0
    for i in l:
        ctr+=1
    return ctr

# {Fungsi selektor 1 baris suatu Matrix}
def getRow(Matrix, row, asList):
    col = length(Matrix[0])
    result = createMatrix(1, col)
    for i in range(col):
        result[0][i] = Matrix[row][i]
    if (asList):
        return result[0]
    else : 
        return result

# {Fungsi selektor 1 kolom suatu Matrix}
def getCol(Matrix, col, asList):
    row = length(Matrix)
    result = createMatrix(row, 1)
    for i in range(row):
        result[i][0] = Matrix[i][col]
    if (asList):
        return transpose(result)[0]
    else:
        return result

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
    M = createMatrix(row,col)
    for i in range(row):
        for j in range(col):
            M[i][j] = Matrix1[i][j] + Matrix2[i][j]
    return M

# {fungsi yang mengembalikan pengurangan matrix dari Matrix1 dan Matrix2}
def subtractMatrix(Matrix1, Matrix2):
    row = length(Matrix1)
    col = length(Matrix1[0])
    M = createMatrix(row, col)
    for i in range(row):
        for j in range(col):
            M[i][j] = Matrix1[i][j] - Matrix2[i][j]
    return M

# {fungsi yang mengembalikan matriks Md yang dikali konstanta n}
def multiplyByConstMatrix(Matrix, n):
    row = length(Matrix)
    col = length(Matrix[0])
    M = createMatrix(row, col)
    for i in range(row):
        for j in range(col):
            M[i][j] = Matrix[i][j] * n
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

# Operasi baris matrix
# {fungsi yang mengurangkan row1 dengan row2}
def addRow(row1, row2):
    l = length(row1)
    result = [0 for i in range(l)]
    for i in range(l):
        result[i] = row1[i] + row2[i]
    return result
# {fungsi yang menjumlahkan row1 dengan row2}
def subtractRow(row1, row2):
    l = length(row1)
    result = [0 for i in range(l)]
    for i in range(l):
        result[i] = row1[i] - row2[i]
    return result
# {fungsi yang mengalikan row dengan n}
def multiplyByConstRow(baris, n):
    l = length(baris)
    result = [0 for i in range(l)]
    for i in range(l):
        result[i] = baris[i] * n
    return result
# def swapRow(M, row1, row2):
#     colM = length(M[0])
#     Mcopy = copyMatrix(M)               #inefficent for image matrices, if fixing, make copy of row instead of matrix
#     for i in range(colM):
#         M[row1][i] = Mcopy[row2][i]
#         M[row2][i] = Mcopy[row1][i]

# Operasi vektor
# {fungsi selektor matrix untuk mendapatkan 1 vektor dr matrix}
def getVector(Matrix, col):
    row = length(Matrix)
    result = [0 for i in range(row)]
    for i in range(row):
        result[i] = Matrix[i][col]
    return result

# {fungsi yang menghasilkan penjumlahan dua vektor u dan vektor v}
def addVector(u, v):
    l = length(u)
    result = [0 for i in range(l)]
    for i in range(l):
        result[i] = u[i] + v[i]
    return result

# {fungsi yang menghasilkan pengurangan dua vektor u dan vektor v}
def subtractVector(u, v):
    l = length(u)
    result = [0 for i in range(l)]
    for i in range(l):
        result[i] = u[i] - v[i]
    return result

# {fungsi yang menghasilkan product dari 2 vektor}
def productVector(u, v):
    result = 0
    for i in range(length(u)):
        result += u[i] * v[i]
    return result

# {fungsi yang mengalikan vektor u dengan skalar n}
def scaleVector(u, n):
    l = length(u)
    result = [0 for i in range(l)]
    for i in range(l):
        result[i] = u[i] * n
    return result

# {fungsi yang mengembalikan magnitude vektor u}
def magnitudeVector(u):
    result = 0
    for i in range(length(u)):
        result += u[i]*u[i]
    return (result**0.5)

# {fungsi yang mengembalikan proyeksi vektor u pada v}
def orthoProjectVector(u, v):
    return (scaleVector(u, productVector(u,v)/productVector(u,u)))

# {fungsi yang menghasilkan dekomposisi QR dari suatu matrix}
def QR(Matrix):
    Q = copyMatrix(Matrix)
    row = length(Matrix)
    col = length(Matrix[0])
    for j in range(col):
        u = getVector(Q, j)
        v = getVector(Q, j)
        for k in range(j-1,0-1,-1):
            uk = getVector(Q, k)
            u = subtractVector(u, orthoProjectVector(uk,v))
        for i in range(col):
            Q[i][j] = u[i] / magnitudeVector(u)
    temp = multiplyMatrix(transpose(Q),Matrix)
    R = createMatrix(row, col)
    for i in range(row):
        for j in range(row):
            if (j >= i):
                R[i][j] = temp[i][j]
    return Q,R

# {fungsi yang menghasilkan nilai-nilai eigen suatu matrix dengan dekomposisi QR, dengan suatu banyak iterasi}
def eigenvalue(Matrix, iteration):
    M = copyMatrix(Matrix)
    l = length(Matrix)
    result = [0 for i in range(l)]
    for i in range(iteration):
        [Q,R] = QR(M)
        M = multiplyMatrix(R,Q)
    for i in range(l):
        result[i] = M[i][i]
    return result

# {fungsi yang menghasilkan nilai vektor-vektor eigen Matrix}
def eigenvector(Matrix, EigenVal):
    result = []
    for i in range(length(EigenVal)):
        tempMat = copyMatrix(Matrix)
        tempEigVal = [EigenVal[i] for j in range(length(EigenVal))]
        for j in range(length(EigenVal)):
            tempMat[j][j] -= tempEigVal[j]
        EigVec = np.linalg.solve(tempMat, tempEigVal)
        norm = magnitudeVector(EigVec)
        for j in range(length(EigVec)):
            EigVec[j] /= norm
        result.append(EigVec)
    return result

# Operator Image
# {mengakses semua image di dalam image dan mengeluarkan matrix grayscale yang diresize}
def accessImage (folder):
    for (root,dirs,files) in os.walk(folder, topdown=True):
        for i in files:
            directory = root + "\\" + i
            image = Image.open(directory,mode='r').convert('L').resize([256,256])
            ar = np.array(image)
            matrix = asarray(ar)                #matrix = masing-masing gambar dalam bentuk matrix
            # print(matrix)

# {fungsi yang mengakses dataset, mengubah image-image menjadi ukuran tertentu, grayscale dan menjadi 1 baris, lalu mengonkatenasi semuanya untuk diproses}
def datasetToArray (folder):
    result = []
    for (root,dirs,files) in os.walk(folder, topdown=True):
        for i in files:
            directory = root + "\\" + i
            image = Image.open(directory,mode='r').convert('L').resize([256,256])
            ar = np.array(image)
            matrix = asarray(ar)
            result.append(intoOneRow(matrix)[0])
    return result
# {fungsi yang mengakses dataset, mengubah image-image menjadi ukuran tertentu, grayscale dan menjadi 1 baris, lalu mengonkatenasi semuanya untuk diproses}
# {fungsi ini sama dengan dataSetToArray() tapi menambahkan batasan jumlah foto}
# {untuk tidak membatasi banyak matrix yang dihasilkan, amount diinput -1}
def datasetToArray_FixedAmount (folder, amount):
    result = []
    ctr=0
    for (root,dirs,files) in os.walk(folder, topdown=True):
        for i in files:
            if ctr>=amount and ctr>=0:
                break
            directory = root + "\\" + i
            image = Image.open(directory,mode='r').convert('L').resize([256,256])
            ar = np.array(image)
            matrix = asarray(ar)
            result.append(intoOneRow(matrix)[0])
            ctr+=1
        ctr=0
    return result

# {menghitung jumlah file}
def numberOfImage (folder):
    sum = 0
    for (root,dirs,files) in os.walk(folder, topdown=True):
        for i in files:
            sum+=1
    return sum

#{fungsi yang mengembalikan matrix kovarian dari suatu matrix}
def covariant (Matrix):
    ds2A = copyMatrix(Matrix)
    #menjumlahkan data-data
    mean = getRow(ds2A, 0, True)
    for i in range(1,length(ds2A)):
        mean = addRow(mean,getRow(ds2A, i, True))
    #ds2A dibagi banyak data
    mean = multiplyByConstRow(mean, 1/length(ds2A))
    #dari sini sudah diperoleh nilai mean dari row-row
    #mengurangi row-row dengan mean
    for i in range(length(ds2A)):
        ds2A[i] = subtractRow(getRow(ds2A, i, True), mean)
    #mendapatkan matrix kovarian
    result = multiplyMatrix(ds2A, transpose(ds2A))
    return result