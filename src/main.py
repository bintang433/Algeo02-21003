import numpy as np
import os
from numpy import *
import functions as fun
from matplotlib import pyplot as plt
import cv2

folder = "\\test\\nyoba"
INPUT = fun.accessImage('src\\test.jpg')

deltaMean, meanTraining, weightTraining = fun.datasetProcess(folder, -1, 1)
weightInput = fun.inputWeight(INPUT, meanTraining, 1)


print(weightInput)