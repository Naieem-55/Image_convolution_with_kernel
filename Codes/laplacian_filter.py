import numpy as np

def laplacian(size=3):

    row = size
    column = size
    center = size // 2

    # Positive Center
    kernel_positive = np.ones((size, size), dtype=int) * - 1
    kernel_positive[center][center] = (size**2 - 1)

    # Negative Center
    kernel_negative = np.ones((size,size), dtype=int) * 1
    kernel_negative[center][center] = -(size**2 - 1)

    print(kernel_positive)
    print(kernel_negative)

    return (kernel_positive,kernel_negative)

laplacian(3)