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
    copy = np.copy(Matrix)
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

# {fungsi yang mengembalikan suatu matrix yang dijadikan 1 baris dengan konkatenasi}
# hasil yang dikembalikan adalah matrix berdimensi 1xCol yang merupakan seluruh elemen matrix yang dijadikan satu baris
def intoOneRowMat(Matrix):
    oneRow = [np.array(Matrix).flatten()]
    return oneRow
# {fungsi yang mengembalikan suatu matrix yang dijadikan 1 kolom dengan konkatenasi dan transpose}
def intoOneColMat(Matrix):
    return transpose(intoOneRowMat(Matrix))

# Operasi array
# {fungsi yang menjumlahkan row1 dengan row2}
def addArray(row1, row2):
    result = np.add(row1,row2)
    return result
# {fungsi yang mengurangkan row1 dengan row2}
def subtractArray(row1, row2):
    result = np.subtract(row1,row2)
    return result
# {fungsi yang mengalikan row dengan n}
def multiplyByConstArray(baris, n):
    result = np.array(baris) * n
    return result

# Operasi vektor
# Vektor : 1 kolom matrix yang dijadikan array
# Karena dalam bentuk array, operasi menggunakan fungsi operasi array
# {fungsi yang menghasilkan dot product dari 2 vektor}
def dotProductVector(u, v):
    result = np.dot(u,v)
    return result

# {fungsi yang mengembalikan magnitude vektor u}
def magnitudeVector(u):
    result = 0
    for i in range(len(u)):
        result += u[i]*u[i]
    return (sqrt(result))

# {fungsi yang mengembalikan proyeksi vektor u pada v}
def orthoProjectVector(u, v):
    return (multiplyByConstArray(u, dotProductVector(u,v)/dotProductVector(u,u)))

# Operator Image
# {mengakses semua image di dalam image dan mengeluarkan matrix grayscale yang diresize}
def accessImage (folder):
    tempImg = cv2.imread(folder, cv2.IMREAD_GRAYSCALE)
    image = cv2.resize(tempImg, [256, 256])
    ar = np.array(image)
    matrix = intoOneRowMat(ar)
    return matrix

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
            result.append(np.array(matrix).flatten())
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
            result.append(np.array(matrix).flatten())
            ctr+=1
        ctr=0
    return result

#{fungsi yang mengembalikan matrix kovarian dari suatu matrix}
def deltaMeanAndCovariant(Matrix):
    print(f"ukuran Matrix {np.array(Matrix).shape}")
    dataset = copyMatrix(Matrix)
    row = len(Matrix)
    col = len(Matrix[0])
    #menjumlahkan data-data
    mean = [0 for j in range(col)]
    for i in range(row):
        mean = addArray(mean, dataset[i])
    #dataset dibagi banyak data
    mean = multiplyByConstArray(mean, 1/row)
    meanMat = [mean]
    print("Achieved mean of matrices")
    #dari sini sudah diperoleh nilai mean dari row-row
    #mengurangi row-row dengan mean
    for i in range(row):
        dataset[i] = subtractArray(dataset[i], mean)
    print("Achieved dataset mean")
    #mendapatkan matrix kovarian
    cov = multiplyMatrix(dataset, transpose(dataset))
    print("Achieved covariance matrix")
    #ukuran matrix kovarian: banyak file x banyak file
    return transpose(dataset), transpose(meanMat), cov

# {fungsi yang menghasilkan dekomposisi QR dari suatu matrix}
def QR(Matrix):
    Q = copyMatrix(Matrix)
    row = len(Matrix)
    col = len(Matrix[0])
    for j in range(col):
        u = getCol(Q, j, True)
        v = getCol(Q, j, True)
        for k in range(j-1,0-1,-1):
            uk = getCol(Q, k, True)
            u = subtractArray(u, orthoProjectVector(uk,v))
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
        result.append(EigVec)
    return result

def eigenFaces(eigenVectors, deltaMean):
    eigFaces = []
    for i in range(len(eigenVectors[0])):
        col = getCol(eigenVectors, i, False)
        temp = getRow(transpose(multiplyMatrix(deltaMean, col)), 0, True)
        # dibagi dengan norm
        temp = multiplyByConstArray(temp, magnitudeVector(temp))
        eigFaces.append(temp)
        print("eigen face progress: {:3.2f}%".format((i/len(eigenVectors[0]))*100))
    eigFaces = transpose(eigFaces)
    return eigFaces

def omega(faces, deltaMean):
    omegaMat = multiplyMatrix(transpose(deltaMean),faces)
    # for i in range(len(deltaMean[0])):
    #     for j in range(len(faces[0])):
    #         temp = multiplyMatrix(np.array(getCol(deltaMean, i, False)).reshape(256, 256), np.array(getCol(faces, j, False)).reshape(256, 256))
    #         omegaMat.append(np.array(temp).flatten())
    #     print("omega progress: {:3.2f}%".format((i/len(deltaMean[0]))*100))
    return transpose(omegaMat)

# {fungsi yang mengembalikan euclidean distance dari 2 matrix}
# asumsi dimensi kedua matrix sama
def euclidean_distance(matrix1, matrix2):
    distance = 0
    result = subtractMatrix(matrix1, matrix2)
    for i in range(len(result)):
        for j in range(len(result[0])):
            distance += result[i][j] * result[i][j]
    return sqrt(distance)

def datasetWeight(folder, fileAmount, eigenIteration):
    MATRIX = datasetToArray_FixedAmount(os.getcwd()+folder, fileAmount)
    deltaMean, meanMATRIX, covMATRIX = deltaMeanAndCovariant(MATRIX)
    eigenValues = eigenvalue(covMATRIX, eigenIteration)
    total = sum(eigenValues)
    if (len(MATRIX[0]) > 5):
        temp = 0
        i = 0
        eigenValFilter = []
        while (temp<(0.95*total))and(eigenValues[i]>=1):
            eigenValFilter.append(eigenValues[i])
            temp += eigenValues[i]
            i += 1
    else : 
        eigenValFilter = eigenValues
    eigVecEff = len(eigenValFilter)
    print(f"ukuran eigenValFilter: {len(eigenValFilter)}")
    eigenVectors = eigenvector(covMATRIX, eigenValues)
    print(f"Ukuran eigenVector: {np.array(eigenVectors).shape}")
    tempEigenFaces = eigenFaces(eigenVectors, deltaMean)
    eigenfaces = transpose(transpose(tempEigenFaces)[:eigVecEff])
    print(f"ukuran eigenFace: {len(eigenfaces)} x {len(eigenfaces[0])}")
    result = omega(eigenfaces, deltaMean)
    print(f"ukuran result {np.array(result).shape}")
    return result

def inputWeight(Matrix1Row):
    Matrix = np.array(Matrix1Row).reshape(256,256)
    print(f"ukuran Matrix {np.array(Matrix).shape}")
    dataset = copyMatrix(Matrix)
    row = len(Matrix)
    col = len(Matrix[0])
    mean = [0 for j in range(col)]
    for i in range(row):
        mean = addArray(mean, dataset[i])
    mean = multiplyByConstArray(mean, 1/row)
    meanMat = [mean]
    for i in range(row):
        dataset[i] = subtractArray(dataset[i], mean)
    cov = multiplyMatrix(dataset, transpose(dataset))
    eigenVectors = eigenvector(cov)
    eigenfaces = eigenFaces(eigenVectors, dataset)
    weight = omega(eigenfaces, dataset)
    return weight