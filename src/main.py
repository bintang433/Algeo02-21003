#disini tinggal manggil fungsi-fungsi
#note: panggil fungsi datasetToArray sekali aja, simpan ke matrix
#usahakan panggil matrix itu sebagai copynya, biar ngga manggil lagi

from PIL import Image
import numpy as np
import os
from numpy import *
import functions as fun


MATRIX = fun.datasetToArray_FixedAmount("../test/dataset/", 1)
fileCount = len(MATRIX)
deltaMean, meanMATRIX, covMATRIX = fun.deltaMeanAndCovariant(MATRIX)
#tiap eigenvector adalah 1 kolom
eigenValues = fun.eigenvalue(covMATRIX, 3)
#menyaring nilai eigen yang kurang dari 1
eigenValFilter = [i for i in eigenValues if i >= 1]
print(f"ukuran eigenValFilter: {len(eigenValFilter)}")
eigenVectors = fun.eigenvector(covMATRIX, eigenValues)
print(f"Ukuran eigenVector: {len(eigenVectors)} x {len(eigenVectors[0])}")
# langkah test image
# misal udah punya eigFaces dan ada matrix test image
eigenFaces = fun.eigFaces(eigenVectors, deltaMean)
print(f"ukuran eigenFace: {len(eigenFaces)} x {len(eigenFaces[0])}")
testImg = fun.accessImage("src/test.jpg")
# Cari eigenValue dari test image
testImg = fun.subtractMatrix(testImg, meanMATRIX)
print(f"ukuran testImg: {np.array(testImg).shape}")
Omega = np.array(np.linalg.solve(eigenFaces, testImg))
print("Ukuran Omega", len(Omega), len(Omega[0]))