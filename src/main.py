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

folder = "\\test\\dataset"
INPUT = fun.accessImage('src\\test.jpg')

deltaMean, meanTraining, datasetEigFaces, weightTraining = fun.datasetProcess(folder, 1, 1)
inputEigFaces, weightInput = fun.inputProcess(INPUT, meanTraining, 1, datasetEigFaces)


print(f"ukuran datasetEigFaces {np.array(datasetEigFaces).shape}")
print(f"ukuran weight train {np.array(weightTraining).shape}")
print(f"ukuran inpEigFaces {np.array(inputEigFaces).shape}")
print(f"ukuran weight input {np.array(weightInput).shape}")

# for i in range(len(weightTraining[0])):
#     fun.euclidean_distance(weightInput, fun.getCol(weightTraining, i, False))

minDistance = fun.euclidean_distance(weightInput, fun.getCol(weightTraining, 0, True))
indexMin = 0
for i in range(1, len(weightTraining[0])):
    distance = fun.euclidean_distance(weightInput, fun.getCol(weightTraining, i, True))
    if (distance < minDistance):
        indexMin = i
        minDistance = distance

weightResult = fun.getCol(weightTraining, indexMin, True)
output = fun.createMatrix(len(datasetEigFaces), 1)
for i in range(len(weightResult)):
    output = fun.addMatrix(output, fun.multiplyByConstMatrix(fun.getCol(datasetEigFaces, i, False), weightResult[i]))
output = fun.addMatrix(output, meanTraining)
unfold = np.array(output).reshape(256,256)
plt.imshow(unfold, cmap = 'gray')
plt.show()