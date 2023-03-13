import numpy as np
import matplotlib.pyplot as plt

fc = 0.1
n = 51

h = np.ones(n)
h[int((n-1)/2)] -= 2 * fc
h = h / np.sum(h)

freq = np.fft.fftfreq(n, d=1)
filter_response = np.abs(np.fft.fft(h))

fig, axs = plt.subplots(2, 1)
axs[0].plot(h)
axs[0].set_title('Highpass Filter Kernel')
axs[1].plot(freq, filter_response)
axs[1].set_title('Highpass Filter Frequency Response')
plt.show()
