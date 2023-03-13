import numpy as np

x = np.array([1 + 2j, 3 + 4j, 5 + 6j, 7 + 8j])

y = np.fft.fft(x)

print(y)

z = np.fft.ifft(y)

print(z)
