import numpy as np
from scipy.signal import butter, filtfilt
import matplotlib.pyplot as plt


fs = 1000
t = np.arange(0, 1, 1/fs)
f1 = 10
f2 = 50
signal = np.sin(2*np.pi*f1*t) + 0.1*np.sin(2*np.pi*f2*t)

fc = 20
order = 4
Wn = fc / (fs/2)
b, a = butter(order, Wn, 'low')

filtered_signal = filtfilt(b, a, signal)

fig, ax = plt.subplots(2, 1, figsize=(10, 6))
ax[0].plot(t, signal)
ax[0].set_title('Original Signal')
ax[1].plot(t, filtered_signal)
ax[1].set_title('Filtered Signal')
plt.show()
