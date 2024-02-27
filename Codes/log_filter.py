import numpy as np
import math


def log(sigma=1.4):

    row = math.floor(7 * sigma)
    column = math.floor(7 * sigma)

    if (row % 2 == 0):
        row += 1
    if (column % 2 == 0):
        column += 1

    center_x = row // 2
    center_y = column // 2

    constant = -1/(math.pi*sigma**4)
    kernel=np.zeros((row,column))

    for x in range(row):
        for y in range(column):
            value=(((x-center_x)**2)+((y-center_y)**2))/(2*sigma**2)
            kernel[x][y]=constant*(1-value)*math.exp(-value)

    minimum = np.min(np.abs(kernel))
    normalized_kernel = kernel / minimum
    normalized_kernel = np.round(normalized_kernel).astype(int)

    print(kernel)
    print("Normalized kernel : ")
    print(normalized_kernel)
    return kernel

log(1.4)