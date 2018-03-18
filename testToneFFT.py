#! /usr/bin/env python

import numpy as np
#import matplotlib.pyplot as plt

samples_amount = 2**20
file_name = "c000p1.bin"
samples = np.fromfile(file_name, dtype=np.complex64, count=samples_amount, sep='')

fft_samples = np.fft.fft(samples)

n = samples.size

timestep = 3.2*(10**(-7))

samples_freq = np.fft.fftfreq(n, timestep)

print(np.max(samples_freq))

#plt.plot(samples_freq, np.abs(fft_samples)**2) #Plotting power spectrum

#plt.show()
