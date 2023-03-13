import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

t = np.linspace(0, 1, 1000, False)
sig = np.sin(10 * 2 * np.pi * t) + np.sin(20 * 2 * np.pi * t)

order = 6
fs = 1000.0
cutoff = 15

b, a = signal.butter(order, cutoff, btype='highpass', fs=fs)

filtered_signal = signal.filtfilt(b, a, sig)

plt.figure(figsize=(10, 7))
plt.plot(t, sig, 'r-', linewidth=1.5, label='Original Signal')
plt.plot(t, filtered_signal, 'k-', linewidth=1.5, label='Filtered Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Butterworth Highpass Filter')
plt.grid(True)
plt.legend()
plt.show()
