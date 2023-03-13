import numpy as np

t = np.linspace(0, 1, 1000, endpoint=False)
signal = np.sin(2*np.pi*10*t) + np.sin(2*np.pi*20*t)

fft = np.fft.fft(signal)

freq = np.fft.fftfreq(signal.size, d=t[1]-t[0])

import matplotlib.pyplot as plt
plt.plot(freq, np.abs(fft))
plt.xlabel('Frequency')
plt.ylabel('Amplitude')
plt.show()
