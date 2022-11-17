# COBA BIKIN DULU YANG STEP 2-4 (NANTI BISA DIBENERIN LAGI)

import numpy as np

# {fungsi yang mengembalikan transpose matrix}
# def transpose(Matrix):
#     #Mtr = M yang ditranspose
#     #row Mtr = col M, col Mtr = row M
#     row = length(Matrix)
#     col = length(Matrix[0])
#     M = Matrix
#     Mtr = createMatrix(col, row)
#     temp = [0 for i in range(col)]
#     for i in range(row):
#         for j in range(col):
#             temp[j] = M[i][j]
#         for k in range(col):
#             Mtr[k][i] = temp[k]
#     return Mtr

# Step 2
# meanofmatrix = [[0 for i in range(256)] for j in range(256)]
# for i in range (256):
#     for j in range (256):
#         meanofmatrix[i][j] = meanofmatrix[i][j] + img[i][j]
#         meanofmatrix[i][j] = meanofmatrix / totaldataset

contoh=[[[1,2,3],
        [4,5,6],
        [7,8,9]],
        [[5,5,5],
        [5,5,5],
        [5,5,5]]]

def meanOfMatriks(Matrix):
    matriksMean=[]
    for i in range(0,len(Matrix),1):
        matriksMean.append(np.mean(Matrix[i]),axis=0)
    return matriksMean

print(meanOfMatriks(contoh))

# # Step 3
# for i in range (256):
#     for j in range (256):
#         img[i][j] = img[i][j] - meanofmatrix[i][j]


def selisihNilai(Matrix):
     hasilSelisih=[]
     for i in range(0,len(Matrix),1):
         hasilSelisih = Matrix[i] - meanOfMatriks(Matrix)
     return hasilSelisih

# Step 4
# img[i][j] * transpose(img[i][j])

def covariant(Matrix):
    hasilCovariant=[]
    for i in range(0,len(Matrix),1):
        hasilCovariant.append(np.transpose(Matrix[i])*Matrix[i])
    return hasilCovariant