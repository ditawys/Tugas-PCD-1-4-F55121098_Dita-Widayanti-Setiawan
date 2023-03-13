import cv2

img = cv2.imread('buram.jpg',0)

height, width = img.shape[:2]

kernel_size = 5
sigma = 1.5
kernel = cv2.getGaussianKernel(kernel_size, sigma)
kernel = -1 * (kernel @ kernel.T)
kernel[int(kernel_size/2), int(kernel_size/2)] = kernel[int(kernel_size/2), int(kernel_size/2)] + 2

filtered_img = cv2.filter2D(img, -1, kernel)

cv2.imshow('Original Image', img)
cv2.imshow('Filtered Image', filtered_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
