import cv2
import numpy as np

img = cv2.imread('bulan.png')

kernel = np.ones((3,3),np.float32)/9

smoothed = cv2.filter2D(img,-1,kernel)

kernel_hp = np.array([[-1,-1,-1],[-1,9,-1],[-1,-1,-1]])

unsharp_mask = cv2.filter2D(smoothed,-1,kernel_hp)

sharpened = cv2.add(img,unsharp_mask)

cv2.imshow('Unsharp Masking', sharpened)
cv2.waitKey(0)
cv2.destroyAllWindows()
