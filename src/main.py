#disini tinggal manggil fungsi-fungsi
#note: panggil fungsi datasetToArray sekali aja, simpan ke matrix
#usahakan panggil matrix itu sebagai copynya, biar ngga manggil lagi

from PIL import Image
import numpy as np
import os
from numpy import *
import functions as fun


MATRIX = fun.datasetToArray_FixedAmount("../test/dataset/", 1)
covMATRIX = fun.covariant(fun.copyMatrix(MATRIX))
fileCount = fun.length(MATRIX)
#tiap eigenvector adalah 1 kolom
eigenVectors = fun.eigenvector(covMATRIX)