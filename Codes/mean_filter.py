import numpy as np


def mean(size):

    row = size
    column = size

    center_x = row//2
    center_y = column//2

    kernel = np.ones((size, size), dtype=float) / (size**2)
    normalized_kernel = kernel * (size**2)

    print("Mean kernel : ")
    print(kernel)
    print(normalized_kernel)
    return kernel

mean(3)