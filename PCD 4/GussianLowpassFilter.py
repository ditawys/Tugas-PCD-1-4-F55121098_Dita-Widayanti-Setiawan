import cv2
import numpy as np

def gaussian_kernel(size, sigma):
    kernel = np.zeros((size, size), np.float32)
    m = size // 2
    for x in range(-m, m+1):
        for y in range(-m, m+1):
            kernel[x+m, y+m] = np.exp(-(x**2 + y**2) / (2*sigma**2))
    kernel /= 2*np.pi*sigma**2
    return kernel

def gaussian_filter(image, size, sigma):
    kernel = gaussian_kernel(size, sigma)
    filtered = cv2.filter2D(image, -1, kernel)
    return filtered

img = cv2.imread('hd.jpg', cv2.IMREAD_GRAYSCALE)
filtered_img = gaussian_filter(img, 5, 1)
cv2.imshow('Original Image', img)
cv2.imshow('Filtered Image', filtered_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
