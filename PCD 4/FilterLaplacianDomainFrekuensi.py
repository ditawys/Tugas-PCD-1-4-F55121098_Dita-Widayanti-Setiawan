import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('hd.jpg', 0)

dft = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)

M, N = img.shape
k = 5
h = np.zeros((M, N), dtype=np.float32)
h[int(M/2)-k:int(M/2)+k+1, int(N/2)-k:int(N/2)+k+1] = -4
h[int(M/2), int(N/2)-k:int(N/2)+k+1] = 1
h[int(M/2)-k:int(M/2)+k+1, int(N/2)] = 1

f = dft_shift[:, :, 0]*h + 1j*dft_shift[:, :, 1]*h
filtered_dft_shift = np.zeros_like(dft_shift)
filtered_dft_shift[:, :, 0] = np.real(f)
filtered_dft_shift[:, :, 1] = np.imag(f)

filtered_dft = np.fft.ifftshift(filtered_dft_shift)
filtered_img = cv2.idft(filtered_dft)
filtered_img = cv2.magnitude(filtered_img[:, :, 0], filtered_img[:, :, 1])

plt.subplot(121), plt.imshow(img, cmap='gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(filtered_img, cmap='gray')
plt.title('Laplacian Filtered Image'), plt.xticks([]), plt.yticks([])
plt.show()
