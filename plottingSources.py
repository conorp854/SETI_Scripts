# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 17:48:52 2016

@author: Conor

EPSSC179
Will output a plot of the exoplanets viewed with the GBT on 15th April 2016.
The output then needs to be edited manually including zooming in on the
area of interest and adding tick values. 
"""
import matplotlib.pyplot as plt

import numpy as np
from math import pi
from astropy import units as u
#import astropy.coordinates as coord
from astropy.coordinates import SkyCoord, Angle
#from astropy.utils import iers
#2016iers.IERS.iers_table = iers.IERS_A.open(iers.IERS_A_URL)
encoding = "utf-8"

#Creating array to hold the exoplanet data
exo_RaDec = np.genfromtxt('unsorted.cat', dtype=None)
exo_plot_ra = []
exo_plot_dec = []

#Create SkyCoord object and hold each source RA and DEC in array
for i in range(len(exo_RaDec)):
    source_Name = exo_RaDec[i][0].decode(encoding)
    source_RA = exo_RaDec[i][1].decode(encoding)
    source_DEC = exo_RaDec[i][2].decode(encoding)
    
    source_RA = source_RA[0:2] + 'h' + source_RA[3:5] + 'm' + source_RA[6:11] + 's'
    source_DEC = '+' + source_DEC[0:2] + 'd' + source_DEC[3:5] + 'm' + source_DEC[6:11] + 's'
    
    source = SkyCoord(source_RA, source_DEC)
    
    source_ra = (source.ra).value
    source_dec = (source.dec).value
    
    exo_plot_ra.append(source_ra)
    exo_plot_dec.append(source_dec)
    
###Read in Kepler field
kepler_field_RADEC = np.genfromtxt('kepler.coords.clean.txt')
kepler_plot_RA = []
kepler_plot_DEC = []

for i in range(len(kepler_field_RADEC)):
    kepler_plot_RA.append(kepler_field_RADEC[i][4])
    kepler_plot_DEC.append(kepler_field_RADEC[i][5])

###Plotting 
ra_kep = Angle(kepler_plot_RA*u.degree)
ra_kep = ra_kep.wrap_at(180*u.degree)
dec_kep = Angle(kepler_plot_DEC*u.degree)

ra = Angle(exo_plot_ra*u.degree)
ra = ra.wrap_at(180*u.degree)
dec = Angle(exo_plot_dec*u.degree)

fig = plt.figure(figsize=(100,80))
ax = fig.add_subplot((111), projection="mollweide")
ax.scatter(ra.radian, dec.radian, color = 'r', s = 0.5)
ax.scatter(ra_kep.radian, dec_kep.radian, color = 'b', s = 0.4)

for i in range(len(exo_plot_ra)):
    beam_width = (8.4/60)*(pi/180)
    ###Convert to radians as that is what the projection requires
    beam_circle = plt.Circle(((ra[i].radian), (dec[i].radian)), beam_width, fc='none', color='g')
    ax.add_patch(beam_circle)

#Adding minor ticks to the plot
minor_x_ticks = np.arange(-90*(pi/180), -31*(3/180), 3*30*(pi/180)*(1/30))
minor_y_ticks = np.arange(30*(pi/180), 61*(3/180), 3*15*(pi/180)*(1/15))

ax.set_xticklabels(['14h','16h','18h','20h','22h','0h','2h','4h','6h','8h','10h'])
ax.set_xticks(minor_x_ticks, minor=True)
ax.set_yticks(minor_y_ticks, minor=True)
ax.grid(which='minor', linewidth = 1)
ax.grid(which='major', linewidth = 1.2, linestyle='-')

#ax.set_yticklabels([])
ax.grid(True)
    
fig.savefig("sourcesPlot.pdf")
