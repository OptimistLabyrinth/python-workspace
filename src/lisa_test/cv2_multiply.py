import cv2
import numpy as np


def multiply_1d_arrays():
    arr = np.array([155, 200, 255])
    roi1 = np.array([0, 0, 0])
    roi2 = np.array([1, 1, 1])
    roi3 = np.array([0.3, 0.5, 0.8])
    print(arr.shape)
    print(roi1.shape)
    arrXro1 = cv2.multiply(arr, roi1, dtype=cv2.CV_8U)
    print(arrXro1.shape)
    print(arrXro1)
    # arrXro1 = [
    #     [0]
    #     [0]
    #     [0]
    #     [0]
    # ]
    print()
    arrXro2 = cv2.multiply(arr, roi2, dtype=cv2.CV_8U)
    print(arrXro2.shape)
    print(arrXro2)
    # arrXro2 = [
    #     [155]
    #     [200]
    #     [255]
    #     [  0]
    # ]
    print()
    arrToFloat = arr.astype(np.float32)
    roi3ToFloat = roi3.astype(np.float32)
    print(arrToFloat.shape)
    print(arrToFloat)
    print(roi3ToFloat.shape)
    print(roi3ToFloat)
    arrXro3 = cv2.multiply(arrToFloat, roi3ToFloat, dtype=cv2.CV_8U)
    print(arrXro3.shape)
    print(arrXro3)
    # arrXro3 = [
    #     [ 47]
    #     [100]
    #     [204]
    #     [  0]
    # ]
    print()


def multiply_2d_arrays():
    arr = np.array([
        [100, 200, 250],
        [50, 50, 150],
        [150, 80, 180],
        [30, 230, 200],
    ])
    roi1 = np.array([
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ])
    roi2 = np.array([
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1],
    ])
    roi3 = np.array([
        [0.3, 1, 1],
        [0, 1, 0.2],
        [0.5, 0.5, 0.5],
        [1, 0.8, 0.2],
    ])
    result = cv2.multiply(arr, roi1, dtype=cv2.CV_8U)
    print(result.shape)
    print(result)
    # result = [
    #     [0 0 0]
    #     [0 0 0]
    #     [0 0 0]
    #     [0 0 0]
    # ]
    print()
    result = cv2.multiply(arr, roi2, dtype=cv2.CV_8U)
    print(result.shape)
    print(result)
    # result = [
    #     [100 200 250]
    #     [ 50  50 150]
    #     [150  80 180]
    #     [ 30 230 200]
    # ]
    print()
    arrFloat = arr.astype(np.float32)
    roi3Float = roi3.astype(np.float32)
    result = cv2.multiply(arrFloat, roi3Float, dtype=cv2.CV_8U)
    print(result.shape)
    print(result)
    # result = [
    #     [ 30 200 250]
    #     [  0  50  30]
    #     [ 75  40  90]
    #     [ 30 184  40]
    # ]
    print()


def multiply_scalar():
    height = 10
    width = 8
    matrix = np.zeros((height, width), np.uint8)
    matrix = matrix + 1
    print(matrix)
    matrix = matrix * 255
    print(matrix)


def run():
    # multiply_1d_arrays()
    # multiply_2d_arrays()
    multiply_scalar()

