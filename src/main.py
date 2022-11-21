#disini tinggal manggil fungsi-fungsi
#note: panggil fungsi datasetToArray sekali aja, simpan ke matrix
#usahakan panggil matrix itu sebagai copynya, biar ngga manggil lagi

from PIL import Image
import numpy as np
import os
from numpy import *
import functions as fun


MATRIX = fun.datasetToArray_FixedAmount("../test/dataset/", 1)
deltaMean, covMATRIX = fun.deltaMeanAndCovariant(fun.copyMatrix(MATRIX))
fileCount = len(MATRIX)
#tiap eigenvector adalah 1 kolom
eigenValues = fun.eigenvalue(covMATRIX, 20)
eigenVectors = fun.eigenvector(covMATRIX, eigenValues)



# langkah test image
# misal udah punya eigFaces dan ada matrix test image
# eigenFaces = fun.eigFaces(eigenVectors, deltaMean)
# testImg = [[]]
# Cari eigenValue dari test image
# testImg = fun.subtractMatrix(testImg, deltaMean)
# Omega = np.array(np.linalg.solve)
# testEigVal = fun.eigenvalue(eigenFaces, testImg)
