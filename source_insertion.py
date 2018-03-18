#!/usr/bin/env python
#Generates noisy gaussian sources to test masking
import numpy as np
import matplotlib.pyplot as plt

def source_insertion(n_sources=3, half_width_min=5, half_width_max=30, power_min=3000, power_max=30000, shape=(256, 401)):
	source_array = np.zeros(shape)
	source_locations = []
	
	n_bin_min = half_width_min
	n_bin_max = half_width_max
		
	p_min = power_min
	p_max = power_max

	x_min = n_bin_max
	x_max = shape[1] - n_bin_max
	y_min = n_bin_max
	y_max = shape[0] - n_bin_max

	for i in range(0,n_sources):
		x_pixel = np.random.randint(x_min, x_max)
		y_pixel = np.random.randint(y_min, y_max)
		source_locations.append([x_pixel, y_pixel])
		
		#Need to choose random 'power' and 'binning'
		p = np.random.randint(p_min, p_max) #Amount of samples to get from distribution
		#What's the effect of the bin number on the strength of the signal?
		
		#Multiplying by 2 will give only even numbers.
		n_bins =2*np.random.randint(n_bin_min, n_bin_max) #How many pixels should the noisy_source occupy?
		mean = [0, 0]
		cov = [[1,0],[0,1]]

		detections = np.random.multivariate_normal(mean, cov, p)
		hist_detections = np.histogram2d(detections[:,0], detections[:,1], bins=n_bins)[0]
		n_bins_2 = n_bins/2
		source_array[y_pixel - n_bins_2:y_pixel + n_bins_2, x_pixel - n_bins_2:x_pixel + n_bins_2] += (hist_detections)
	
	return source_array, source_locations
	
		

	
