import cv2
import numpy as np

def merge_1d_arrays():
    roi1 = np.array([0, 1, 2]) # 3, 1
    roi2 = np.array([4, 8, 7]) # 3, 1
    roi3 = np.array([3, 6, 9]) # 3, 1
    result = cv2.merge((roi1, roi2, roi3)) # 3, 1, 4
    print(roi1.shape)
    # roi1 = [0 1 2]
    print(roi2.shape)
    # roi1 = [4 8 7]
    print(roi3.shape)
    # roi1 = [3 6 9]
    print()
    print(result.shape)
    print(result)
    # result = [
    #     [
    #         [0 4 3]
    #     ]
    #     [
    #         [1 8 6]
    #     ]
    #     [
    #         [2 7 9]
    #     ]
    # ]
    print()
    result2 = cv2.merge((result, result, result))
    print(result2.shape)
    print(result2)
    # result2 = [
    #     [
    #         [0 4 3 0 4 3 0 4 3]
    #     ]
    #     [
    #         [1 8 6 1 8 6 1 8 6]
    #     ]
    #     [
    #         [2 7 9 2 7 9 2 7 9]
    #     ]
    # ]
    print()

def merge_2d_arrays():
    roi1 = np.array([
        [0, 1, 2],
        [10, 11, 12],
    ])
    roi2 = np.array([
        [4, 8, 7],
        [24, 28, 27],
    ])
    roi3 = np.array([
        [3, 6, 9],
        [33, 36, 39],
    ])
    print(roi1.shape)
    print(roi2.shape)
    print(roi3.shape)
    print()
    result = cv2.merge((roi1, roi2, roi3))
    print(result.shape)
    print(result)
    print()

def run():
    # merge_1d_arrays()
    merge_2d_arrays()
