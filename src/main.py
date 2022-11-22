#disini tinggal manggil fungsi-fungsi
#note: panggil fungsi datasetToArray sekali aja, simpan ke matrix
#usahakan panggil matrix itu sebagai copynya, biar ngga manggil lagi

# from PIL import Image
import numpy as np
import os
from numpy import *
import functions as fun
from matplotlib import pyplot as plt
import cv2

# covMATRIX = [
#     [40, 35, 33, 34, 37, 44],
#     [52, 43, 37, 34, 42, 50],
#     [60, 62, 53, 55, 49, 55],
#     [54, 48, 50, 61, 64, 60],
#     [42, 45, 47, 54, 55, 59],
#     [30, 34, 36, 42, 44, 50]
# ]
MATRIX = fun.datasetToArray_FixedAmount(os.getcwd()+"\\test\\dataset", 1)
fileCount = len(MATRIX)
deltaMean, meanMATRIX, covMATRIX = fun.deltaMeanAndCovariant(MATRIX)
# plt.imshow(np.array(meanMATRIX).reshape(256, 256), cmap='gray', vmin=0, vmax=255)
# plt.show()
# plt.imshow(np.array(meanMATRIX).reshape(256, 256), cmap='gray', vmin=0, vmax=255)
# plt.show()
#tiap eigenvector adalah 1 kolom
eigenValues = fun.eigenvalue(covMATRIX, 10)
total = sum(eigenValues)
#menyaring nilai eigen yang kurang dari 1
temp = 0
i = 0
eigenValFilter = []
while (temp<(0.95*total))and(eigenValues[i]>=1):
    eigenValFilter.append(eigenValues[i])
    temp += eigenValues[i]
    i += 1

eigVecEff = len(eigenValFilter)

print(f"ukuran eigenValFilter: {len(eigenValFilter)}")
eigenVectors = fun.eigenvector(covMATRIX, eigenValues)
print(f"Ukuran eigenVector: {np.array(eigenVectors).shape}")
# plt.imshow(np.array(fun.getCol(eigenVectors, 0, False)).reshape(256, 256), cmap='gray', vmin=0, vmax=255)
# plt.show()
# langkah test image
# misal udah punya eigFaces dan ada matrix test image
# print(np.array(eigenVectors))
tempEigenFaces = fun.eigenFaces(eigenVectors, deltaMean)
eigenFaces = transpose(transpose(tempEigenFaces)[:eigVecEff])
# plt.imshow(np.array(fun.getCol(eigenFaces, 29, False)).reshape(256, 256), cmap='gray', vmin=-1e-7, vmax=1e-7)
# plt.show()
# cv2.imshow("Resized image")
print(f"ukuran eigenFace: {len(eigenFaces)} x {len(eigenFaces[0])}")
omega = fun.Omega(eigenFaces, deltaMean)
print(f"ukuran omega {np.array(omega).shape}")

# testImg = fun.accessImage(os.getcwd()+"\src\\dadario.jpg")
# testImg = fun.subtractMatrix(testImg, meanMATRIX)
# plt.imshow(np.array(testImg).reshape(256, 256), cmap='gray', vmin=0, vmax=255)
# plt.show()
# testEigenValues = fun.eigenvalue(np.array(testImg).reshape(256, 256), 10)
# testEigenVectors = fun.eigenvector(np.array(testImg).reshape(256, 256), testEigenValues)
# testEigenFace = fun.eigFaces(testEigenVectors, testImg)
# print(np.array(testEigenFace).reshape(256, 256))
# plt.imshow(np.array(testEigenFace).reshape(256, 256), cmap='gray', vmin=0, vmax=255)
# plt.show()
# plt.imshow(np.array(testImg).reshape(256, 256), cmap='gray', vmin=0, vmax=255)
# plt.show()
# Cari eigenValue dari test image
# # Omega = np.linalg.solve(eigenFaces, testImg)
# # print("Ukuran Omega", len(Omega), len(Omega[0]))
# print(np.array(eigenValues))
# print("----------------------")
# print(np.array(eigenVectors))
