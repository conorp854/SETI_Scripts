#! /usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.image as mpimg

samples_amount_block = 1024

file_name = "c000p0.bin"
fh = open(file_name, 'rb')
waterfall_blocks = []

for i in range(0,2048):
	sample_block = np.fromfile(fh, dtype=np.complex64, count=samples_amount_block, sep='')
	fft_samples = np.fft.fft(sample_block)
	fft_samples = np.fft.fftshift(fft_samples)#Change order of fft samples
	waterfall_blocks.append((np.abs(fft_samples)**2))
#print((sample_block))
plt.imshow(waterfall_blocks, aspect='auto', extent=[(-3.125*(10**6)/2),(3.125*(10**6)/2),0, 100]) 
plt.show()	





