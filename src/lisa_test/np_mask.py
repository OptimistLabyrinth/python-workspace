import numpy as np

def run():
    arr = np.array([
        [1, 2, 3, 4],
        [1, 2, 3, 4],
    ])
    mask = np.array([
        [True, False, False, True],
        [False, True, True, False],
    ])

    arr[mask] = 77
    print(arr)
