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

# folder = "\\test\\nyoba"
folder = "\\test\\dataset"
dirInput = "src\\test1.jpg"
# dirInput = "src\\test1.jpg"

fun.recognition(folder, dirInput, -1, 10)