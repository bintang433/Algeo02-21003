from PIL import Image
import numpy as np
import os
from numpy import *
from matplotlib import pyplot as plt
import cv2 

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

# {Fungsi selektor 1 baris suatu Matrix}
# asList False akan mengembalikan matrix dimensi 1xCol yang merupakan baris matrix dengan index row
def getRow(Matrix, row, asList):
    col = len(Matrix[0])
    result = createMatrix(1, col)
    for i in range(col):
        result[0][i] = Matrix[row][i]
    if (asList):
        return result[0]
    else : 
        return result

# {Fungsi selektor 1 kolom suatu Matrix}
# asList False akan mengembalikan matrix dimensi Rowx1 yang merupakan kolom matrix dengan index col
def getCol(Matrix, col, asList):
    row = len(Matrix)
    result = createMatrix(row, 1)
    for i in range(row):
        result[i][0] = Matrix[i][col]
    if (asList):
        return transpose(result)[0]
    else:
        return result

# {fungsi yang menghasilkan salinan suatu matriks}
def copyMatrix(Matrix):
    rowCopy = len(Matrix)
    colCopy = len(Matrix[0])
    copy = [[0 for j in range(colCopy)] for i in range(rowCopy)]
    for i in range(rowCopy):
        for j in range(colCopy):
            copy[i][j] = Matrix[i][j]
    return copy

# {Prosedur print matrix}
def printMatrix(Matrix):
    row = len(Matrix)
    col = len(Matrix[0])
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
    result = np.add(Matrix1, Matrix2)
    return result

# {fungsi yang mengembalikan pengurangan matrix dari Matrix1 dan Matrix2}
def subtractMatrix(Matrix1, Matrix2):
    result = np.subtract(Matrix1, Matrix2)
    return result

# {fungsi yang mengembalikan matriks Md yang dikali konstanta n}
def multiplyByConstMatrix(Matrix, n):
    result = np.array(Matrix) * n
    return result

# {fungsi yang mengembalikan perkalian matrix Matrix1 dan Matrix2}
def multiplyMatrix(Matrix1, Matrix2):
    result = np.matmul(Matrix1, Matrix2)
    return result

# {fungsi yang mengembalikan hasil kali Matrix1 dan Matrix2 dan dibentuk menjadi matrix ukuran }
def reshapeMultiply(Matrix1, Matrix2, row, col):
    np.array(Matrix1).reshape(row,col)
    result = multiplyMatrix(Matrix1, Matrix2)
    return result

# {fungsi yang mengembalikan transpose matrix}
# fungsi ini menerima matrix lalu mengembalikan hasil transpose matrix tersebut
def transpose(Matrix):
    #Mtr = M yang ditranspose
    #row Mtr = col M, col Mtr = row M
    row = len(Matrix)
    col = len(Matrix[0])
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
    resultCol = len(M1[0])+len(M2[0])
    rowM1 = len(M1)
    colM1 = len(M1[0])
    result = createMatrix(rowM1, resultCol)
    for i in range(rowM1):
        for j in range(resultCol):
            if (j<colM1):
                result[i][j] = M1[i][j]
            else :
                result[i][j] = M2[i][j-colM1]
    return result

# {fungsi yang mengembalikan suatu matrix yang dijadikan 1 baris dengan konkatenasi}
# hasil yang dikembalikan adalah matrix berdimensi 1xCol yang merupakan seluruh elemen matrix yang dijadikan satu baris
def intoOneRow(Matrix):
    oneRow = [np.array(Matrix).flatten()]
    return oneRow
# {fungsi yang mengembalikan suatu matrix yang dijadikan 1 kolom dengan konkatenasi dan transpose}
def intoOneCol(Matrix):
    return transpose(intoOneRow(Matrix))

# Operasi baris matrix
# baris : 1 baris matrix yang dijadikan array (1 dimensi)
# gunakan getRow dengan parameter asList true
# {fungsi yang mengurangkan row1 dengan row2}
def addRow(row1, row2):
    result = np.add(row1,row2)
    return result
# {fungsi yang menjumlahkan row1 dengan row2}
def subtractRow(row1, row2):
    result = np.subtract(row1,row2)
    return result
# {fungsi yang mengalikan row dengan n}
def multiplyByConstRow(baris, n):
    result = np.array(baris) * n
    return result
# def swapRow(M, row1, row2):
#     colM = len(M[0])
#     Mcopy = copyMatrix(M)               #inefficent for image matrices, if fixing, make copy of row instead of matrix
#     for i in range(colM):
#         M[row1][i] = Mcopy[row2][i]
#         M[row2][i] = Mcopy[row1][i]

# Operasi vektor
# Vektor : 1 kolom matrix yang dijadikan array (1 dimensi)
# {fungsi selektor matrix untuk mendapatkan 1 vektor dr matrix}
def getVector(Matrix, col):
    row = len(Matrix)
    result = [0 for i in range(row)]
    for i in range(row):
        result[i] = Matrix[i][col]
    return result

# {fungsi yang menghasilkan penjumlahan dua vektor u dan vektor v}
def addVector(u, v):
    result = np.add(u,v)
    return result

# {fungsi yang menghasilkan pengurangan dua vektor u dan vektor v}
def subtractVector(u, v):
    result = np.subtract(u,v)
    return result

# {fungsi yang menghasilkan product dari 2 vektor}
def dotProductVector(u, v):
    result = np.dot(u,v)
    return result

# {fungsi yang mengalikan vektor u dengan skalar n}
def scaleVector(u, n):
    result = np.array(u)*n
    return result

# {fungsi yang mengembalikan magnitude vektor u}
def magnitudeVector(u):
    result = 0
    for i in range(len(u)):
        result += u[i]*u[i]
    return (sqrt(result))

# {return magnitude matrix m, sqrt(sum(sum(i**2 for i in j) for j in matrix))}
def magnitudeMatrix(m):
    result = 0
    for i in range(len(m)):
        for j in range(len(i)):
            result += m[i][j]**2
    return result**0.5

# {fungsi yang mengembalikan proyeksi vektor u pada v}
def orthoProjectVector(u, v):
    return (scaleVector(u, dotProductVector(u,v)/dotProductVector(u,u)))

# {fungsi yang menghasilkan dekomposisi QR dari suatu matrix}
def QR(Matrix):
    Q = copyMatrix(Matrix)
    row = len(Matrix)
    col = len(Matrix[0])
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
    l = len(Matrix)
    result = [0 for i in range(l)]
    for i in range(iteration):
        print("eigenValue iteration: {} of {}".format(i+1, iteration))
        [Q,R] = QR(M)
        M = multiplyMatrix(R,Q)
    for i in range(l):
        result[i] = M[i][i]
    result.sort(reverse=True)
    return result

# {fungsi yang menghasilkan nilai vektor-vektor eigen Matrix}
def eigenvector(Matrix, EigenVal):
    result = []
    for i in range(len(EigenVal)):
        tempMat = copyMatrix(Matrix)
        tempEigVal = [EigenVal[i] for j in range(len(EigenVal))]
        for j in range(len(EigenVal)):
            tempMat[j][j] -= tempEigVal[j]
        EigVec = np.linalg.solve(tempMat, tempEigVal)
        norm = magnitudeVector(EigVec)
        # for j in range(len(EigVec)):
        #     EigVec[j] /= norm
        result.append(EigVec)
    return result

# {fungsi copy matrix 3D}
def copyMatrix3D (Matrix3D):
    col = len(Matrix3D[0][0])
    row = len(Matrix3D[0])
    depth = len(Matrix3D)
    result = [[[0 for j in range(col)] for i in range(row)] for k in range(depth)]
    for k in range(depth):
        for i in range(row):
            for j in range(col):
                result[k][i][j] = Matrix3D[k][i][j]
    return result

# Operator Image
# {mengakses semua image di dalam image dan mengeluarkan matrix grayscale yang diresize}
def accessImage (folder):
    tempImg = cv2.imread(folder, cv2.IMREAD_GRAYSCALE)
    image = cv2.resize(tempImg, [256, 256])
    ar = np.array(image)
    matrix = asarray(ar)                #matrix = masing-masing gambar dalam bentuk matrix
    matrix = intoOneCol(matrix)
    return matrix
# def accessImage (folder):
#     for (root,dirs,files) in os.walk(folder, topdown=True):
#         for i in files:
#             directory = root + "\\" + i
#             image = Image.open(directory,mode='r').convert('L').resize([256,256])
#             ar = np.array(image)
#             matrix = asarray(ar)                #matrix = masing-masing gambar dalam bentuk matrix
#             # print(matrix)

# {fungsi yang mengakses dataset, mengubah image-image menjadi ukuran tertentu, grayscale dan menjadi 1 baris, lalu mengonkatenasi semuanya untuk diproses}
def datasetToArray (folder):
    result = []
    for (root,dirs,files) in os.walk(folder, topdown=True):
        for i in files:
            directory = root + "\\" + i
            tempImg = cv2.imread(directory, cv2.IMREAD_GRAYSCALE)
            image = cv2.resize(tempImg, [256, 256])
            ar = np.array(image)
            matrix = asarray(ar)
            result.append(matrix)
    return result
# {fungsi yang mengakses dataset, mengubah image-image menjadi ukuran tertentu, grayscale dan menjadi 1 baris, lalu mengonkatenasi semuanya untuk diproses}
# {fungsi ini sama dengan dataSetToArray() tapi menambahkan batasan jumlah foto}
# {untuk tidak membatasi banyak matrix yang dihasilkan, amount diinput -1}
def datasetToArray_FixedAmount (folder, amount):
    result = []
    ctr=0
    for (root,dirs,files) in os.walk(folder, topdown=True):
        for i in files:
            if ctr>=amount and amount>=0:
                break
            directory = root + "\\" + i
            tempImg = cv2.imread(directory, cv2.IMREAD_GRAYSCALE)
            image = cv2.resize(tempImg, [256, 256])
            ar = np.array(image)
            matrix = asarray(ar)
            result.append(matrix)
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
def deltaMeanAndCovariant (Matrix3D):
    dataset = copyMatrix3D(Matrix3D)
    depth = len(Matrix3D)
    row = len(Matrix3D[0])
    col = len(Matrix3D[0][0])
    delta = []
    #flatten matrix 3D
    for i in range(depth):
        temp = np.array(dataset[i]).flatten()
        delta.append(temp)
    #menjumlahkan data-data
    mean = [0 for j in range(col*row)]
    for i in range(depth):
        mean = addRow(mean, delta[i])

    #delta dibagi banyak data
    mean = multiplyByConstRow(mean, 1/depth)
    meanVector = [mean]
    print("Achieved mean of matrices")
    #dari sini sudah diperoleh nilai mean dari row-row
    #mengurangi row-row dengan mean
    for i in range(depth):
        delta[i] = subtractRow(delta[i], mean)
    print("Achieved delta mean")
    #dari sini delta adalah berukuran baris banyak file kolom resolusi**2
    #mendapatkan matrix kovarian
    cov = multiplyMatrix(delta, transpose(delta))
    # cov = multiplyMatrix(delta, transpose(delta))
    print("Achieved covariance matrix")
    #ukuran matrix kovarian: banyak file x banyak file
    return transpose(delta), transpose(meanVector), cov

def eigenFaces(eigenVectors, deltaMean):
    eigFaces = []
    for i in range(len(eigenVectors[0])):
        col = getCol(eigenVectors, i, False)
        temp = getRow(transpose(multiplyMatrix(deltaMean, col)), 0, True)
        # dibagi dengan norm
        temp = multiplyByConstRow(temp, magnitudeVector(temp))
        eigFaces.append(temp)
        print("eigen face progress: {:3.2f}%".format((i/len(eigenVectors[0]))*100))
    eigFaces = transpose(eigFaces)
    return eigFaces

def Omega(faces, deltaMean):
    omegaMat = multiplyMatrix(transpose(deltaMean),faces)
    # for i in range(len(deltaMean[0])):
    #     for j in range(len(faces[0])):
    #         temp = multiplyMatrix(np.array(getCol(deltaMean, i, False)).reshape(256, 256), np.array(getCol(faces, j, False)).reshape(256, 256))
    #         omegaMat.append(np.array(temp).flatten())
    #     print("omega progress: {:3.2f}%".format((i/len(deltaMean[0]))*100))
    return transpose(omegaMat)

# def euclidean_distance(x, faces):
#     currMin = 1e10
#     for i in range(len(faces)):
#         y = np.array(faces[i]).flatten()
#         distance = (sum((magnitudeMatrix(px) - magnitudeMatrix(py))**2  for px, py in zip(x,y)))**0.5
#         if distance<currMin:
#             currMin = distance
#             face = y
#     return face.reshape(256, 256)