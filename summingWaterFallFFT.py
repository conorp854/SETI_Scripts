#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np

fft_length = 3145728
#fft_length_test = 1024
fft_blocks = 252
delta_t = 3.4133333*(10**(-7))

file_name = "./fftb/c006p0.fftb"
fh = open(file_name, 'rb')

#Need to use allocated array to avoid dynamically allocating very large array every time we append.
waterfall_blocks = np.empty((fft_blocks, fft_length))

#Data here is already in power spectrum form
for i in range(0, fft_blocks):
	FFT_power_block = np.fromfile(fh, dtype=np.float32, count=fft_length)
	#Samples already sorted and calculated by professor
	waterfall_blocks[i] = FFT_power_block

waterfall_sum = np.sum(waterfall_blocks, axis=0)

sum_max_indices = np.argsort(waterfall_sum) #sorts from lowest to highest
plt.imshow(waterfall_blocks[:,sum_max_indices[-1]-200:sum_max_indices[-1]+200])
plt.show()
