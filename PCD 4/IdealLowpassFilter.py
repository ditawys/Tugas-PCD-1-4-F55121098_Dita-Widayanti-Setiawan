import numpy as np
import matplotlib.pyplot as plt

def ideal_lowpass_filter(shape, cutoff, filter_type='low'):
    filter = np.zeros(shape)
    center = (shape[0]//2, shape[1]//2)
    for i in range(shape[0]):
        for j in range(shape[1]):
            distance = np.sqrt((i - center[0])**2 + (j - center[1])**2)
            if filter_type == 'low':
                if distance <= cutoff:
                    filter[i,j] = 1
            elif filter_type == 'high':
                if distance > cutoff:
                    filter[i,j] = 1
    return filter

filter_size = (256, 256)
cutoff_frequency = 32
filter_type = 'low'
filter = ideal_lowpass_filter(filter_size, cutoff_frequency, filter_type)

plt.imshow(filter, cmap='gray')
plt.title('Ideal Lowpass Filter')
plt.show()
